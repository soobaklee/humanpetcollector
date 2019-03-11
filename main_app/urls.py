from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets, name='pets'),
    path('mypets/', views.mypets, name='mypets')
]