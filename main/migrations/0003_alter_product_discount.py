# Generated by Django 4.0.4 on 2022-06-23 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_rating_alter_product_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
