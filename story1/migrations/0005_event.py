# Generated by Django 3.1.2 on 2020-10-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story1', '0004_auto_20201013_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50, null=True)),
                ('brief_description', models.CharField(max_length=200, null=True)),
                ('complete_description', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
