# Generated by Django 3.0.2 on 2020-03-08 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0010_auto_20200307_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 3, 8, 13, 9, 17, 732362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
    ]
