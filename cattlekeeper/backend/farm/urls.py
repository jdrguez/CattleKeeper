from django.urls import path
from .views import animals, finances, health, production

app_name = 'farm'

urlpatterns = [
    path('batch/', animals.batch_list, name='batch-list'),
    path('batch/create/', animals.batch_create, name='batch-create'),
    path('batch/<slug:batch_slug>/', animals.batch_detail, name='batch-detail'),
    path('batch/<slug:batch_slug>/update/', animals.batch_update, name='batch-update'),
    path('batch/<slug:batch_slug>/delete/', animals.batch_delete, name='batch-delete'),
    path('batch/<slug:batch_slug>/animals/', animals.animal_list, name='batch-animals'),
    path('batch/<slug:batch_slug>/animals/create/', animals.animal_create, name='animals-create'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/', animals.animal_detail, name='animal-detail'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/update/', animals.animal_update, name='animal-update'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/delete/', animals.animal_delete, name='animal-delete'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/health/', health.health_events, name='animal-health'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/health/create/', health.health_event_create, name='event-create'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/health/<int:event_pk>/update/', health.health_event_update, name='event-update'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/health/<int:event_pk>/delete/', health.health_event_delete, name='event-delete'),
    path('batch/<slug:batch_slug>/production/', production.production_list, name='production-list'),
    path('batch/<slug:batch_slug>/production/create/', production.production_create ,name='production-create'),
    path('batch/<slug:batch_slug>/production/<int:production_pk>/update/', production.update_production, name='update-production'),
    path('batch/<slug:batch_slug>/production/<int:production_pk>/delete/', production.delete_production, name='delete-production'),
    path('finances/expenses/', finances.all_expenses, name='all-expenses'),
    path('finances/expenses/summary/', finances.expense_summary, name='expenses-summary'),
    path('finances/expenses/create/', finances.expense_create, name='expense-create'),
    path('finances/expenses/<int:expense_pk>/delete/', finances.expense_delete, name='expense-delete'),
    path('finances/incomes/', finances.all_incomes, name='all-inall_incomes'),
    path('finances/incomes/summary/', finances.income_summary, name='incomes-summary'),
    path('finances/incomes/create/', finances.income_create, name='income-create'),
    path('finances/incomes/<int:income_pk>/delete/', finances.income_delete, name='income-delete'),
]
