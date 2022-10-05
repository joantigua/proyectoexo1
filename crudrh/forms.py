
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def validar_cedula(value):

    # La cédula debe tener 11 dígitos
        value = value.replace('-','')
        if len(value)== 11:
            if (int(value[0:3]) < 122 and int(value[0:3]) > 0 or int(value[0:3]) == 402):
                suma = 0
                mutliplicador = 1
                verificador = 0

                # Los dígitos pares valen 2 y los impares 1
                mutliplicador = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
                for i in range(10):

                    # Se multiplica cada dígito por su paridad
                    digito = int(value[i])*mutliplicador[i]

                    # Si la multiplicación da de dos dígitos, se suman entre sí
                    if(digito>9):
                        digito = digito//10 + digito%10

                    # Y se va haciendo la acumulación de esa suma
                    suma = suma + digito

                # Al final se obtiene el verificador con la siguiente fórmula
                verificador = (10 - (suma % 10) ) % 10

                # Se comprueba que coincidan
                if(verificador == int(value[10]) ):
                    return True
                # El dígito verificador no es válido
                else:
                    raise forms.ValidationError("La cedula es invalida")
            # La serie no es válida
            else:
                raise forms.ValidationError("La cedula es invalida")
        # No tiene 11 dígitos
        else:
            raise forms.ValidationError("La cedula es invalida")


class CandidatosForm(ModelForm):
    
    class Meta:
      model = Candidatos
      fields = '__all__'

    experiencia_laboral = forms.ModelMultipleChoiceField (
            queryset = Experiencia_Laboral.objects.all(),
            widget = forms.CheckboxSelectMultiple,
        )
    principales_capacitaciones = forms.ModelMultipleChoiceField (
            queryset = Capacitaciones.objects.all(), 
            widget = forms.CheckboxSelectMultiple,
        )
    principales_competencias = forms.ModelMultipleChoiceField (
            queryset = Competencias.objects.all(), 
            widget = forms.CheckboxSelectMultiple,
        )
    cedula = forms.CharField(validators = [validar_cedula])

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('experiencia_laboral').count() > 3:
            raise ValidationError('No puede seleccionar mas de tres opciones!')
    
    



class EmpleadosForm(ModelForm):
    class Meta:
      model = Empleados
      fields = '__all__'

class CompetenciasForm(ModelForm):
    class Meta:
      model = Competencias
      fields = '__all__'

class IdiomasForm(ModelForm):
    class Meta:
      model = Idiomas
      fields = '__all__'

class CapacitacionesForm(ModelForm):
    class Meta:
      model = Capacitaciones
      fields = '__all__'

class PuestosForm(ModelForm):
    class Meta:
      model = Puestos
      fields = '__all__'

class Experiencia_LaboralForm(ModelForm):
    class Meta:
      model = Experiencia_Laboral
      fields = '__all__'
     
    



class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']