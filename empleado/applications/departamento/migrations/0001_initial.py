# Generated by Django 4.0.1 on 2022-01-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=50, verbose_name='Nombre Corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
