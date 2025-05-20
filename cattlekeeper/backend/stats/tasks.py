from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django_rq import job
from django.utils import timezone
from farm.models import Income, Expense, Production, AnimalBatch
from django.db.models import Sum
from io import BytesIO
from django.contrib.auth import get_user_model
from weasyprint import HTML

@job
def farm_report_pdf(user, year = None, month = None):
    user = user

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

    pdf_buffer = BytesIO()
    html = HTML(string=html_string)
    html.write_pdf(target=pdf_buffer)
    pdf_buffer.seek(0)

    email = EmailMessage(
        subject=f'Reporte mensual de tu granja - {month}/{year}',
        body='Adjunto encontrarás tu reporte mensaul en PDF',
        from_email=None,
        to=[user.email],
    )

    email.attach(f'report_{month}_{year}.pdf', pdf_buffer.getvalue(), 'application/pdf')
    email.send()
