from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from accounts.models import *

def customer(request,id):
    customer=Customer.objects.get(id=id)
    orders=customer.order_set.all()
    order_count=orders.count()
    return render(request,'accounts/customer.html',{
        'customer':customer,
        'orders':orders,
        'order_count':order_count
    })

def product(request):
    products=Product.objects.all()
    return render(request,'accounts/product.html',{
        'products':products
    })

def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total=orders.count()
    delivered=Order.objects.filter(status="delivered").count()
    pending=Order.objects.filter(status="pending").count()

    return render(request,'accounts/dashboard.html',{
        'customers':customers,
        'orders':orders,
        'total':total,
        'delivered':delivered,
        'pending':pending
    })
