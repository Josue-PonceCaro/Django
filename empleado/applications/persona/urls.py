from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app' # a name for this aplication

urlpatterns = [
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name = 'empleados_all', 
        ),
    # path('listar-por-departamento/', views.ListByArea.as_view()),
    path('listar-por-departamento/<shorname>/', views.ListByArea.as_view()),
    path('listar-por-nombre/',views.ListByName.as_view()),
    path('listar-por-habilidades/', views.ListByHabilidades.as_view()),
    path(
        'detalle-del-empleado/<int:pk>', 
        views.EmpleadoDetailView.as_view(),
        name = 'detalle_empleado'
        ),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name = 'all_ok'),
    path('update/<int:pk>', views.EmpleadoUpdateView.as_view()),
    path('delete/<int:pk>', views.EmpleadoDeleteView.as_view()),
    path('', views.HomeView.as_view(), name = 'home'),
]
