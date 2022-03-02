from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customer/<int:id>',views.customer,name='customers.show'),
    path('product/',views.product,name='product'),
    path('order/create/',views.orderCreate,name='order.create')
]