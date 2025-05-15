from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
import json
<<<<<<< HEAD
from shared.decorators import method_required, check_json_body, required_fields, valid_token
from .models import Token
from .forms import EditProfileForm

=======
from shared.decorators import method_required, check_json_body, required_fields
from .models import Token, Profile
>>>>>>> 37bf2ceac1903d94faca4f187456e2fefb82c4e5

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
            print(response.headers)
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
def user_detail(request, username):
    try:
        actual_user = User.objects.get(username=username)
        profile = actual_user.profile
        data = {
            "username": actual_user.username,
            "email": actual_user.email,
            "first_name": actual_user.first_name,
            "last_name": actual_user.last_name,
            "profile": {
                "bio": profile.bio,
                "avatar": profile.avatar.url if profile.avatar else None,
            }
        }
        return JsonResponse(data, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


@csrf_exempt  
@method_required("POST")
@valid_token
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            form = EditProfileForm(data, instance=profile)
        else:
            form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User profile has been successfully updated'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    else:
        data = {
            "username": request.user.username,
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "profile": {
                "bio": profile.bio,
                "avatar": profile.avatar.url if profile.avatar else None,
            }
        }
        return JsonResponse(data, status=200)
