from django.shortcuts import redirect, render
from rest_framework import generics

from django.contrib.auth.decorators import login_required

from login.decorators import unauthenticated_user, allowed_users


from django.contrib import messages
from django.db import connection

from user.models import *
from user.forms import *
from user.serializers import TransSerializer



# @login_required(login_url='/login/')
# @unauthenticated_user
@allowed_users(allowed_roles=['admin', 'user'])
def booking(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:

            Time_From = request.POST['Time_From']
            Time_To = request.POST['Time_To']
            dt = request.POST['dt']

            # slots = cursor.execute(f'''SELECT * FROM maladb.CB_Trans_Table
            #     where (({Time_From} between Time_From and Time_To OR {Time_To} between Time_From and Time_To) OR (Time_From between {Time_From} and {Time_To} OR Time_To between {Time_From} and {Time_To}))
            #     and dt = "{dt}"''')

            slots = cursor.execute(f'''SELECT * FROM maladb.CB_Trans_Table 
                                                where (('{Time_From}' between Time_From and Time_To
                                                OR '{Time_To}' between Time_From and Time_To) OR (Time_From between '{Time_From}' and '{Time_To}' OR Time_To between '{Time_From}' and '{Time_To}')) and dt = "{dt}"''')
                                                
            # row = cursor.fetchall()
            # print(row)

            if slots < 2:
                bookings = Form_CB_Trans_Table(request.POST)

                if bookings.is_valid():
                    bookings.save()
                    messages.error(request, "Booking Complete. Please Wait for the Confirmation...")
                    return redirect(booking)

                else:
                    print(bookings.errors)
                    messages.error(request, "Booking Failed. Please Try Again...")
                    return redirect(booking)
            else:
                    messages.error(request, "This Slot is Currently Full. Please Select Another Slot...")
                    return redirect(booking)


    else:
        options = CB_Option_Master.objects.all()
        context = {'options':options}
        return render(request, 'booking.html', context)

# class BookingList(generics.ListCreateAPIView):
#     serializer_class = TransSerializer
#     queryset = CB_Trans_Table.objects.all()