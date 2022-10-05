from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *

# Create your models here.

class Competencias(models.Model):
  ESTADO = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
  )
  descripcion = models.CharField(max_length = 200, null = True)
  estado = models.CharField(max_length = 200, null = True, choices = ESTADO)

  def __str__(self):
    return self.descripcion

class Idiomas(models.Model):
  ESTADO = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
  )
  nombre_idioma = models.CharField(max_length = 200, null = True)
  estado = models.CharField(max_length = 200, null = True, choices = ESTADO)

  def __str__(self):
    return self.nombre_idioma

class Capacitaciones(models.Model):
  NIVEL = (
    ('Grado', 'Grado'),
    ('Post-grado', 'Post-grado'),
    ('Maestria', 'Maestria'),
    ('Doctorado', 'Doctorado'),
    ('Tecnico', 'Tecnico'),
  )
  descripcion = models.CharField(max_length = 200, null = True)
  nivel = models.CharField(max_length = 200, null = True, choices = NIVEL)
  fecha_inicio = models.DateField(null = True)
  fecha_final = models.DateField(null = True)
  institucion = models.CharField(max_length = 200, null = True)

  def __str__(self):
    return self.descripcion

class Puestos(models.Model):
  NIVEL = (
    ('Alto', 'Alto'),
    ('Medio', 'Medio'),
    ('Bajo', 'Bajo'),
  )

  ESTADO = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
  )

  nombre_puesto = models.CharField(max_length = 200, null = True)
  nivel_riesgo = models.CharField(max_length = 200, null = True, choices = NIVEL)
  salario_minimo = models.FloatField(null = True)
  salario_maximo = models.FloatField(null = True)
  estado = models.CharField(max_length = 200, null = True, choices = ESTADO)

  def __str__(self):
    return self.nombre_puesto

class Experiencia_Laboral(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  empresa = models.CharField(max_length = 200, null = True)
  puesto_ocupado = models.CharField(max_length = 200, null = True)
  fecha_inicio = models.DateField(null = True)
  fecha_final = models.DateField(null = True)
  salario = models.FloatField(null = True)

  def __str__(self):
      return self.puesto_ocupado

class Candidatos(models.Model):

  cedula = models.CharField(max_length = 11, null = True)
  nombre_candidato = models.CharField(max_length = 200, null = True)
  puesto_aspiracion = models.ForeignKey(Puestos, on_delete = models.SET_NULL, null = True)
  departamento = models.CharField(max_length = 200, null = True)
  salario_aspiracion = models.FloatField(null = True)
  principales_competencias = models.ManyToManyField(Competencias)
  principales_capacitaciones = models.ManyToManyField(Capacitaciones)
  experiencia_laboral = models.ManyToManyField(Experiencia_Laboral)
  recomendacion = models.CharField(max_length = 200, null = True)

  def __str__(self):
      return self.nombre_candidato

class Empleados(models.Model):

  codigo_empleado = models.CharField(max_length = 11, null = True)
  candidato = models.ForeignKey(Candidatos, on_delete = models.SET_NULL, null = True)
  fecha_inicio = models.DateField(null = True)

  def __str__(self):
      return self.codigo_empleado
