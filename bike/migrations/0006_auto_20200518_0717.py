# Generated by Django 2.2.6 on 2020-05-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_auto_20200518_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_feedback',
            name='message1',
            field=models.TextField(null=True),
        ),
    ]
