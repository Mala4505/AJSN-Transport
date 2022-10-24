from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from user.models import user_transactions
from user.serializers import BookingSerializer
from user.forms import Form_user_transactions


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        bookings = Form_user_transactions(request.POST)
        if bookings.is_valid():
            bookings.save()
            context = {'bookings': bookings}
            return render(request, 'test.html', context)

        else:
            print(bookings.errors)
            return render(request, 'home.html')

    
    else:
        return render(request, 'home.html')


# @api_view(['POST'])
# def createBooking(request):
#     serializer = BookingSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

