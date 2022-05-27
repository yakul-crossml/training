from django.urls import path
from statsdoc_app.views import *

urlpatterns = [
    path('', home, name='home'),
]
