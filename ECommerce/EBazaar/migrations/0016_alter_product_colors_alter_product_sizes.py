# Generated by Django 4.2.6 on 2023-12-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBazaar', '0015_alter_product_colors_alter_product_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
