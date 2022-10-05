from importlib import resources
from pyexpat import model
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter
from import_export import resources
from import_export.fields import Field

class EmpleadosResource(resources.ModelResource):
    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'candidato__nombre_candidato':
                headers[i] = "Nombre del candidato"
            if h == 'codigo_empleado':
                headers[i] = "Codigo del empleado"
            if h == 'id':
                headers[i] = "Id"
            if h == 'fecha_inicio':
                headers[i] = "Fecha de inicio"
        return headers

    class Meta:
        model = Empleados
        fields = ('id', 'candidato__nombre_candidato','codigo_empleado', 'fecha_inicio')


class EmpleadosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmpleadosResource
    list_filter = ('fecha_inicio',)

#Change the file path according to your project

# Register your models here.

admin.site.register(Competencias)
admin.site.register(Idiomas)
admin.site.register(Capacitaciones)
admin.site.register(Puestos)
admin.site.register(Experiencia_Laboral)
admin.site.register(Candidatos)
admin.site.register(Empleados, EmpleadosAdmin)


