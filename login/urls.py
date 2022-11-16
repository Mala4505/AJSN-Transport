# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from django.views.generic.base import TemplateView 


urlpatterns = [
    path('', views.login_user, name='login'),    
    # path('', views.home, name='home'),

    # path('', TemplateView.as_view(template_name='home.html'), name='home')

    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
