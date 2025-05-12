from ..models.expenses import Expense, AnimalBatch
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from shared.decorators import method_required, valid_token, required_fields, authenticated_user
from ..serializers.production import ProductionSerializer
from ..helpers import expense_exist
import json
from django.db.models import Sum
from django.db.models import Q

@csrf_exempt
@method_required('get')
def all_expenses(request):
    expenses = Expense.objects.all().order_by('-date')
    category = request.GET.get('category')
    batch = request.GET.get('batch')
    if category:
        expenses = expenses.filter(category=category)
    if batch:
        expenses = expenses.filter(batch__slug=batch)
    data = [
        {
            'batch': expense.batch.name,
            'category': expense.category,
            'description': expense.description,
            'amount': str(expense.amount),
            'date': expense.date
        }
        for expense in expenses
    ]
    return JsonResponse({'results': data})


@csrf_exempt
@method_required('get')
def expense_summary(request):
    summary = Expense.objects.values('category').annotate(total=Sum('amount'))
    return JsonResponse({'summary': list(summary)})

@csrf_exempt
@method_required('post')
def expense_create(request):
    data = json.loads(request.body)
    category = data.get('category')
    batch = AnimalBatch.objects.get(slug=data.get('batch'))
    description = data.get('description')
    amount = data.get('amount')
    date = data.get('date')
    currency = data.get('currency', '€')
    
    expense = Expense.objects.create(
        category=category,
        batch=batch,
        description=description,
        amount=amount,
        date=date,
        currency=currency
    )
    return JsonResponse({'message': 'Expense created successfully', 'id': expense.id}, status=201)

@csrf_exempt
@method_required('post')
@expense_exist
def expense_update(request, expense_pk):
    expense = request.expense
    data = json.loads(request.body)
    expense.category = data.get('category', expense.category)
    expense.description = data.get('description', expense.description)
    expense.amount = data.get('amount', expense.amount)
    expense.date = data.get('date', expense.date)
    expense.currency = data.get('currency', expense.currency)
    expense.save()
    return JsonResponse({'message': 'Expense updated successfully', 'id': expense.pk})

@csrf_exempt
@method_required('delete')
@expense_exist
def expense_delete(request, expense_pk):
    expense = request.expense
    expense.delete()
    return JsonResponse({'message': 'Expense deleted successfully'}, status=204)
