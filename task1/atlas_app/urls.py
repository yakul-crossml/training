from django.urls import path
from atlas_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('datatables', datatables, name='datatables'),
]
