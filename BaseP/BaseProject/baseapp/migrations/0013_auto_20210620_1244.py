# Generated by Django 3.1.3 on 2021-06-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0012_auto_20210620_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_point',
            new_name='user_score',
        ),
        migrations.RenameField(
            model_name='properties',
            old_name='amended',
            new_name='amendment_condition',
        ),
        migrations.AddField(
            model_name='subtasks1',
            name='amendment_condition',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tasks',
            name='amendment_condition',
            field=models.BooleanField(default=False),
        ),
    ]
