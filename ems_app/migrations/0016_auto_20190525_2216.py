# Generated by Django 2.2 on 2019-05-25 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0015_auto_20190525_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entranceexitmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_exit_project', to='ems_app.ProjectModel', verbose_name='Projekt'),
        ),
    ]