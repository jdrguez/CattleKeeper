from ..models.finances import Expense, Income
from ..models.animals import AnimalBatch
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from shared.decorators import method_required, valid_token, required_fields, authenticated_user
from ..serializers.finances import ExpenseSerializer, IncomeSerializer
from ..helpers import expense_exist, income_exist
import json
from django.db.models import Sum

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
    serializer = ExpenseSerializer(expenses, request=request)
    return serializer.json_response()

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
    payment_method = data.get('payment_method')
    date = data.get('date')
    currency = data.get('currency', '€')
    
    expense = Expense.objects.create(
        category=category,
        batch=batch,
        description=description,
        amount=amount,
        payment_method = payment_method,
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
    expense.payment_method = data.get('payment_method', expense.payment_method)
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

@csrf_exempt
@method_required('get')
def all_incomes(request):
    incomes = Income.objects.all().order_by('-date')
    category = request.GET.get('category')
    batch = request.GET.get('batch')
    
    # Filtrar por categoría si se proporciona
    if category:
        incomes = incomes.filter(category=category)
    
    # Filtrar por lote si se proporciona
    if batch:
        incomes = incomes.filter(batch__slug=batch)
    
    # Usamos el serializer para convertir los datos en JSON
    serializer = IncomeSerializer(incomes, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('get')
def income_summary(request):
    # Resumen por categoría con el total de la cantidad por categoría
    summary = Income.objects.values('category').annotate(total=Sum('amount'))
    return JsonResponse({'summary': list(summary)})

@csrf_exempt
@method_required('post')
def income_create(request):
    data = json.loads(request.body)
    category = data.get('category')
    batch_slug = data.get('batch')
    batch = AnimalBatch.objects.get(slug=batch_slug)
    description = data.get('description')
    amount = data.get('amount')
    currency = data.get('currency', '€')
    date = data.get('date')
    
    # Crear el nuevo Income
    income = Income.objects.create(
        category=category,
        batch=batch,
        description=description,
        amount=amount,
        currency=currency,
        date=date
    )
    
    # Devolver una respuesta con el id del nuevo Income
    return JsonResponse({'message': 'Income created successfully', 'id': income.id}, status=201)

@csrf_exempt
@method_required('post')
@income_exist
def income_update(request, income_pk):
    income = request.income
    data = json.loads(request.body)
    
    # Actualizar los valores del Income con los datos del request
    income.category = data.get('category', income.category)
    income.description = data.get('description', income.description)
    income.amount = data.get('amount', income.amount)
    income.currency = data.get('currency', income.currency)
    income.date = data.get('date', income.date)
    income.batch = AnimalBatch.objects.get(slug=data.get('batch', income.batch.slug))  # Actualizar lote si es necesario
    
    income.save()
    
    return JsonResponse({'message': 'Income updated successfully', 'id': income.pk})

@csrf_exempt
@method_required('delete')
@income_exist
def income_delete(request, income_pk):
    income = request.income
    income.delete()
    return JsonResponse({'message': 'Income deleted successfully'}, status=204)