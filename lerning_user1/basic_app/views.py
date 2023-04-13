from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def home(request):
    print('login_ok')
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

def go_login(request):
    print('go_login')
    return render(request,'basic_app/login.html')

def user_login(request):
    print('try')
    if request.method == "POST":
        user  = request.POST['username']
        password = request.POST['password']
        userCheck = authenticate(username=user,password=password)
        if userCheck:
            if userCheck.is_active:
                print("Oh Ho mere user")
                login(request,userCheck)
                return HttpResponseRedirect(reverse('home'))
            else:
                print("Please activate the account")
        else:
            return HttpResponse("Account not active")

    return render(request,'basic_app/login.html')

# Create your views here.
