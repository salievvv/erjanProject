# Generated by Django 4.2.9 on 2024-02-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_aboutpage_options_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otzyvy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Отзывы на страничку')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='написать')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='title',
            field=models.CharField(max_length=130, verbose_name='О компании'),
        ),
    ]
