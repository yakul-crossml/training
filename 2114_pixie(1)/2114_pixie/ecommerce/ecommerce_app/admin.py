from django.contrib import admin
from ecommerce_app.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Buy)

admin.site.register(User , UserAdmin)
