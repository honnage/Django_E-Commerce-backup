# Generated by Django 3.1.6 on 2021-05-02 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cartItem',
        ),
    ]