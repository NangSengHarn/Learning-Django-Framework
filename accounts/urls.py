from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customer/<int:id>',views.customer,name='customers.show'),
    path('product/',views.product,name='product'),
    path('order/create/<int:customerId>',views.orderCreate,name='order.create'),
    path('order/update/<int:orderId>',views.orderUpdate,name='order.update'),
    path('order/delete/<int:orderId>',views.orderDelete,name='order.delete'),
    path('register/',views.register,name='register')


]