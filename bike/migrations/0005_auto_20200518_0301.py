# Generated by Django 2.2.6 on 2020-05-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_auto_20200517_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_detail',
            name='price',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]