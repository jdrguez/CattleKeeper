from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def animals(request):
    data = [
        ['animals', '2020', '2021', '2022', '2023', '2024', '2025'],
        ['Cows', 10, 13, 14 , 10, 15, 29],
        ['Pigs', 1, 3, 4 , 10, 15, 18],
        ['Sheeps', 25, 30, 14 , 50, 45, 100],
    ]
    return JsonResponse(data, safe=False)