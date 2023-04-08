from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .models import User

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(login=form.cleaned_data['login']).exists():
                form.add_error('login', 'Пользователь с таким логином уже существует')
            else:
                user = User(
                    name=form.cleaned_data['name'],
                    login=form.cleaned_data['login'],
                    password=form.cleaned_data['password']
                )
                user.save()
                user = authenticate(request, username=user.login, password=user.password)
                login(request, user)
                return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': form})