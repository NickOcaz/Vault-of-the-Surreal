# Generated by Django 4.2.17 on 2025-01-15 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_movie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
