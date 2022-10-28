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
