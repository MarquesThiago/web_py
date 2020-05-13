from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('filter/<int:pk>', views.filter, name= 'filter'),
    path('list', views.ListDeph.as_view(), name= 'list'),
    path("depth/new", views.new_depth, name="new_depth")
]