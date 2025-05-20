from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('monthly-summary/', views.monthly_income_expense_summary, name='monthly_summary'),
    path('production-summary/', views.production_by_type, name='production_summary'),
    path('expense-category-summary/', views.expenses_by_category, name='expense_category_summary'),
    path('batch-net-income/', views.net_income_per_batch, name='batch_net_income'),
    path('report/pdf/', views.get_report, name='get-report'),
]
