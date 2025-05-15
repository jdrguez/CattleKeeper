from django.contrib import admin


from .models import Token, Profile

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'created_at',
    ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'avatar',
        'bio'
    ]