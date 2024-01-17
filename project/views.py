from django.shortcuts import render
from .models import Product, AboutPage, Kategorypage

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def about(request):
    aboutpage = AboutPage.objects.latest('id')
    context = {'aboutpage':aboutpage}
    return render(request,'about.html', context)


def kategory(request):
    kategorypage = Kategorypage.objects.latest('id')
    context = {'kategorypage':kategorypage}
    return render(request,'kategory.html', context)