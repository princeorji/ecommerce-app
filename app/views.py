from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product': product})

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # provisional values for unauthenticated users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

"""
def checkout(request):
    context = {}
    return render(request, '', context)
"""