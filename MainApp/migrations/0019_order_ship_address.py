# Generated by Django 3.2.14 on 2022-09-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_remove_cart_foot_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ship_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
