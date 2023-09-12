# Generated by Django 3.2.20 on 2023-09-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230912_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tires',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brake',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='frame',
            field=models.TextField(blank=True, null=True),
        ),
    ]