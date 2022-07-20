from django.shortcuts import render
from numpy import product
from .models import Product

# Create your views here.

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})