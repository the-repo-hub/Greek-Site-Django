# Generated by Django 4.1.4 on 2023-01-19 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_postimage_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]