from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('filter/<int:pk>', views.Filter.as_view(), name= 'filter'),
    path('list', views.ListDeph.as_view(), name= 'list')
    
]