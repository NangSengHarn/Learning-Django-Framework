from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('customer/<int:id>',views.customer),
    path('product/',views.product),
]