from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from user.models import *
from user.serializers import BookingSerializer
from user.forms import *


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        bookings = Form_CB_Trans_Table(request.POST)
        if bookings.is_valid():
            bookings.save()
            context = {'bookings': bookings}
            return render(request, 'test.html', context)

        else:
            print(bookings.errors)
            return render(request, 'home.html')

    else:
        options = CB_Option_Master.objects.all()
        context = {'options':options}
        return render(request, 'home.html', context)
    
    # else:
    #     return render(request, 'home.html')


# @api_view(['POST'])
# def createBooking(request):
#     serializer = BookingSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

