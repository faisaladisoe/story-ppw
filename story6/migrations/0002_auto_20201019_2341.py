# Generated by Django 3.1.2 on 2020-10-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='complete_description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
