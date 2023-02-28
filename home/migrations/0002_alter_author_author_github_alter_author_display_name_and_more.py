# Generated by Django 4.1.6 on 2023-02-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_github',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='display_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='home_host',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_image',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_url',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='uid',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.URLField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_id',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='comments',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following_summary',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='like',
            name='context',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_summary',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='like',
            name='obj',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='like',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='liked',
            name='context',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='object_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_origin',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_source',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(default='FRIENDS', max_length=20),
        ),
    ]