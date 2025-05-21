from django.db import models
from .animals import AnimalBatch
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.conf import settings

class Production(models.Model):
    class ProductionType(models.TextChoices):
        MEAT = 'MEAT', 'Meat'
        MILK = 'MILK', 'Milk'
        EGG = 'EGG', 'Eggs'
        WOOL = 'WOOL', 'Wool'

    class Unit(models.TextChoices):
        LITERS = 'L', 'Liters'
        KILOGRAMS = 'KG', 'Kilograms'
        UNITS = 'U', 'Units'

    batch = models.ForeignKey(AnimalBatch, on_delete=models.CASCADE, related_name='productions')
    production_type = models.CharField(max_length=10, choices=ProductionType.choices)
    quantity = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
        )
    unit = models.CharField(max_length=2, choices=Unit.choices)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='production'
    )
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_production_type_display()} - {self.quantity} {self.get_unit_display()} ({self.batch})"
