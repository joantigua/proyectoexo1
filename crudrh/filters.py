from dataclasses import fields
import django_filters 
from .models import *
from django_filters import *


class CandidatosFilter(django_filters.FilterSet):
    class Meta:
        model = Candidatos
        fields = ['cedula', 'nombre_candidato', 'puesto_aspiracion']

class EmpleadosFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "fecha_inicio", lookup_expr = 'gte')
    end_date = DateFilter(field_name = "fecha_inicio", lookup_expr = 'lte')
    class Meta:
        model = Empleados
        fields = '__all__'
        exclude = ['fecha_inicio', 'codigo_empleado', 'candidato']


        
    
