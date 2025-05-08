from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db import models

class AnimalBatch(models.Model):
    class Sex(models.IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'
        MIXED = 3, 'Mixed'

    class Species(models.IntegerChoices):
        CATTLE = 1, 'Cattle'
        POULTRY = 2, 'Poultry'
        PIG = 3, 'Pig'
        SHEEP = 4, 'Sheep'
        GOAT = 5, 'Goat'
        OTHER = 99, 'Other'

    name = models.CharField(max_length=10, unique=True, blank=True)
    species = models.IntegerField(choices=Species.choices, default=Species.OTHER)
    purchase_date = models.DateField()
    sex = models.IntegerField(choices=Sex.choices, default=Sex.MIXED)
    quantity = models.PositiveIntegerField()
    origin = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.name:
            species_letter = self.get_species_display()[0].upper() 
            sex_letter = self.get_sex_display()[0].upper()         
            last_batch = AnimalBatch.objects.order_by('-id').first()
            next_id = last_batch.id + 1 if last_batch else 1
            self.name = f"{species_letter}-{sex_letter}{next_id:03d}" 
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def update_quantity(self):
        actual_count = self.animals.count()
        if self.quantity != actual_count:
            self.quantity = actual_count
            self.save()

    def __str__(self):
        return f"Batch {self.name} ({self.get_species_display()})"

class Animal(models.Model):
    class HealthStatus(models.IntegerChoices):
        HEALTHY = 1, 'Healthy'
        SICK = 2, 'Sick'
        RECOVERING = 3, 'Recovering'
        DEAD = 4, 'Dead'

    batch = models.ForeignKey('AnimalBatch', on_delete=models.CASCADE, related_name='animals')
    identifier = models.CharField(max_length=100, unique=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    health_status = models.IntegerField(choices=HealthStatus.choices, default=HealthStatus.HEALTHY)
    sex = models.IntegerField(choices=AnimalBatch.Sex.choices, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            last_animal = Animal.objects.filter(batch=self.batch).order_by('-id').first()
            next_id = last_animal.id + 1 if last_animal else 1
            self.identifier = f"{self.batch.name}-{next_id:03d}"
        if not self.slug:
            self.slug = slugify(self.identifier)
        if not self.sex:
            self.sex = self.batch.sex
        super().save(*args, **kwargs)

    def __str__(self):
        return self.identifier
