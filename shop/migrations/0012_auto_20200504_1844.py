# Generated by Django 3.0.5 on 2020-05-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valueandprices',
            old_name='price',
            new_name='another_price',
        ),
    ]
