from django.http import JsonResponse
from .models import AnimalBatch, Animal, HealthEvent

def batch_exist(func):
    def wrapper(request, *args, **kwargs):
        try:
            batch = AnimalBatch.objects.get(slug=kwargs['batch_slug'])
            request.batch = batch
            return func(request, *args, **kwargs)
        except AnimalBatch.DoesNotExist:
            return JsonResponse({'error': 'Batch not found'}, status=404)
    return wrapper

def animal_exist(func):
    def wrapper(request, *args, **kwargs):
        try:
            animal = Animal.objects.get(slug=kwargs['animal_slug'])
            request.animal = animal
            return func(request, *args, **kwargs)
        except Animal.DoesNotExist:
            return JsonResponse({'error': 'Animal not found'}, status=404)
    return wrapper

def event_exist(func):
    def wrapper(request, *args, **kwargs):
        try:
            event = HealthEvent.objects.get(slug=kwargs['event_pk'])
            request.event = event
            return func(request, *args, **kwargs)
        except HealthEvent.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)
    return wrapper