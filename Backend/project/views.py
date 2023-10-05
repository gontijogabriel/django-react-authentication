from django.shortcuts import render, redirect, HttpResponse
from project.models import User
from .forms import CaptchaForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse('teste')
    else:
        form = CaptchaForm()
        return render(request, 'login.html', {"form": form})