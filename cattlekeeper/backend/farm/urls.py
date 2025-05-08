from django.urls import path
from .views import animals

app_name = 'farm'

urlpatterns = [
    path('batch/', animals.batch_list, name='batch-list'),
    path('batch/create/', animals.batch_create, name='batch-create'),
    path('batch/<slug:batch_slug>/', animals.batch_detail, name='batch-detail'),
    path('batch/<slug:batch_slug>/update/', animals.batch_update, name='batch-update'),
    path('batch/<slug:batch_slug>/animals/', animals.animal_list, name='batch-animals'),
    path('batch/<slug:batch_slug>/animals/create/', animals.animal_create, name='animals-create'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/', animals.animal_detail, name='animal-detail'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/update/', animals.animal_update, name='animal-update'),
    path('batch/<slug:batch_slug>/animals/<slug:animal_slug>/delete/', animals.animal_delete, name='animal-delete'),
]
