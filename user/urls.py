# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.booking, name='booking'),
    # path('add-booking/', views.createBooking, name='add-booking'),
]
