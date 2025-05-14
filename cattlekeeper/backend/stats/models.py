from django.db import models
from farm.models import AnimalBatch

class MonthlySummary(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveSmallIntegerField()
    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_expense = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('year', 'month')

    def __str__(self):
        return f"{self.month}/{self.year} Summary"

class BatchPerformance(models.Model):
    batch = models.ForeignKey(AnimalBatch, on_delete=models.CASCADE, related_name='performances')
    period_start = models.DateField()
    period_end = models.DateField()
    total_production = models.DecimalField(max_digits=10, decimal_places=2) 
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Performance {self.batch.name} ({self.period_start} to {self.period_end})"

