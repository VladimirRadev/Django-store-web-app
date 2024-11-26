import json
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from accounts.models import ShoppingCartProducts,Order
from products.models import Product
from django.db import transaction

# Create your views here.
def accounts_view(request):
    return render(request,'accounts/accounts_view.html')

def accounts_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("products:list")
    else:
        form = UserCreationForm()
    return render(request,'accounts/accounts_register.html',{"form" : form})


def accounts_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("products:list")
    else:
        form = AuthenticationForm()
    return render(request,'accounts/accounts_login.html',{"form" : form})

def accounts_logout(request):
    logout(request)
    return redirect("/")

def accounts_shopping_cart(request):
    if request.method == "POST":
        product_obj = Product.objects.get(title=request.POST.get("product"))
        product_obj.quantity-=1
        product_obj.save()
        
        if ShoppingCartProducts.objects.filter(user = request.user , product=product_obj).count() > 0 :
            shopping_cart_product = ShoppingCartProducts.objects.get(user = request.user , product=product_obj)
            shopping_cart_product.quantity+=1

        else:
            shopping_cart_product = ShoppingCartProducts()
            shopping_cart_product.user = request.user
            shopping_cart_product.product= product_obj
            shopping_cart_product.quantity=1
        shopping_cart_product.save()

    products = []
    total_sum = 0
    for product in ShoppingCartProducts.objects.filter(user=request.user):
        products.append(product)
        total_sum+= product.product.price * product.quantity
    total_sum= round(total_sum,2)

    return render(request,'accounts/accounts_shopping_cart.html', {"products": products ,"total_sum": total_sum})

def accounts_shopping_cart_empty(request):
    if request.method == "POST":
        products_payload =request.POST.get("products")
        products_payload_dict = json.loads(products_payload)
        for product in products_payload_dict:
            obj = Product.objects.get(title = product["title"])
            obj.quantity += int(product["quantity"])

            obj.save()
            with transaction.atomic():
                ShoppingCartProducts.objects.filter(product=obj).delete()

    return redirect('products:list')

def accounts_orders(request):
    if request.method == "POST":

        products_payload =request.POST.get("products")
        products_payload_dict = json.loads(products_payload)
        for product in products_payload_dict:
            obj = Product.objects.get(title = product["title"])
            with transaction.atomic():
                ShoppingCartProducts.objects.filter(product=obj).delete()

        new_order = Order()
        new_order.user = request.user
        new_order.save()
    orders = Order.objects.filter(user = request.user)
    return render(request,"accounts/accounts_orders.html",{"orders":orders})

