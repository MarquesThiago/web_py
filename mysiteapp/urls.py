from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('filter/<int:id_deph>', views.filter, name= 'filter'),
    path('list', views.list, name= 'list')
    
]