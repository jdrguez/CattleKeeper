from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import method_required,authenticated_user, subscription_status
from farm.models import Income, Expense, Production, AnimalBatch
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponse
from .tasks import farm_report_pdf

@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
def monthly_income_expense_summary(request):
    user = request.user
    year = request.GET.get('year') or timezone.now().year

    summary = []
    for month in range(1, 13):
        incomes = Income.objects.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        expenses = Expense.objects.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        summary.append({
            'month': month,
            'income': float(incomes),
            'expense': float(expenses),
            'net': float(incomes - expenses)
        })

    return JsonResponse({'year': year, 'monthly_summary': summary})


@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
def production_by_type(request):
    user = request.user
    summary = Production.objects.filter(user=user).values('production_type').annotate(total=Sum('quantity')).order_by('-total')
    return JsonResponse({'production_summary': list(summary)})


@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
def expenses_by_category(request):
    user = request.user
    summary = Expense.objects.filter(user=user).values('category').annotate(total=Sum('amount')).order_by('-total')
    return JsonResponse({'category_summary': list(summary)})


@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
def net_income_per_batch(request):
    user = request.user
    batches = AnimalBatch.objects.filter(owner=user)
    data = []
    for batch in batches:
        income = batch.incomes.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
        expense = batch.expenses.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
        net = income - expense
        data.append({
            'batch': batch.name,
            'income': float(income),
            'expense': float(expense),
            'net': float(net)
        })

    return JsonResponse({'batches': data})


@csrf_exempt
@method_required('get')
@authenticated_user
@subscription_status
def get_report(request):
    user = request.user
    year = request.GET.get('year')
    month = request.GET.get('month')

    farm_report_pdf.delay(user, year, month)
    
    return JsonResponse({
        'status': 'success',
        'message': 'Generated Report'
    })