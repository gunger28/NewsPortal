from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm, SearchForm
from news.models import News
from django.db.models import Q

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'newsportal/registration.html', {'form': form})

def autentefication(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') # Замените 'home' на URL вашей домашней страницы
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'newsportal/log-in.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def userpage(request):
    user = request.user
    return render(request, 'newsportal/userpage.html', {'user': user})

def searchingnews(request):
    query = request.GET.get('query', '')
    form = SearchForm(request.GET)
    articles = []
    if form.is_valid() and query:
        articles = News.objects.filter(title__icontains=query).order_by('title')
    context = {'form': form, 'articles': articles, 'query': query}
    return render(request, 'newsportal/searching-news.html', context)
