# Generated by Django 4.2.17 on 2025-01-12 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_movie_add_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_Movie',
            new_name='Movie',
        ),
    ]