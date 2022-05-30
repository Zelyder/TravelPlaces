# Generated by Django 3.1.5 on 2022-05-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0009_page_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='short_description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]