# Generated by Django 3.0.5 on 2020-06-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20200531_2119'),
    ]

    operations = [
        migrations.AddField(
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