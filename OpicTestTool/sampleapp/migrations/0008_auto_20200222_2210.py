# Generated by Django 3.0.2 on 2020-02-22 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0007_auto_20200222_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(
                2020, 2, 22, 13, 10, 57, 149186, tzinfo=utc)),
        ),
    ]
