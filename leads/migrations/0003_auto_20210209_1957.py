# Generated by Django 3.0.5 on 2021-02-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210207_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=True),
        ),
    ]