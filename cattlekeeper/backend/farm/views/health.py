from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from shared.decorators import method_required, authenticated_user, user_owner, subscription_status
from ..serializers.health import HealthEventSerializer
from ..models import HealthEvent
from ..helpers import animal_exist, event_exist
import json

@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
@animal_exist
def health_events(request, batch_slug, animal_slug):
    animal = request.animal
    health_events = HealthEvent.objects.filter(animal = animal)
    serializer = HealthEventSerializer(health_events, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@authenticated_user
@subscription_status
@animal_exist
def health_event_create(request, batch_slug, animal_slug):
    animal = request.animal
    data = json.loads(request.body)
    event = HealthEvent.objects.create(
        animal=animal,
        date=data['date'],
        event_type=data['event_type'],
        description=data['description'],
    )
    event.save()
    health_events = HealthEvent.objects.filter(animal=animal)
    serializer = HealthEventSerializer(health_events, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@event_exist
@authenticated_user
@subscription_status
@user_owner
def health_event_update(request, batch_slug, animal_slug, event_pk):
    event = request.event
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    for field in ['date', 'event_type', 'description']:
        if field in data:
            setattr(event, field, data[field])

    event.save()
    return JsonResponse({'message': 'Health event updated'})


@csrf_exempt
@method_required('post')
@event_exist
@authenticated_user
@subscription_status
@user_owner
def health_event_delete(request, batch_slug, animal_slug, event_pk):
    event = request.event
    animal = event.animal
    event.delete()
    return JsonResponse({'message': 'Health event deleted'})
