# Generated by Django 2.2 on 2019-07-16 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources_app', '0002_auto_20190716_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcemodel',
            name='approver_user',
        ),
        migrations.RemoveField(
            model_name='resourcemodel',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='resourcemodel',
            name='resource_state',
        ),
        migrations.DeleteModel(
            name='ResourceStateModel',
        ),
    ]