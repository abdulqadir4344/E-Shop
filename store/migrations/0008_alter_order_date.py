# Generated by Django 4.2.4 on 2023-08-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_address_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.BooleanField(default=False),
        ),
    ]