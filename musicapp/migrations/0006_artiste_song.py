# Generated by Django 4.1.2 on 2022-11-04 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_remove_song_artiste_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='song',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
    ]
