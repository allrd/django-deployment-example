from django.shortcuts import render

def home(request):
    return render(request,'basic_app/index.html')

def base(request):
    return render(request,'basic_app/base.html')