# Generated by Django 4.2.6 on 2023-12-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBazaar', '0010_rename_images_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
