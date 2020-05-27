# Generated by Django 3.0.6 on 2020-05-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmovies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]