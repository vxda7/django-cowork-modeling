# Generated by Django 2.2.4 on 2019-11-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191120_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_genres',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='movies.Genre'),
        ),
    ]
