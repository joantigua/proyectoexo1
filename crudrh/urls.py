from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('competencias/', views.competencias),
    path('idiomas/', views.idiomas),
    path('capacitaciones/', views.capacitaciones),
    path('puestos/', views.puestos),
    path('experiencia_laboral/', views.experiencia_laboral),
    path('empleados/', views.empleados),
    path('candidatos/', views.candidatos),
    path('login/', views.loginPage),
    path('', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logoutUser),
    path('user/', views.logoutUser),
    path('create_candidatos/', views.createCandidatos),
    path('create_capacitaciones/', views.createCapacitaciones),
    path('create_idiomas/', views.createIdiomas),
    path('create_puestos/', views.createPuestos),
    path('create_competencias/', views.createCompetencias),
    path('create_experiencia_laboral/', views.createExperienciaLaboral),
    path('create_empleados/', views.createEmpleados),
    path('update_competencias/<int:id>/', views.updateCompetencias),
    path('update_candidatos/<int:id>/', views.updateCandidatos),
    path('update_capacitaciones/<int:id>/', views.updateCapacitaciones),
    path('update_idiomas/<int:id>/', views.updateIdiomas),
    path('update_puestos/<int:id>/', views.updatePuestos),
    path('update_experiencia_laboral/<int:id>/', views.updateExperienciaLaboral),
    path('update_empleados/<int:id>/', views.updateEmpleados),
    path('delete_competencias/<int:id>/', views.deleteCompetencias),
    path('delete_candidatos/<int:id>/', views.deleteCandidatos),
    path('delete_capacitaciones/<int:id>/', views.deleteCapacitaciones),
    path('delete_idiomas/<int:id>/', views.deleteIdiomas),
    path('delete_puestos/<int:id>/', views.deletePuestos),
    path('delete_experiencia_laboral/<int:id>/', views.deleteExperienciaLaboral),
    path('delete_empleados/<int:id>/', views.deleteEmpleados),

    path('search_candidatos/', views.searchCandidatos),
    path('view_candidatos/<int:id>/', views.viewCandidatos),
    path('view_capacitaciones/<int:id>/', views.viewCapacitaciones),
    path('view_idiomas/<int:id>/', views.viewIdiomas),
    path('view_puestos/<int:id>/', views.viewPuestos),
    path('view_experiencia_laboral/<int:id>/', views.viewExperienciaLaboral),
    path('view_empleados/<int:id>/', views.viewEmpleados),
    path('view_competencias/<int:id>/', views.viewCompetencias),
    

]
