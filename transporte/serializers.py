from rest_framework import serializers
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)

# ==========================================================
# SERIALIZERS BÁSICOS
# ==========================================================

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'


class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class CargaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = Carga
        fields = '__all__'

# ==========================================================
# SERIALIZERS AVANZADOS — DESPACHO
# ==========================================================

# --- Serializers anidados para mostrar detalles completos ---
class DespachoDetailSerializer(serializers.ModelSerializer):
    ruta = RutaSerializer(read_only=True)
    vehiculo = VehiculoSerializer(read_only=True)
    aeronave = AeronaveSerializer(read_only=True)
    conductor = ConductorSerializer(read_only=True)
    piloto = PilotoSerializer(read_only=True)
    carga = CargaSerializer(read_only=True)

    class Meta:
        model = Despacho
        fields = '__all__'


# --- Serializer para creación/edición (recibe solo IDs) ---
class DespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despacho
        fields = '__all__'

    # Validación adicional (opcional, la principal está en el modelo)
    def validate(self, data):
        ruta = data.get('ruta')
        vehiculo = data.get('vehiculo')
        conductor = data.get('conductor')
        aeronave = data.get('aeronave')
        piloto = data.get('piloto')

        # Reglas igual que en clean() del modelo
        if ruta.tipo_transporte == "TERRESTRE":
            if not vehiculo or not conductor:
                raise serializers.ValidationError("Debe asignar vehículo y conductor.")
            if aeronave or piloto:
                raise serializers.ValidationError("No debe asignar aeronave ni piloto en transporte terrestre.")

        if ruta.tipo_transporte == "AEREO":
            if not aeronave or not piloto:
                raise serializers.ValidationError("Debe asignar aeronave y piloto.")
            if vehiculo or conductor:
                raise serializers.ValidationError("No debe asignar vehículo ni conductor en transporte aéreo.")

        return data
