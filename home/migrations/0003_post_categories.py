# Generated by Django 4.1.6 on 2023-04-07 16:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remotetoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), blank=True, null=True, size=None),
        ),
    ]
