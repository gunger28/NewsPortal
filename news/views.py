from django.http import HttpResponse, HttpResponseRedirect
from .models import News
from newsportal.localization.languagerout import Language
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import date
# from django.contrib.auth import authenticate, login
# from .models import User

from .forms import AddArticle

# Create your views here.

def index(request):
    news = News.objects.order_by('-date')
    
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anonymous'

    dictionary = Language
    # news = [
    #     {'title': 'loyer killed 0', 'text': 'tex0'},
    #     {'title': 'loyer killed 1', 'text': 'tex1'},
    #     {'title': 'loyer killed 2', 'text': 'tex2'},
    #     {'title': 'loyer killed 3', 'text': 'tex3'},
    # ]
    return render(request, "newsportal/newsscroller.html", {'news': news, 'loc': dictionary, 'username': username})


def createarticle(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            form.save()
            return redirect('index')
    else:
        form = AddArticle()
    return render(request, "newsportal/addarticle.html", {'form': form})
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")