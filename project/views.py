from django.shortcuts import render
from .models import Product, AboutPage

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def about(request):
    aboutpage = AboutPage.objects.latest('id')
    context = {'aboutpage':aboutpage}
    return render(request,'about.html', context)
