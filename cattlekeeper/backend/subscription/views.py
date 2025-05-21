import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import SubscriptionPlan, UserSubscription
from .serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer
from datetime import timedelta
from shared.decorators import valid_token, method_required, authenticated_user

@authenticated_user
@valid_token
@method_required('get')
def plans_list(request):
    plans = SubscriptionPlan.objects.all()
    data = [
        {
            'id': plan.id,
            'name': plan.name,
            'price': float(plan.price),
            'duration_days': plan.duration_days,
        }
        for plan in plans
    ]
    return JsonResponse(data, safe=False)

@authenticated_user
@valid_token
@method_required('get')
def plan_detail(request, plan_pk):
    plan = SubscriptionPlan.objects.get(pk=plan_pk)
    serializer = SubscriptionPlanSerializer(plan, request=request)
    return serializer.json_response()

@authenticated_user
@valid_token
@method_required('get')
def get_subscription(request):
    try:
        sub = request.user.usersubscription
        serializer = UserSubscriptionSerializer(sub, request=request)
        return serializer.json_response()
    except UserSubscription.DoesNotExist:
        return JsonResponse({'error': 'No subscription found'}, status=404)


@csrf_exempt
@authenticated_user
@valid_token
@method_required('post')
def create_subscription(request):
    try:
        data = json.loads(request.body)
        plan_id = data.get('plan_id')
        if not plan_id:
            return JsonResponse({'error': 'Plan ID es obligatorio'}, status=400)

        plan = SubscriptionPlan.objects.get(id=plan_id)
        end_date = timezone.now() + timedelta(days=plan.duration_days)

        UserSubscription.objects.update_or_create(
            user=request.user,
            defaults={'plan': plan, 'end_date': end_date}
        )
        return JsonResponse({'message': 'Suscripción actualizada correctamente'})
    except SubscriptionPlan.DoesNotExist:
        return JsonResponse({'error': 'Plan no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@authenticated_user
@valid_token
@method_required('get')
def subscription_status(request):
    user = request.user
    active = UserSubscription.objects.get(user=user).is_active()
    return JsonResponse({'active': active})


@csrf_exempt
@authenticated_user
@valid_token
@method_required('post')
def cancel_subscription(request):
    try:
        subscription = UserSubscription.objects.get(user=request.user)
        subscription.end_date = timezone.now()
        subscription.save()
        return JsonResponse({'message': 'Suscripción cancelada correctamente'})
    except UserSubscription.DoesNotExist:
        return JsonResponse({'error': 'No tienes una suscripción activa'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)