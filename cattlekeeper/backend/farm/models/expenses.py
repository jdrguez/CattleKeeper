from django.db import models
from .animals import AnimalBatch

class Expense(models.Model):
    class Category(models.TextChoices):
        FEED = "FEED", "Alimento"
        VET = "VET", "Veterinaria"
        MAINTENANCE = "MAINTENANCE", "Mantenimiento"
        LABOR = "LABOR", "Mano de obra"
        EQUIPMENT = "EQUIPMENT", "Equipamiento"
        OTHER = "OTHER", "Otro"

    class Currency(models.TextChoices):
        EUROS = '€', 'Euros'
        DOLLARS = '$', 'Dollars'
        OTHER = '', 'Other'

    batch = models.ForeignKey(AnimalBatch, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=5,
        choices=Currency.choices,
        default=Currency.EUROS
    )
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.amount} ({self.date})"
