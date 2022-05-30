# Generated by Django 3.1.5 on 2022-04-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0004_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='images/posts/{}cover'),
        ),
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='images/cover'),
        ),
    ]