# Generated by Django 5.0.1 on 2024-01-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_aboutpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='фотки'),
        ),
    ]
