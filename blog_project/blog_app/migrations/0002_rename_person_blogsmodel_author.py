# Generated by Django 3.2.5 on 2022-05-30 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogsmodel',
            old_name='person',
            new_name='author',
        ),
    ]