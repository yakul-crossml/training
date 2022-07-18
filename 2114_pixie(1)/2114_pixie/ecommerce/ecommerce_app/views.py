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

# Create your views here.
@login_required
def aboutus(request):
    return render(request, 'about.html')

@login_required
def contactus(request):
    return render(request, 'contact.html')

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

@login_required
def products(request):
    return render(request, 'products.html')

@login_required
def single_projuct(request):
    return render(request, 'single-product.html')

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



def order(request):
    return render(request, 'buy.html')

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderajax(request):
    buy=Buy.objects.filter(user=request.user)
    serializer = BuySerializer(buy, many=True)
    content = {'category': serializer.data}
    return Response(content)



class Buynow(APIView):
    def get(self, request):
        try:
            if request.GET.get('id'):
                productt = Product.objects.get(id=request.GET.get('id'))
                buyserializer = BuysSerializer(data={'product':productt.id, 'user':request.user.id})
                if buyserializer.is_valid():
                    buyserializer.save()
                    content={'message':'Your Order has been placed'}
                return Response(content)
            else:
                buy=Buy.objects.filter(user=request.user)
                return render(request, 'buy.html', {'buy':buy})
        except:
            content={'message':'There should be some issue in placing your order'}
            return Response(content)


class Cancelorder(APIView):
    def get(self, request):
        try:
            if request.GET.get('id'):
                Buy.objects.get(id=request.GET.get('id')).delete()
                content={'message':'Your Order has been successfully cancelled'}
                return Response(content)
        except:
            content={'message':'There should be some issue in cancelling your order'}
            return Response(content)




class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        content = {'category': serializer.data}
        return Response(content)


class CartsView(APIView):
    def get(self, request):
        products = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(products, many=True)
        content = {'category': serializer.data}
        return Response(content)


class CartView(APIView):
    def get(self, request):
        try:
            if request.GET.get('id'):
                if Cart.objects.filter(product_id=request.GET.get('id'), user=request.user).exists():
                    content={'message':'Product has been already added into cart'}
                else:
                    productt = Product.objects.get(id=request.GET.get('id'))
                    # cartserializer = CartSerializer(data={'product':productt.id, 'user':request.user.id})
                    cartserializer = CartsSerializer(data={'product':productt.id, 'user':request.user.id})
                    if cartserializer.is_valid():
                        cartserializer.save()
                        content={'message':'Product has been successfully added to you carts'}
                return Response(content)
            else:
                cart = Cart.objects.filter(user=request.user)
                return render(request, 'carts.html',{'cart':cart})
        except:
            content={'message':'There should be some issue in adding your product in cart'}
            return Response(content)    



class Lowtohigh(APIView):
    def get(self, request):
        products = Product.objects.order_by('price')
        serializer = ProductSerializer(products, many=True)
        content = {'category': serializer.data}
        return Response(content)

class HightoLow(APIView):
    def get(self, request):
        products = Product.objects.order_by('-price')
        serializer = ProductSerializer(products, many=True)
        content = {'category': serializer.data}
        return Response(content)

