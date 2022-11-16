# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from .views import DriverList, BookingList

from django.views.generic.base import TemplateView 


urlpatterns = [
    path('test/', views.home, name='home'),
    path('driver/', DriverList.as_view()),
    path('bookings/', BookingList.as_view()),
]
