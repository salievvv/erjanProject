from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='название категории')
    slug = AutoSlugField(populate_from='name', unique=True)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(verbose_name='название', max_length=30)
    img = models.ImageField(upload_to='product/',verbose_name='фотки', blank=True, null=True)
    desc = models.TextField(verbose_name='описание', blank=True, null=True)
    price = models.FloatField(verbose_name='цена') # doolar

    def __str__(self) -> str:
        return self.name

class AboutPage(models.Model):
    title = models.CharField(verbose_name='О компании', max_length=30)
    img = models.ImageField(upload_to='about/',verbose_name='фотки')
    desc = models.TextField(verbose_name='описание')

    def __str__(self) -> str:
        return self.title

class Kategorypage(models.Model):
    marc = models.CharField(verbose_name='марка авто', max_length=30,blank=True, null=True)
    img = models.ImageField(upload_to='kategory/',verbose_name='изображение',blank=True, null=True )
    modelavto = models.TextField(verbose_name='модель',blank=True, null=True)
    godvypuska = models.FloatField(verbose_name='год выпуска',blank=True, null=True)
    dvigatel = models.FloatField(verbose_name='объем двигаетля',blank=True, null=True)
    price = models.FloatField(verbose_name='цена в $',blank=True, null=True)


    def __str__(self) -> str:
        return self.marc