from django.contrib import admin
from django.urls import path, include
from ecommerce_app.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="check"),
    path('contactus', contactus, name="contactus"),
    path('aboutus', aboutus, name="aboutus"),
    path('products', products, name="products"),
    path('single_projuct', single_projuct, name="single_projuct"),
    path('productview', login_required(ProductView.as_view()), name="productview"),
    path('carts', login_required(CartView.as_view()), name="carts"),
    path('cartss', login_required(CartsView.as_view()), name="cartss"),
    path('buy', login_required(Buynow.as_view()), name="buy"),
    path('order', order, name="order"),
    path('orderajax', orderajax, name="orderajax"),
    path('cancelorder', login_required(Cancelorder.as_view()), name="cancelorder"),
    path('lowtohigh', login_required(Lowtohigh.as_view()), name="lowtohigh"),
    path('hightolow', login_required(HightoLow.as_view()), name="hightolow"),
]
