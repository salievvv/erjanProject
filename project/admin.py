from django.contrib import admin
from .models import Product, Category, AboutPage, Kategorypage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(AboutPage)
admin.site.register(Kategorypage)