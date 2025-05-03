from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
import json
from shared.decorators import method_required, check_json_body, required_fields

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
            return JsonResponse({'message': 'Login successful.'})
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401) 

@csrf_exempt
@method_required('post')
def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful.'})