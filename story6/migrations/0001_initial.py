# Generated by Django 3.1.2 on 2020-10-19 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=75, null=True)),
                ('visitor_age', models.PositiveIntegerField(null=True)),
                ('id_type', models.CharField(choices=[('KTM', 'KTM'), ('KTP', 'KTP'), ('SIM', 'SIM'), ('Passport', 'Passport')], default='KTM', max_length=10, null=True)),
                ('identity_number', models.CharField(max_length=75, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story6.event')),
            ],
        ),
    ]
