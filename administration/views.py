from django.shortcuts import render
from rest_framework import generics

from .models import CB_Driver_Master
from user.models import CB_Trans_Table
from .serializers import DriverSerializer, TransSerializer


from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render(request, 'login.html')


class DriverList(generics.ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = CB_Driver_Master.objects.all()

class BookingList(generics.ListCreateAPIView):
    serializer_class = TransSerializer
    queryset = CB_Trans_Table.objects.all()


# class DriverList(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = DriverSerializer
#     queryset = CB_Driver_Master.objects.all()
        
