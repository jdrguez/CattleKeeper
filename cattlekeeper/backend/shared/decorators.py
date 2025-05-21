import json
import re
from json.decoder import JSONDecodeError
from farm.models import AnimalBatch
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from subscription.models import UserSubscription

def auth_required(func):
    def wrapper(request, *args, **kwargs):
        if user := authenticate(
            username=request.json_body['username'], password=request.json_body['password']
        ):
            request.user = user
            return func(request, *args, **kwargs)
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return wrapper


def token_exists(func):
    def wrapper(request, *args, **kwargs):
        try:
            request.user = User.objects.get(token__key=request.token)
            return func(request, *args, **kwargs)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Unregistered authentication token'}, status=401)

    return wrapper


def valid_token(func):
    def wrapper(request, *args, **kwargs):
        auth = request.headers.get('Authorization', 'no existe')
        regexp = 'Bearer (?P<token>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if auth_value := re.fullmatch(regexp, auth):
            request.token = auth_value['token']
            return func(request, *args, **kwargs)
        return JsonResponse({'error': 'Invalid authentication token'}, status=400)

    return wrapper


def method_required(method):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method == method.upper():
                return func(request, *args, **kwargs)
            return JsonResponse({'error': 'Method not allowed'}, status=405)

        return wrapper

    return decorator


def check_json_body(func):
    def wrapper(request, *args, **kwargs):
        try:
            json_body = json.loads(request.body)
            request.json_body = json_body
            return func(request, *args, **kwargs)
        except JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    return wrapper


def user_owner(func):
    def wrapper(request, *args, **kwargs):
        batch = AnimalBatch.objects.get(slug=kwargs['batch_slug'])
        user = request.user
        if batch.owner == user:
            return func(request, *args, **kwargs)
        return JsonResponse({'error': 'User is not the owner of batch'}, status=403)

    return wrapper


def required_fields(*fields):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            json_body = json.loads(request.body)
            for field in fields:
                if field not in json_body:
                    return JsonResponse({'error': 'Missing required fields'}, status=400)
            return func(request, *args, **kwargs)

        return wrapper

    return decorator

def authenticated_user(func):
    def wrapper(request, *args, **kwargs):
        auth = request.headers.get('Authorization', '')
        regexp = r'Bearer (?P<token>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        match = re.fullmatch(regexp, auth)
        if not match:
            return JsonResponse({'error': 'Invalid or missing authentication token'}, status=400)

        token = match['token']
        try:
            request.user = User.objects.get(token__key=token)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Unregistered authentication token'}, status=401)

        return func(request, *args, **kwargs)
    return wrapper



def subscription_status(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        active = UserSubscription.objects.get(user=user).is_active()

        if active:
            return func(request, *args, **kwargs)
        return JsonResponse({'error': 'No Premium active'}, status=402)
    return wrapper