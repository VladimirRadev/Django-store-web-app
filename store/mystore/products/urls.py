from django.urls import path,include
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.products_list,name='list'),
]