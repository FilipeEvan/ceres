# Generated by Django 4.1 on 2022-09-04 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]