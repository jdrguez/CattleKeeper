from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_all_products(request):
    return JsonResponse({'producto':'arroz'})