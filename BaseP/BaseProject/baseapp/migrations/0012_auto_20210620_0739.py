# Generated by Django 3.1.3 on 2021-06-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0011_auto_20210620_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtasks1',
            name='number_of_submitted_experiences',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subtasks1',
            name='number_of_verified_experiences',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
