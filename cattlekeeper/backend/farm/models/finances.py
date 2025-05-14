from django.db import models
from .animals import AnimalBatch
from django.core.validators import MinValueValidator
from decimal import Decimal

class Currency(models.TextChoices):
        EUROS = '€', 'Euros'
        DOLLARS = '$', 'Dollars'
        OTHER = '', 'Other'

class Expense(models.Model):
    class Category(models.TextChoices):
        FEED = "FEED", "Alimento"
        VET = "VET", "Veterinaria"
        MAINTENANCE = "MAINTENANCE", "Mantenimiento"
        LABOR = "LABOR", "Mano de obra"
        EQUIPMENT = "EQUIPMENT", "Equipamiento"
        OTHER = "OTHER", "Otro"

    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', 'Efectivo'
        BANK_TRANSFER = 'BANK_TRANSFER', 'Transferencia Bancaria'
        MOBILE_PAYMENT = 'MOBILE_PAYMENT', 'Pago Móvil'
        CHECK = 'CHECK', 'Cheque'
        OTHER = 'OTHER', 'Otro'

    batch = models.ForeignKey(AnimalBatch, on_delete=models.SET_NULL, null=True, related_name='expenses')
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField(blank=True)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))]
        )
    currency = models.CharField(
        max_length=5,
        choices=Currency.choices,
        default=Currency.EUROS
    )
    payment_method = models.CharField(
         max_length=20, 
         choices=PaymentMethod.choices, 
         default=PaymentMethod.OTHER
         )
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.amount} ({self.date})"


class Income(models.Model):
    class Category(models.TextChoices):
        SALE = 'SALE', 'Venta'
        SUBSIDY = 'SUBSIDY', 'Subvención'
        DONATION = 'DONATION', 'Donación'
        OTHER = 'OTHER', 'Otro'

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER
    )
    batch = models.ForeignKey('AnimalBatch', on_delete=models.SET_NULL, null=True, blank=True, related_name='incomes')
    description = models.TextField(blank=True)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
        )
    currency = models.CharField(
         max_length=5, 
         choices=Currency.choices, 
         default=Currency.EUROS
         )
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} {self.currency}"

