from django.contrib import admin
from .models import AnimalBatch, Animal, HealthEvent, Production, Expense, Income

@admin.register(AnimalBatch)
class AnimalBatchAdmin(admin.ModelAdmin):
    list_display = ('name','species', 'quantity', 'sex', 'purchase_date', 'owner')
    search_fields = ('name', 'species')
    list_filter = ('species', 'sex', 'purchase_date')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('identifier','batch', 'sex', 'birth_date', 'weight', 'health_status', 'created_at')
    search_fields = ('identifier',)
    list_filter = ('sex', 'health_status', 'created_at')
    prepopulated_fields = {'slug': ['identifier']}

@admin.register(HealthEvent)
class HealthEventAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'event_type', 'description')
    list_filter = ('event_type', 'date')
    search_fields = ('animal__identifier',)
    ordering = ('-date',)

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('batch', 'production_type', 'quantity', 'unit', 'date')
    list_filter = ('production_type', 'unit', 'date')
    search_fields = ('batch__slug', 'notes')
    date_hierarchy = 'date'
    ordering = ['-date']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('batch', 'category', 'amount', 'date')
    list_filter = ('category', 'date', 'batch')
    search_fields = ('description',)
    date_hierarchy = 'date'

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'currency', 'date', 'batch')
    list_filter = ('category', 'currency', 'date')
    search_fields = ('description',)
    ordering = ('-date',)
