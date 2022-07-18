from django.shortcuts import render
from django.shortcuts import render
from ecommerce_app.serializer import *
from ecommerce_app.models import *
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ecommerce_app.forms import BuyForm
from rest_framework.decorators import api_view
from ecommerce_app.forms import CustomUserCreationForm  
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('login')




@api_view(['GET','POST'])
def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            content={'message':'Login successfully','login':True}
        else:
             content={'message':'Enter valid Details', 'login':False}
        return Response(content)
    return render(request, 'login.html')


@api_view(['GET','POST'])
def register(request):  
    form = CustomUserCreationForm()  
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        print(request.POST)
        if form.is_valid():  
            form.save()
            content={'message':'User register successfully', 'register':True}
        else:
            content={'message':form.errors, 'register':False}
        return Response(content)
    return render(request, 'register.html', {'form':form})