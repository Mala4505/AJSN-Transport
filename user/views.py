from django.shortcuts import redirect, render

# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from user.models import *
from user.forms import *


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        bookings = Form_CB_Trans_Table(request.POST)
        if bookings.is_valid():
            # answer = bookings.cleaned_data['value']
            bookings.save()
            context = {'bookings': bookings}
            messages = {messages: "Booking Complete. Please Wait for the Confirmation..."}
            return render(request, 'test.html', context, messages)

        else:
            print(bookings.errors)
            messages = {messages: "Booking Failed. Please Try Again..."}
            return render(request, 'home.html', messages)

    else:
        options = CB_Option_Master.objects.all()
        context = {'options':options}
        return render(request, 'home.html', context)
