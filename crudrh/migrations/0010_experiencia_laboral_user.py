# Generated by Django 4.1.1 on 2022-09-27 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudrh', '0009_alter_empleados_codigo_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencia_laboral',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]