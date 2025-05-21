from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from subscription.models import UserSubscription
import json
from shared.decorators import method_required, check_json_body, required_fields, valid_token
from .models import Token, Profile
from .forms import EditProfileForm


@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('username', 'email', 'password')
def signup_user(request):
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        UserSubscription.objects.create(user=user)
        serializer = UserSerializer(user, request=request)
        return serializer.json_response()

@csrf_exempt
@method_required('post')
@check_json_body
@required_fields('username', 'password')
def login_user(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            response = JsonResponse({'message': 'Login successful.'})
            response.headers['authorization'] = str(token.key)
            return response
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401) 

@csrf_exempt
@method_required('post')
def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful.'})


@method_required("GET")
@valid_token
def user_detail(request):
    user = User.objects.get(token__key=request.token)
    serilizer = UserSerializer(user, request=request)
    return serilizer.json_response()

@csrf_exempt  
@method_required("POST")
@valid_token
def edit_profile(request):
    user = User.objects.get(token__key=request.token)
    profile = user.profile

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            form = EditProfileForm(data, instance=profile)
        else:
            form = EditProfileForm(request.POST, request.FILES, instance=profile, user=user)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User profile has been successfully updated'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    else:
        serializer = UserSerializer(user, request=request)
        return serializer.json_response()
