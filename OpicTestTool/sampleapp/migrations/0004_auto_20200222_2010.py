# Generated by Django 3.0.2 on 2020-02-22 11:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_auto_20200203_2247'),
    ]

    operations = [
        migrations.DeleteModel(
            name='addinput',
        ),
        migrations.DeleteModel(
            name='SelectQuestion',
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='frequency',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 2, 22, 11, 10, 40, 62815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='sample_answer',
            field=models.TextField(blank=True),
        ),
    ]
