from django import forms
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)


# ===========================================================
#  WIDGETS Bootstrap (para hacer los formularios profesionales)
# ===========================================================

class BootstrapFormMixin:
    """Agrega clases Bootstrap a todos los campos automáticamente."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


# ===========================================================
#  FORMULARIOS POR ENTIDAD
# ===========================================================

class RutaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'tipo_transporte', 'distancia_km']


class VehiculoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'tipo_vehiculo', 'capacidad_kg', 'activo']


class AeronaveForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Aeronave
        fields = ['matricula', 'tipo_aeronave', 'capacidad_kg', 'activo']


class ConductorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'rut', 'licencia', 'activo']


class PilotoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'rut', 'certificacion', 'activo']


class ClienteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut', 'telefono', 'direccion']


class CargaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Carga
        fields = [
            'descripcion', 'peso_kg', 'tipo_mercancia',
            'valor_estimado', 'cliente'
        ]


class DespachoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Despacho
        fields = [
            'fecha_despacho',
            'estado',
            'costo_envio',
            'ruta',
            'vehiculo',
            'aeronave',
            'conductor',
            'piloto',
            'carga',
        ]

        widgets = {
            'fecha_despacho': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
