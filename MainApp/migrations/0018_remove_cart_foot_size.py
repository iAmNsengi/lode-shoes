# Generated by Django 3.2.14 on 2022-09-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_cart_foot_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='foot_size',
        ),
    ]
