from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import method_required, valid_token, required_fields, authenticated_user
from farm.models import Income, Expense, Production, AnimalBatch
from django.db.models import Sum
from django.utils import timezone

@csrf_exempt
@method_required('get')
def monthly_income_expense_summary(request):
    year = request.GET.get('year')
    if not year:
        year = timezone.now().year
    summary = []
    for month in range(1, 13):
        incomes = Income.objects.filter(date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        expenses = Expense.objects.filter(date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        summary.append({
            'month': month,
            'income': float(incomes),
            'expense': float(expenses),
            'net': float(incomes - expenses)
        })

    return JsonResponse({'year': year, 'monthly_summary': summary})

@csrf_exempt
@method_required('get')
def production_by_type(request):
    summary = Production.objects.values('production_type').annotate(total=Sum('quantity')).order_by('-total')
    return JsonResponse({'production_summary': list(summary)})

@csrf_exempt
@method_required('get')
def expenses_by_category(request):
    summary = Expense.objects.values('category').annotate(total=Sum('amount')).order_by('-total')
    return JsonResponse({'category_summary': list(summary)})


@csrf_exempt
@method_required('get')
def net_income_per_batch(request):
    batches = AnimalBatch.objects.all()
    data = []
    for batch in batches:
        income = batch.incomes.aggregate(total=Sum('amount'))['total'] or 0
        expense = batch.expenses.aggregate(total=Sum('amount'))['total'] or 0
        net = income - expense
        data.append({
            'batch': batch.name,
            'income': float(income),
            'expense': float(expense),
            'net': float(net)
        })

    return JsonResponse({'batches': data})


def animals(request):
    data = [
        ['animals', '2020', '2021', '2022', '2023', '2024', '2025'],
        ['Cows', 10, 13, 14 , 10, 15, 29],
        ['Pigs', 1, 3, 4 , 10, 15, 18],
        ['Sheeps', 25, 30, 14 , 50, 45, 100],
    ]
    return JsonResponse(data, safe=False)