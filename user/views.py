from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from user.models import AT_transaction
from user.serializers import BookingSerializer


@login_required(login_url='/login/')
def home(request):
    # if request.method == 'POST':
    #     bookings = JSONParser().parse(request)
    #     bookings_serializers = BookingSerializer(data=bookings)
    #     if bookings_serializers.is_valid():
    #         bookings_serializers.save()
    #         return JsonResponse("Booking is complete. We will inform you shortly for the Confirmation...", safe=False)
    #     return JsonResponse("Booking Failed...", safe=False)
    
    # else:
        return render(request, 'home.html')


@api_view(['POST'])
def createBooking(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# @login_required(login_url='/login/')
# def user_bookings(request):

