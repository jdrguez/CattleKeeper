from ..models.finances import Expense, Income
from ..models.animals import AnimalBatch
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from shared.decorators import method_required, authenticated_user, user_owner
from ..serializers.finances import ExpenseSerializer, IncomeSerializer
from ..helpers import expense_exist, income_exist, user_owner_expense, user_owner_income
import json
from django.db.models import Sum

@csrf_exempt
@method_required('get')
@authenticated_user
def all_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
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
@authenticated_user
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
        currency=currency,
        user = request.user
    )
    return JsonResponse({'message': 'Expense created successfully', 'id': expense.id}, status=200)

@csrf_exempt
@method_required('post')
@expense_exist
@authenticated_user
@user_owner_expense
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
@authenticated_user
@user_owner_expense
def expense_delete(request, expense_pk):
    expense = request.expense
    expense.delete()
    return JsonResponse({'message': 'Expense deleted successfully'}, status=200)

@csrf_exempt
@method_required('get')
@authenticated_user
def all_incomes(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    category = request.GET.get('category')
    batch = request.GET.get('batch')
    if category:
        incomes = incomes.filter(category=category)
    if batch:
        incomes = incomes.filter(batch__slug=batch)
    serializer = IncomeSerializer(incomes, request=request)
    return serializer.json_response()

@csrf_exempt
@method_required('get')
def income_summary(request):
    summary = Income.objects.values('category').annotate(total=Sum('amount'))
    return JsonResponse({'summary': list(summary)})

@csrf_exempt
@method_required('post')
@authenticated_user
def income_create(request):
    data = json.loads(request.body)
    category = data.get('category')
    batch_slug = data.get('batch')
    batch = AnimalBatch.objects.get(slug=batch_slug)
    description = data.get('description')
    amount = data.get('amount')
    currency = data.get('currency', '€')
    date = data.get('date')
    income = Income.objects.create(
        category=category,
        batch=batch,
        description=description,
        amount=amount,
        currency=currency,
        date=date,
        user= request
    )
    return JsonResponse({'message': 'Income created successfully', 'id': income.id}, status=200)

@csrf_exempt
@method_required('post')
@income_exist
@authenticated_user
@user_owner_income
def income_update(request, income_pk):
    income = request.income
    data = json.loads(request.body)
    income.category = data.get('category', income.category)
    income.description = data.get('description', income.description)
    income.amount = data.get('amount', income.amount)
    income.currency = data.get('currency', income.currency)
    income.date = data.get('date', income.date)
    income.save()
    return JsonResponse({'message': 'Income updated successfully', 'id': income.pk})

@csrf_exempt
@method_required('delete')
@income_exist
@authenticated_user
@user_owner_income
def income_delete(request, income_pk):
    income = request.income
    income.delete()
    return JsonResponse({'message': 'Income deleted successfully'}, status=200)