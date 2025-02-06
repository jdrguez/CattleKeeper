from django.urls import path, include

from .views import get_all_products

app_name='products'


urlpatterns = [
    path('', get_all_products, name='all-products'),
]
