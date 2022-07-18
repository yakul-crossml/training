from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):   
    dob = models.DateField(verbose_name= 'Birthday',null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    manager=models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='Updated', auto_now=True,null=True)

    class Meta(object):
        unique_together = ('email',)

    def __str__(self):
        return self.username


# Create your models here.
Category_types = (
    ('T_shirt', 'T-Shirt'),
    ('Shirt', 'Shirt'),
)
class Category(models.Model):
    type = models.CharField(max_length=500, choices=Category_types,null=True, blank=True)
    def __str__(self):
        return self.type


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')  
    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True) 


class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "visitor", null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "buyuser", null=True, blank=True) 




