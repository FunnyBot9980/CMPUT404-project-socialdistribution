# Generated by Django 4.1.6 on 2023-02-12 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='type',
            new_name='object_type',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='id',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='authors',
            old_name='type',
            new_name='object_type',
        ),
    ]