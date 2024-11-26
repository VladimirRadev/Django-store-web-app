from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.accounts_view),
    path('register/', views.accounts_register),
    path('login/',views.accounts_login),
    path('logout/',views.accounts_logout),
    path('shopping-cart/',views.accounts_shopping_cart),
    path('shopping-cart/empty/',views.accounts_shopping_cart_empty),
    path('orders/',views.accounts_orders),

]