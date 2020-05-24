# Generated by Django 3.0.5 on 2020-05-23 21:29

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200521_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='verification',
            field=models.CharField(max_length=20),
        ),
    ]
