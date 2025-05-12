from ..models.production import Production
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from shared.decorators import method_required, valid_token, required_fields, authenticated_user
from ..serializers.production import ProductionSerializer
from ..helpers import animal_exist, event_exist, batch_exist, production_exist
import json

@csrf_exempt
@method_required('get')
@batch_exist
def production_list(request, batch_slug):
    productions = Production.objects.filter(batch=request.batch)
    serializer = ProductionSerializer(productions, request=request)
    return serializer.json_response()

from datetime import date

@csrf_exempt
@method_required('post')
@batch_exist
def production_create(request, batch_slug):
    data = json.loads(request.body)

    production = Production.objects.create(
        batch=request.batch,
        production_type=data['production_type'],
        quantity=data['quantity'],
        unit=data['unit'],
        date=date.fromisoformat(data['date']), 
        notes=data.get('notes', '')
    )

    serializer = ProductionSerializer(production, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('post')
@batch_exist
@production_exist
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
def delete_production(request, batch_slug, production_pk):
    production = request.production
    production.delete()
    return JsonResponse({'message': 'Production deleted'})
