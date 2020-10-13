# Generated by Django 3.1.2 on 2020-10-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story1', '0003_course_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='academic_year',
            field=models.CharField(choices=[('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022')], default='2020/2021', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='room',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
