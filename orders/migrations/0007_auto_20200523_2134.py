# Generated by Django 3.0.5 on 2020-05-23 21:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200523_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 05999999999', regex='^(05)\\d{9}$')]),
        ),
    ]
