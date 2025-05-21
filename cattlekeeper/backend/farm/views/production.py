from ..models.production import Production
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from shared.decorators import method_required, user_owner, authenticated_user, subscription_status
from ..serializers.production import ProductionSerializer
from ..helpers import batch_exist, production_exist
from datetime import date
import json

@csrf_exempt
@method_required('get')
@batch_exist
@authenticated_user
@subscription_status
@user_owner
def production_list(request, batch_slug):
    productions = Production.objects.filter(batch=request.batch)
    serializer = ProductionSerializer(productions, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@batch_exist
@authenticated_user
@subscription_status
def production_create(request, batch_slug):
    data = json.loads(request.body)

    production = Production.objects.create(
        batch=request.batch,
        production_type=data['production_type'],
        quantity=data['quantity'],
        unit=data['unit'],
        date=date.fromisoformat(data['date']), 
        notes=data.get('notes', ''),
        user = request.user
    )

    serializer = ProductionSerializer(production, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@batch_exist
@production_exist
@authenticated_user
@subscription_status
@user_owner
def update_production(request, batch_slug, production_pk):
    data = json.loads(request.body)
    production = request.production

    production.production_type = data['production_type']
    production.quantity = data['quantity']
    production.unit = data['unit']
    production.date = data['date']
    production.notes = data.get('notes', '')
    production.save()

    return JsonResponse({'message': 'Production updated', 'identifier': production_pk})

@csrf_exempt
@method_required('post')
@batch_exist
@production_exist
@authenticated_user
@subscription_status
@user_owner
def delete_production(request, batch_slug, production_pk):
    production = request.production
    production.delete()
    return JsonResponse({'message': 'Production deleted'})
