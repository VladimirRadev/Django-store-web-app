from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class ShoppingCartProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f" {self.user.username} -> {self.product.title}"

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f" {self.user.username} -> {self.date}"