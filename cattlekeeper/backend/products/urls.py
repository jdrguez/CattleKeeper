from django.urls import path, include
from . import views

app_name='products'

urlpatterns = [
    path('', views.product_list ,name='products-list'),
    path('<str:product_slug>/', views.product_detail ,name='products-detail'),
    path('<str:product_slug>/reviews/', views.review_list, name='review-list'),
    path('reviews/<int:review_pk>/', views.review_detail, name='review-detail'),
    path('<str:product_slug>/reviews/add/', views.add_review, name='add-review'),
]
