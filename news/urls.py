from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-article/', views.createarticle, name='createarticle'),
]
