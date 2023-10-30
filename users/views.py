from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from users.forms import LoginForms
from users.forms import RegisterForm

# Create your views here.
def login(request):
    form = LoginForms()
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid:
            username = form['username'].value()
            password = form['password'].value()
            
        user = auth.authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Bem-Vindo {username}")
            return redirect('index')
        else:
            messages.error(request, f"Dados de acesso inválidos")
            return redirect('users_login')
            
    return render(request, 'users/login.html', {'form':form })

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            if form['password'].value() != form['repassword'].value():
                messages.error(request, f"Senhas diferentes, confirme novamente.")
                return redirect('users_register')
            
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()
            
            if User.objects.filter(username=username).exists():
                messages.error(request, f"O usuário {username} já existe")
                return redirect('users_register')
            
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_user.save
            messages.error(request, f"O usuário {username} críado com sucesso")
            return redirect('users_login')
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout()
    return redirect('users_login')