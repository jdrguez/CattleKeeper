from django.db import models
from .animals import Animal

class HealthEvent(models.Model):
    class EventType(models.TextChoices):
        ILLNESS = 'illness'
        TREATMENT = 'treatment'
        CHECKUP = 'checkup'
        VACCINE = 'vaccine'
        OTHER = 'other'

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='health_events')
    date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    description = models.TextField()
    veterinarian = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.animal.identifier} ({self.date})"
