# Generated by Django 4.1.1 on 2022-09-30 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudrh', '0013_rename_fecha_inicio_empleados_fecha_iniciod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleados',
            old_name='fecha_iniciod',
            new_name='fecha_inicio',
        ),
    ]
