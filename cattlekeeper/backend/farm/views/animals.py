from django.http import JsonResponse
from shared.decorators import method_required, user_owner, required_fields, authenticated_user, subscription_status
from django.views.decorators.csrf import csrf_exempt
from ..models.animals import AnimalBatch, Animal
from ..serializers.animals import AnimalBatchSerializer, AnimalSerializer
from ..helpers import batch_exist, animal_exist
import json

@csrf_exempt
@method_required('get')
@authenticated_user
def batch_list(request):
    batchs = AnimalBatch.objects.filter(owner=request.user)
    batch_json = AnimalBatchSerializer(batchs, request=request)
    return batch_json.json_response()

@csrf_exempt
@method_required('get')
@batch_exist 
@authenticated_user
@user_owner
def batch_detail(request, batch_slug):
    batch_json = AnimalBatchSerializer(request.batch, request=request)
    return batch_json.json_response()

@csrf_exempt
@method_required('post')
@required_fields('species', 'purchase_date', 'quantity')
@authenticated_user
def batch_create(request):
    data = json.loads(request.body)
    batch = AnimalBatch.objects.create(
        species=data['species'],
        purchase_date=data['purchase_date'],
        sex=data.get('sex', AnimalBatch.Sex.MIXED),
        quantity=data['quantity'],
        origin=data.get('origin', ''),
        owner=request.user,
        notes=data.get('notes', '')
    )

    for i in range(batch.quantity):
            animal = Animal.objects.create(
            batch=batch,
            sex=batch.sex,  
            birth_date=data.get('birth_date', None),  
            weight=data.get('weight', None),  
        )
    serializer = AnimalBatchSerializer(batch, request=request)
    return serializer.json_response()


@csrf_exempt
@method_required('post')
@batch_exist
@authenticated_user
@user_owner
def batch_update(request, batch_slug):
    data = json.loads(request.body)
    batch = request.batch

    batch.species = data.get('species', batch.species)
    batch.purchase_date = data.get('purchase_date', batch.purchase_date)
    batch.sex = data.get('sex', batch.sex)
    batch.origin = data.get('origin', batch.origin)
    batch.notes = data.get('notes', batch.notes)

    batch.save()
    serializer = AnimalBatchSerializer(batch, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('get')
@batch_exist
@authenticated_user
@subscription_status
@user_owner
def animal_list(request, batch_slug):
    batch = request.batch
    animals = batch.animals.all()
    data = [AnimalSerializer(animal, request=request).serialize_instance(animal) for animal in animals]
    return JsonResponse(data, safe=False)

@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
@user_owner
def animal_detail(request, batch_slug, animal_slug):
    animal = Animal.objects.get(slug=animal_slug, batch__slug=batch_slug)
    serializer = AnimalSerializer(animal, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@required_fields('birth_date','weight', 'health_status', 'notes')
@batch_exist
@authenticated_user
@subscription_status
@user_owner
def animal_create(request, batch_slug):
    data = json.loads(request.body)
    batch = request.batch
    animal = Animal.objects.create(
        batch=batch,
        birth_date=data.get('birth_date'),
        weight=data.get('weight'),
        health_status=data.get('health_status', Animal.HealthStatus.HEALTHY),
        notes=data.get('notes', ''),
        sex=batch.sex
    )
    animal.save()
    return JsonResponse({'message': 'Animal created', 'identifier': animal.identifier}, status=201)

@csrf_exempt
@method_required('post')
@animal_exist
@authenticated_user
@subscription_status
@user_owner
def animal_update(request, batch_slug, animal_slug):
    animal = request.animal
    data = json.loads(request.body)
    animal.birth_date = data.get('birth_date', animal.birth_date)
    animal.weight = data.get('weight', animal.weight)
    if isinstance('health_status', int) and 'health_status' in dict(Animal.HealthStatus.choices):
        animal.health_status = 'health_status'
    animal.notes = data.get('notes', animal.notes)
    animal.save()
    return JsonResponse({'message': 'Animal updated', 'identifier': animal.identifier})


@csrf_exempt
@method_required('delete')
@animal_exist
@batch_exist
@authenticated_user
@subscription_status
@user_owner
def animal_delete(request, batch_slug, animal_slug):
    animal = request.animal
    animal.delete()
    return JsonResponse({'message': 'Animal deleted'})

@csrf_exempt
@method_required('delete')
@batch_exist
@authenticated_user
@user_owner
def batch_delete(request, batch_slug):
    batch = request.batch
    batch.delete()
    return JsonResponse({'message': 'Batch deleted'})