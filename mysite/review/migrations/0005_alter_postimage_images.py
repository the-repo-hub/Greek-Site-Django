# Generated by Django 4.1.4 on 2023-01-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_postimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='review/images/False'),
        ),
    ]