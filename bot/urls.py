from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('c19/', views.c19, name='c19'),
    path('c19cd/', views.c19cd, name='c19cd'),
]