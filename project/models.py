from django.db import models 
from django.urls import reverse
from ckeditor.fields import RichTextField

class Marka(models.Model):
    name = models.CharField(max_length=120,verbose_name='название марки') 
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("marka_detail", kwargs={"slug": self.url})

    def __str__(self) -> str:
        return self.name

class Year(models.Model):
    year = models.PositiveSmallIntegerField(verbose_name='год выпуска') 
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("year_detail", kwargs={"slug": self.url})

    def __str__(self) -> str:
        return self.year

class Product(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE,null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL,null=True)
    name = models.CharField(verbose_name='название', max_length=70)
    img = models.ImageField(upload_to='product/',verbose_name='фотки', blank=True, null=True)
    desc = models.TextField(verbose_name='описание', blank=True, null=True)
    price = models.FloatField(verbose_name='цена') # doolar 
    modelavto = models.TextField(verbose_name='модель',blank=True, null=True)
    godvypuska = models.FloatField(verbose_name='год выпуска',blank=True, null=True)
    dvigatel = models.FloatField(verbose_name='объем двигаетля',blank=True, null=True)
    price = models.FloatField(verbose_name='цена в $',blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class AboutPage(models.Model):
    title = models.CharField(verbose_name='О компании', max_length=30)
    img = models.ImageField(upload_to='about/',verbose_name='фотки')
    desc = RichTextField()

    def __str__(self) -> str:
        return self.title
    

class Gallery(models.Model):
    pageAbout = models.ForeignKey(AboutPage, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery/')

    def __str__(self) -> str:
        return f'{self.id}'
