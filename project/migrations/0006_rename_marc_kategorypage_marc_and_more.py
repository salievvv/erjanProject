# Generated by Django 5.0.1 on 2024-01-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_kategorypage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategorypage',
            old_name='Marc',
            new_name='marc',
        ),
        migrations.RemoveField(
            model_name='kategorypage',
            name='dvigatel',
        ),
        migrations.RemoveField(
            model_name='kategorypage',
            name='godvypuska',
        ),
        migrations.RemoveField(
            model_name='kategorypage',
            name='price',
        ),
    ]