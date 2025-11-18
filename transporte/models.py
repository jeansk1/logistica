from django.db import models
from django.core.exceptions import ValidationError

# ==========================================================
# CHOICES GLOBALES
# ==========================================================

TIPO_TRANSPORTE_CHOICES = [
    ('TERRESTRE', 'Terrestre'),
    ('AEREO', 'Aéreo'),
]

ESTADO_DESPACHO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('EN RUTA', 'En Ruta'),
    ('ENTREGADO', 'Entregado'),
]

# ==========================================================
# MODELOS BASE DEL SISTEMA DE LOGÍSTICA
# ==========================================================

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tipo_transporte = models.CharField(
        max_length=15,
        choices=TIPO_TRANSPORTE_CHOICES,
        default='TERRESTRE'
    )
    distancia_km = models.FloatField()

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.tipo_transporte})"


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=10, unique=True)
    tipo_vehiculo = models.CharField(max_length=50)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patente} - {self.tipo_vehiculo}"


class Aeronave(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=15, unique=True)
    tipo_aeronave = models.CharField(max_length=50)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} - {self.tipo_aeronave}"


class Conductor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    licencia = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.licencia})"


class Piloto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    certificacion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.certificacion})"

# ==========================================================
# MODELOS ADICIONALES (REQUISITO DE MEJORA DEL MODELO)
# ==========================================================

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Carga(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    peso_kg = models.FloatField()
    tipo_mercancia = models.CharField(max_length=50)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cargas')

    def __str__(self):
        return f"Carga {self.id}: {self.descripcion} - {self.peso_kg} kg"

# ==========================================================
# MODELO PRINCIPAL (DESPACHO)
# ==========================================================

class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_despacho = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_DESPACHO_CHOICES,
        default='PENDIENTE'
    )
    costo_envio = models.FloatField()

    # Relación principal
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name='despachos')

    # Terrestre
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.PROTECT,
        related_name='despachos',
        null=True, blank=True
    )
    conductor = models.ForeignKey(
        Conductor,
        on_delete=models.PROTECT,
        related_name='despachos',
        null=True, blank=True
    )

    # Aéreo
    aeronave = models.ForeignKey(
        Aeronave,
        on_delete=models.PROTECT,
        related_name='despachos',
        null=True, blank=True
    )
    piloto = models.ForeignKey(
        Piloto,
        on_delete=models.PROTECT,
        related_name='despachos',
        null=True, blank=True
    )

    # Carga asociada (1:1)
    carga = models.OneToOneField(
        Carga,
        on_delete=models.PROTECT,
        related_name='despacho',
        null=True, blank=True
    )

    # -----------------------------------------------
    # VALIDACIONES DE CONSISTENCIA DE NEGOCIO
    # -----------------------------------------------
    def clean(self):
        # Reglas para despacho TERRESTRE
        if self.ruta.tipo_transporte == "TERRESTRE":
            if not self.vehiculo or not self.conductor:
                raise ValidationError("Un despacho terrestre requiere un vehículo y un conductor.")
            if self.aeronave or self.piloto:
                raise ValidationError("Un despacho terrestre no debe tener aeronave ni piloto.")

        # Reglas para despacho AÉREO
        if self.ruta.tipo_transporte == "AEREO":
            if not self.aeronave or not self.piloto:
                raise ValidationError("Un despacho aéreo requiere aeronave y piloto.")
            if self.vehiculo or self.conductor:
                raise ValidationError("Un despacho aéreo no debe tener vehículo ni conductor.")

    def __str__(self):
        return f"Despacho {self.id} | {self.estado} | {self.ruta.origen} → {self.ruta.destino}"
