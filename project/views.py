from django.shortcuts import render
from .models import Product, AboutPage, Gallery, Otzyvy

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def otzyvy(request):
    otz = Otzyvy.objects.latest('id')
    context = {'otz':otz}
    return render(request,'otzyvy.html',context)
    

def about(request):
    aboutpage = AboutPage.objects.latest('id')
    galleries = Gallery.objects.all()
    context = {
        'aboutpage':aboutpage,
        'galleries':galleries,
    }
    return render(request,'about.html', context)
