# Generated by Django 3.0.5 on 2020-05-31 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20200531_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
