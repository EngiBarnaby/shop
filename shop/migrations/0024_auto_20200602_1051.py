# Generated by Django 3.0.5 on 2020-06-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20200602_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(related_name='subcategories', to='shop.Subcategory'),
        ),
    ]
