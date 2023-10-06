from django.shortcuts import render, redirect, HttpResponse
from project.models import User
from .forms import LoginCaptchaForm, RegisterForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = LoginCaptchaForm(request.POST)

        username = form.cleaned_data['nome']
        password = form.cleaned_data['password']
        user = User.objects.get(nome=username)
        print(user)
        if form.is_valid():  

            if user is not None:
                # Credenciais válidas, efetue o login do usuário
                login(request, user)
                return HttpResponse('Login bem-sucedido!')
            else:
                # Credenciais inválidas
                form.add_error(None, 'Nome de usuário ou senha incorretos.')
                return render(request, 'login.html', {"form": form})

        else:
            return render(request, 'login.html', {"form": form})
    
    else:
        form = LoginCaptchaForm() 
        return render(request, 'login.html', {"form": form})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Salvar o usuário no banco de dados
            novo_usuario = form.save()
            # Redirecionar para a página de sucesso ou outra página apropriada
            LoginForm = LoginCaptchaForm(request.POST)
            return render(request, 'login.html', {"form": LoginForm})
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
