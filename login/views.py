from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users
from user.views import booking



# @login_required(login_url='/login/')
# @unauthenticated_user
# @allowed_users(allowed_roles=['admin', 'user'])
# def home(request):
#     return render(request, 'home.html')


@unauthenticated_user
def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, pwd=pwd)

        if user is not None:
            login(request, user)
            return redirect(booking)

        else:
            messages.error(request, 'There was an error Logging in, Try Again...')
            return redirect('login')

    else:
        return render(request, 'registration/login.html')



