# Generated by Django 3.0.5 on 2020-06-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20200602_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='region',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sort',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
