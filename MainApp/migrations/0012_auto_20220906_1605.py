# Generated by Django 3.2.14 on 2022-09-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_order_quantity_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shoe_size',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='order',
            name='shoe_size',
            field=models.IntegerField(default=42),
        ),
    ]
