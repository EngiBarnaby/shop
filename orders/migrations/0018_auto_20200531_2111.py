# Generated by Django 3.0.5 on 2020-05-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20200531_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress_choice',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
