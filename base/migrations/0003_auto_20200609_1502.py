# Generated by Django 3.0.5 on 2020-06-09 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200609_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='plan_type',
            new_name='type',
        ),
    ]