# Generated by Django 4.0.1 on 2022-02-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_alter_habilidades_options_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Administrador de empleados'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre Completos'),
        ),
    ]
