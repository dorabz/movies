# Generated by Django 4.1.4 on 2022-12-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_movie_imdb_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
