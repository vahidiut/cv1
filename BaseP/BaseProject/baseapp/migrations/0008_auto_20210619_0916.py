# Generated by Django 3.1.3 on 2021-06-19 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0007_properties_evaluated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='evaluated',
            new_name='amended',
        ),
    ]
