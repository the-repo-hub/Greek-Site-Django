# Generated by Django 4.1.4 on 2023-01-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_remove_postimage_post_delete_post_delete_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Сайдбар страница',
                'verbose_name_plural': 'Сайдбар страницы',
            },
        ),
    ]
