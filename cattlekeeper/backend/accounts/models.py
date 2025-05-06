from django.db import models
from django.conf import settings
from django.db import models
import uuid

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='cache',
        default='cache/noavatar.png',
    )
    bio = models.TextField(blank=True, null=True)

class Token(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='token',
        on_delete=models.CASCADE,
    )
    key = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)