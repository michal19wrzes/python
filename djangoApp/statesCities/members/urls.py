

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='loginView'),
    path('changePassword/', auth_views.PasswordChangeView.as_view(), name='passwordChange'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
