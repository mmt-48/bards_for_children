# Generated by Django 3.1.5 on 2021-05-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_song_workfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='workfield',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]