from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('operacional/', views.operacional, name='operacional'),
    path('tecnico/', views.tecnico, name='tecnico'),
    path('condominio/', views.condominio, name='condominio'),
    path('sobre/', views.sobre, name='sobre'),   
]

