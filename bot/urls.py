from django.urls import path

from . import views

urlpatterns = [
    path('bot/bot/', views.bot, name='bot'),
    path('bot/c19/', views.c19, name='c19'),
]