from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    img = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.title
