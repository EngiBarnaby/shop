# Generated by Django 3.0.5 on 2020-05-31 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200531_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
    ]
