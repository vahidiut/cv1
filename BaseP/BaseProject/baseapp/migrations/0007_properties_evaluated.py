# Generated by Django 3.1.3 on 2021-06-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_subtasks1_number_of_related_experiences'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='evaluated',
            field=models.BooleanField(default=False),
        ),
    ]
