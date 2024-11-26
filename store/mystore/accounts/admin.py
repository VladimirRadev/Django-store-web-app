from django.contrib import admin
from .models import ShoppingCartProducts, Order

# Register your models here.
admin.site.register(ShoppingCartProducts)
admin.site.register(Order)
