from django.contrib import admin

from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)

# Tp personalice the Admin 
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name', 
        'last_name', 
        'job',
        'departamento',
        'full_name'
        )
    def full_name(self, obj):
        # print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name', 'last_name') # BUSCADOR - ingresar valores
    list_filter = ('departamento','job', 'habilidades') # Shows a list for filtering
    filter_horizontal = ('habilidades', ) ## Only for many to many

admin.site.register(Empleado, EmpleadoAdmin)