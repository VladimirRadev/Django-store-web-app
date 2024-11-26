from django.shortcuts import render
from .models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.filter(quantity__gt=0).all()
    return render(request, "products/products_list.html", {"products": products})
