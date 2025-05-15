from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import method_required, valid_token, required_fields, authenticated_user
from farm.models import Income, Expense, Production, AnimalBatch
from django.db.models import Sum
from django.utils import timezone
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from io import BytesIO

@csrf_exempt
@method_required('get')
@authenticated_user
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
def production_by_type(request):
    user = request.user
    summary = Production.objects.filter(user=user).values('production_type').annotate(total=Sum('quantity')).order_by('-total')
    return JsonResponse({'production_summary': list(summary)})


@csrf_exempt
@method_required('get')
@authenticated_user
def expenses_by_category(request):
    user = request.user
    summary = Expense.objects.filter(user=user).values('category').annotate(total=Sum('amount')).order_by('-total')
    return JsonResponse({'category_summary': list(summary)})


@csrf_exempt
@method_required('get')
@authenticated_user
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
def farm_report_pdf(request):
    user = request.user
    year = request.GET.get('year')
    month = request.GET.get('month')

    if not year or not month:
        now = timezone.now()
        year = now.year
        month = now.month
    else:
        year = int(year)
        month = int(month)

    incomes = Income.objects.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
    expenses = Expense.objects.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
    monthly_summary = [{
        'month': month,
        'income': float(incomes),
        'expense': float(expenses),
        'net': float(incomes - expenses)
    }]

    production_summary = list(
        Production.objects.filter(user=user, date__year=year, date__month=month)
        .values('production_type')
        .annotate(total=Sum('quantity'))
        .order_by('-total')
    )

    category_summary = list(
        Expense.objects.filter(user=user, date__year=year, date__month=month)
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    batches_data = []
    for batch in AnimalBatch.objects.filter(owner=user):
        income = batch.incomes.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        expense = batch.expenses.filter(user=user, date__year=year, date__month=month).aggregate(total=Sum('amount'))['total'] or 0
        net = income - expense
        batches_data.append({
            'batch': batch.name,
            'income': float(income),
            'expense': float(expense),
            'net': float(net)
        })

    html_string = render_to_string('farm_report.html', {
        'year': year,
        'month': month,
        'monthly_summary': monthly_summary,
        'production_summary': production_summary,
        'category_summary': category_summary,
        'batches': batches_data,
    })

    html = HTML(string=html_string)
    pdf_file = BytesIO()
    html.write_pdf(target=pdf_file)

    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="farm_report_{year}_{month}.pdf"'
    return response