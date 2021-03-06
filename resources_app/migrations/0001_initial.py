# Generated by Django 2.2 on 2019-06-09 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type_description', models.CharField(max_length=100, verbose_name='Typ paliwa')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceStateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_description', models.CharField(max_length=50, verbose_name='Stan zasobu')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Czy zatwierdzone')),
                ('is_available', models.BooleanField(default=True, verbose_name='Czy dostępny')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='Nazwa zasobu')),
                ('start_date', models.DateField(blank=True, default=None, null=True, verbose_name='Data przydzielenia')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Data zakończenia')),
                ('production_year', models.DateField(blank=True, default=None, null=True, verbose_name='Data produkcji')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='resources/', verbose_name='Zdjęcie')),
                ('brand', models.CharField(default=None, max_length=200, verbose_name='Marka zasobu')),
                ('model', models.CharField(default=None, max_length=200, verbose_name='Model zasobu')),
                ('info', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Dodatkowe informacje')),
                ('approver_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Osoba zatwierdzająca')),
                ('resource_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_state', to='resources_app.ResourceStateModel', verbose_name='Stan zasobu')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Data rozpoczęcia')),
                ('end_date', models.DateField(verbose_name='Data zakończenia')),
                ('approver_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_history_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Osoba zatwierdzająca')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='resources_app.ResourceModel', verbose_name='Zasób')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_history_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_card_number', models.IntegerField(verbose_name='Numer karty paliwa')),
                ('registration_number', models.CharField(max_length=30, verbose_name='Numer rejestracyjny')),
                ('car_meter_status', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Stan licznika')),
                ('fuel_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auto_fuel_type', to='resources_app.FuelType', verbose_name='Rodzaj paliwa')),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_auto', to='resources_app.ResourceModel', verbose_name='Pracownik')),
            ],
        ),
    ]
