# Generated by Django 3.1.2 on 2020-10-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story1', '0002_auto_20201013_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
