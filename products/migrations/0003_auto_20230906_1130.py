# Generated by Django 3.2.20 on 2023-09-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_motor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='battery',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='speed',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
