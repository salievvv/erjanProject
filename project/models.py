from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='название категории')
    slug = AutoSlugField(populate_from='name', unique=True)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(verbose_name='название', max_length=30)
    img = models.ImageField(upload_to='product ',verbose_name='фотки')
    desc = models.TextField(verbose_name='описание')
    price = models.FloatField(verbose_name='цена')

    def __str__(self) -> str:
        return self.name

