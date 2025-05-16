from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order-list'),
    path('add/', views.add_order, name='add-order'),
    path('<int:order_pk>/', views.order_detail, name='order-detail'),
    path('<int:order_pk>/status/', views.change_order_status, name='change-status'),
    path('<int:order_pk>/pay/', views.pay_order, name='pay-order'),
    path('<int:order_pk>/products/', views.order_product_list, name='order-game-list'),
    path(
        '<int:order_pk>/products/add/',
        views.add_game_to_order,
        name='add-product-to-order',
    ),
]