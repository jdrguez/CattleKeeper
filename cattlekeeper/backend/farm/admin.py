from django.contrib import admin
from .models import AnimalBatch, Animal

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
