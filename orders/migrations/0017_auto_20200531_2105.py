# Generated by Django 3.0.5 on 2020-05-31 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20200531_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress_choice',
            field=models.TextField(null=True),
        ),
    ]
