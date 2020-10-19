# Generated by Django 3.1.2 on 2020-10-19 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story6', '0002_auto_20201019_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='visitor_age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(17), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
