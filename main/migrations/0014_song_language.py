# Generated by Django 3.1.5 on 2021-08-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_execution_workfield3'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.CharField(default='', max_length=20),
        ),
    ]
