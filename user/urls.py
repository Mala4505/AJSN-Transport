# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    # path('add-booking/', views.createBooking, name='add-booking'),
]
