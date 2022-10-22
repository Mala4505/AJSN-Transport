from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def login_user(request):
    print("Authenticated")

    if request.user.is_authenticated():
        return redirect('home')

    elif request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, pwd=pwd)
        print("Authenticated")

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')

        else:
            messages.success(request, ("There was an error Logging in, Try Again..."))
            return redirect('login')

    else:
        return render(request, 'registration/login.html')



