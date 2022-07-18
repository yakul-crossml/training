from ecommerce_app.models import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category', 
            'name', 
            'price', 
            'description',
            'image',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'product',
            'user',
        ]
        depth=1


class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'product',
            'user',
        ]


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = [
            'id',
            'product',
            'user',
        ]
        # fields = '__all__'
        depth = 1

        
class BuysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = [
            'product',
            'user',
        ]
      