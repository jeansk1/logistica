from django.contrib import admin
from .models import (
    Ruta, Vehiculo, Aeronave,
    Conductor, Piloto,
    Cliente, Carga,
    Despacho
)

# ==========================================================
# CONFIGURACIONES DEL ADMIN
# ==========================================================

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'tipo_transporte', 'distancia_km')
    search_fields = ('origen', 'destino', 'tipo_transporte')
    list_filter = ('tipo_transporte',)


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'patente', 'tipo_vehiculo', 'capacidad_kg', 'activo')
    search_fields = ('patente', 'tipo_vehiculo')
    list_filter = ('activo',)


@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'tipo_aeronave', 'capacidad_kg', 'activo')
    search_fields = ('matricula', 'tipo_aeronave')
    list_filter = ('activo',)


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'licencia', 'activo')
    search_fields = ('nombre', 'rut')
    list_filter = ('activo',)


@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'certificacion', 'activo')
    search_fields = ('nombre', 'rut')
    list_filter = ('activo',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut', 'telefono', 'direccion')
    search_fields = ('nombre', 'rut', 'direccion')


@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'peso_kg', 'tipo_mercancia', 'valor_estimado', 'cliente')
    search_fields = ('descripcion', 'tipo_mercancia')
    list_filter = ('tipo_mercancia', 'cliente')


# ==========================================================
# DESPACHO (Vista Profesional)
# ==========================================================

@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_despacho',
        'estado',
        'ruta',
        'vehiculo',
        'aeronave',
        'conductor',
        'piloto',
        'costo_envio',
    )
    search_fields = (
        'estado',
        'ruta__origen',
        'ruta__destino',
        'vehiculo__patente',
        'aeronave__matricula',
        'conductor__nombre',
        'piloto__nombre'
    )
    list_filter = ('estado', 'ruta__tipo_transporte')

