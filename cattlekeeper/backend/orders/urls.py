from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add_order, name='add-order'),
    path('<int:order_pk>/products/', views.order_product_list, name='order-game-list'),
    path(
        '<int:order_pk>/products/add/',
        views.add_game_to_order,
        name='add-product-to-order',
    ),
]