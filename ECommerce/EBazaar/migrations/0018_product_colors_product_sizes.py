# Generated by Django 4.2.6 on 2023-12-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBazaar', '0017_remove_product_colors_remove_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]