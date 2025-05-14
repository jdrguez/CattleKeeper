from django.contrib import admin
from .models import MonthlySummary, BatchPerformance


@admin.register(MonthlySummary)
class MonthlySummaryAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'total_income', 'total_expense', 'net_profit', 'created_at')
    ordering = ('-year', '-month')
    search_fields = ('year',)


@admin.register(BatchPerformance)
class BatchPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'batch', 
        'period_start', 
        'period_end', 
        'total_production', 
        'total_income', 
        'total_expense', 
        'net_result', 
        'created_at'
    )

    def net_result(self, obj):
        return obj.total_income - obj.total_expense
    net_result.short_description = "Net Result"
