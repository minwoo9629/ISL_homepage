# Generated by Django 2.2.6 on 2020-08-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_auto_20200831_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoboard',
            name='year',
            field=models.IntegerField(),
        ),
    ]
