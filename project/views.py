from django.shortcuts import render
from .models import Product
from .models import ProAbout

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def about(request):
    return render(request,'proabout/about.html')
