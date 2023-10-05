from django.shortcuts import render, redirect, HttpResponse
from project.models import User
from .forms import CaptchaForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)

        if form.is_valid():
            print(request.POST)
            return HttpResponse('dados preenchidos com sucesso')
        else:
            return render(request, 'login.html', {"form": form})
    
    else:
        form = CaptchaForm()
        return render(request, 'login.html', {"form": form})