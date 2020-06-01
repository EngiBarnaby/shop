# Generated by Django 3.0.5 on 2020-06-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_shopadress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress_choice',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]