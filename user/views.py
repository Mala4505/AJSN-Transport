from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        pass
    
    else:
        return render(request, 'home.html')


# @login_required(login_url='/login/')
# def user_bookings(request):

