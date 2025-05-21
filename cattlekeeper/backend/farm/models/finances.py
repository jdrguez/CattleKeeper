from django.db import models
from .animals import AnimalBatch
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.conf import settings

class Currency(models.TextChoices):
        EUROS = '€', 'Euros'
        DOLLARS = '$', 'Dollars'
        OTHER = '', 'Other'

class Expense(models.Model):
    class Category(models.TextChoices):
        FEED = "FEED", "Feed"
        VET = "VET", "Veterinary"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        LABOR = "LABOR", "Labor"
        EQUIPMENT = "EQUIPMENT", "Equipment"
        OTHER = "OTHER", "Other"

    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', 'Cash'
        BANK_TRANSFER = 'BANK_TRANSFER', 'Bank Transfer'
        MOBILE_PAYMENT = 'MOBILE_PAYMENT', 'Mobile Payment'
        CHECK = 'CHECK', 'Check'
        OTHER = 'OTHER', 'Other'

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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.amount} ({self.date})"


class Income(models.Model):
    class Category(models.TextChoices):
        SALE = 'SALE', 'Sale'
        SUBSIDY = 'SUBSIDY', 'Subsidy'
        DONATION = 'DONATION', 'Donation'
        OTHER = 'OTHER', 'Other'

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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='incomes'
    )

    def __str__(self):
        return f"{self.category} - {self.amount} {self.currency}"

