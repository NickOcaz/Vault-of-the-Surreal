# Generated by Django 4.2.17 on 2025-01-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image_url',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
