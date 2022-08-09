from django.urls import path

from . import views

urlpatterns = [
    path('/bot/', views.bot, name='bot'),
    path('/c19/', views.c19, name='c19'),
]