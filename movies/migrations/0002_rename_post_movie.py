# Generated by Django 4.2.17 on 2025-01-12 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Movie',
        ),
    ]
