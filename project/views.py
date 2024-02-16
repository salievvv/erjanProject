from django.shortcuts import render
from .models import Product, AboutPage, Gallery

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def about(request):
    aboutpage = AboutPage.objects.latest('id')
    galleries = Gallery.objects.all()
    context = {
        'aboutpage':aboutpage,
        'galleries':galleries,
    }
    return render(request,'about.html', context)
