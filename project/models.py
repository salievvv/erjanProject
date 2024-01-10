from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name='название', max_length=30)
    desc = models.TextField(verbose_name='описание')
    price = models.FloatField(verbose_name='цена', max_length=10)

    def __str__(self) -> str:
        return self.name

