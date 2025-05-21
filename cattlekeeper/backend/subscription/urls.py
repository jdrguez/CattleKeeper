from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_subscription, name='get_subscription'),
    path('status/', views.subscription_status, name='subscription-status'),
    path('plans/', views.plans_list, name='plans_list'),
    path('create/', views.create_subscription, name='create_subscription'),
    path('cancel/', views.cancel_subscription, name='cancel-subscription'),
    path('plans/<plan_pk>/', views.plan_detail, name='plan-detail'),
]