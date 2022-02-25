from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('customer/',views.customer),
    path('product/',views.product),
]