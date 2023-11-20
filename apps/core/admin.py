from django.contrib import admin
from .models import (
    Pais,
    Provincia,
    Ciudad,
    Direccion,
    TipoHabitacion,
    Servicio,
    Categoria,
    Vendedor,
    Encargado,
    Cliente,
)


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "documento", "tipo_documento")

    def apellido(self, obj):
        return obj.apellido

    def nombre(self, obj):
        return obj.nombre

    def documento(self, obj):
        return obj.documento

    def tipo_documento(self, obj):
        return obj.tipo_documento


admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Direccion)
admin.site.register(TipoHabitacion)
admin.site.register(Servicio)
admin.site.register(Categoria)
admin.site.register(Vendedor, PersonaAdmin)
admin.site.register(Encargado, PersonaAdmin)
admin.site.register(Cliente)
