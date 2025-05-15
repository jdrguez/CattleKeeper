from django.urls import path
from . import views

app = 'accounts'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('me/', views.user_detail, name='user-detail'),
    path('user/edit/', views.edit_profile, name='edit-profile')
]
