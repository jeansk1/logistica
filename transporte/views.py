# transporte/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# MODELOS Y FORMULARIOS
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)

from .forms import (
    RutaForm, VehiculoForm, AeronaveForm, ConductorForm, PilotoForm,
    ClienteForm, CargaForm, DespachoForm
)

# DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    RutaSerializer, VehiculoSerializer, AeronaveSerializer,
    ConductorSerializer, PilotoSerializer, ClienteSerializer,
    CargaSerializer, DespachoSerializer
)

# ===========================================================
#      API REST - VIEWSETS (PARA SWAGGER Y MOBILE)
# ===========================================================

class RutaViewSet(ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

class AeronaveViewSet(ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    permission_classes = [IsAuthenticated]

class ConductorViewSet(ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permission_classes = [IsAuthenticated]

class PilotoViewSet(ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class CargaViewSet(ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [IsAuthenticated]

class DespachoViewSet(ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    permission_classes = [IsAuthenticated]

# ===========================================================
#              CRUD - VISTAS HTML (PROTEGIDAS)
# ===========================================================

# -----------------------------
#           RUTAS
# -----------------------------
def rutas_listado(request):
    query = request.GET.get('q')
    if query:
        rutas = Ruta.objects.filter(
            Q(origen__icontains=query) | 
            Q(destino__icontains=query) |
            Q(tipo_transporte__icontains=query)
        )
    else:
        rutas = Ruta.objects.all()
    return render(request, "transporte/rutas/listado_rutas.html", {"rutas": rutas})

def ruta_detalle(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    return render(request, "transporte/rutas/detalle_ruta.html", {"ruta": ruta})

@login_required
def ruta_crear(request):
    if request.method == "POST":
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ruta creada correctamente.")
            return redirect("transporte:rutas_listado")
    else:
        form = RutaForm()
    return render(request, "transporte/rutas/form_ruta.html", {"form": form})

@login_required
def ruta_editar(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == "POST":
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, "Ruta actualizada correctamente.")
            return redirect("transporte:rutas_listado")
    else:
        form = RutaForm(instance=ruta)
    return render(request, "transporte/rutas/form_ruta.html", {"form": form})

@login_required
def ruta_eliminar(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    ruta.delete()
    messages.success(request, "Ruta eliminada correctamente.")
    return redirect("transporte:rutas_listado")

# -----------------------------
#           VEHÍCULOS
# -----------------------------
def vehiculos_listado(request):
    query = request.GET.get('q')
    if query:
        vehiculos = Vehiculo.objects.filter(
            Q(patente__icontains=query) | 
            Q(tipo_vehiculo__icontains=query)
        )
    else:
        vehiculos = Vehiculo.objects.all()
    
    context = {
        'vehiculos': vehiculos,
        'vehiculos_activos': vehiculos.filter(activo=True).count(),
        'vehiculos_inactivos': vehiculos.filter(activo=False).count(),
    }
    return render(request, "transporte/vehiculos/listado_vehiculos.html", context)

def vehiculo_detalle(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    return render(request, "transporte/vehiculos/detalle_vehiculo.html", {"vehiculo": vehiculo})

@login_required
def vehiculo_crear(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehículo creado correctamente.")
            return redirect("transporte:vehiculos_listado")
    else:
        form = VehiculoForm()
    return render(request, "transporte/vehiculos/form_vehiculo.html", {"form": form})

@login_required
def vehiculo_editar(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehículo actualizado correctamente.")
            return redirect("transporte:vehiculos_listado")
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, "transporte/vehiculos/form_vehiculo.html", {"form": form})

@login_required
def vehiculo_eliminar(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado correctamente.")
    return redirect("transporte:vehiculos_listado")

# -----------------------------
#           AERONAVES
# -----------------------------
def aeronaves_listado(request):
    query = request.GET.get('q')
    if query:
        aeronaves = Aeronave.objects.filter(
            Q(matricula__icontains=query) | 
            Q(tipo_aeronave__icontains=query)
        )
    else:
        aeronaves = Aeronave.objects.all()
    return render(request, "transporte/aeronaves/listado_aeronaves.html", {"aeronaves": aeronaves})

def aeronave_detalle(request, pk):
    aeronave = get_object_or_404(Aeronave, pk=pk)
    return render(request, "transporte/aeronaves/detalle_aeronave.html", {"aeronave": aeronave})

@login_required
def aeronave_crear(request):
    if request.method == "POST":
        form = AeronaveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aeronave creada correctamente.")
            return redirect("transporte:aeronaves_listado")
    else:
        form = AeronaveForm()
    return render(request, "transporte/aeronaves/form_aeronave.html", {"form": form})

@login_required
def aeronave_editar(request, pk):
    aeronave = get_object_or_404(Aeronave, pk=pk)
    if request.method == "POST":
        form = AeronaveForm(request.POST, instance=aeronave)
        if form.is_valid():
            form.save()
            messages.success(request, "Aeronave actualizada correctamente.")
            return redirect("transporte:aeronaves_listado")
    else:
        form = AeronaveForm(instance=aeronave)
    return render(request, "transporte/aeronaves/form_aeronave.html", {"form": form})

@login_required
def aeronave_eliminar(request, pk):
    aeronave = get_object_or_404(Aeronave, pk=pk)
    aeronave.delete()
    messages.success(request, "Aeronave eliminada correctamente.")
    return redirect("transporte:aeronaves_listado")

# -----------------------------
#           CONDUCTORES
# -----------------------------
def conductores_listado(request):
    query = request.GET.get('q')
    if query:
        conductores = Conductor.objects.filter(
            Q(nombre__icontains=query) | 
            Q(rut__icontains=query) |
            Q(licencia__icontains=query)
        )
    else:
        conductores = Conductor.objects.all()
    return render(request, "transporte/conductores/listado_conductores.html", {"conductores": conductores})

def conductor_detalle(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    return render(request, "transporte/conductores/detalle_conductor.html", {"conductor": conductor})

@login_required
def conductor_crear(request):
    if request.method == "POST":
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conductor creado correctamente.")
            return redirect("transporte:conductores_listado")
    else:
        form = ConductorForm()
    return render(request, "transporte/conductores/form_conductor.html", {"form": form})

@login_required
def conductor_editar(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == "POST":
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            messages.success(request, "Conductor actualizado correctamente.")
            return redirect("transporte:conductores_listado")
    else:
        form = ConductorForm(instance=conductor)
    return render(request, "transporte/conductores/form_conductor.html", {"form": form})

@login_required
def conductor_eliminar(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    conductor.delete()
    messages.success(request, "Conductor eliminado correctamente.")
    return redirect("transporte:conductores_listado")

# -----------------------------
#             PILOTOS
# -----------------------------
def pilotos_listado(request):
    query = request.GET.get('q')
    if query:
        pilotos = Piloto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(rut__icontains=query) |
            Q(certificacion__icontains=query)
        )
    else:
        pilotos = Piloto.objects.all()
    return render(request, "transporte/pilotos/listado_pilotos.html", {"pilotos": pilotos})

def piloto_detalle(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    return render(request, "transporte/pilotos/detalle_piloto.html", {"piloto": piloto})

@login_required
def piloto_crear(request):
    if request.method == "POST":
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Piloto creado correctamente.")
            return redirect("transporte:pilotos_listado")
    else:
        form = PilotoForm()
    return render(request, "transporte/pilotos/form_piloto.html", {"form": form})

@login_required
def piloto_editar(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    if request.method == "POST":
        form = PilotoForm(request.POST, instance=piloto)
        if form.is_valid():
            form.save()
            messages.success(request, "Piloto actualizado correctamente.")
            return redirect("transporte:pilotos_listado")
    else:
        form = PilotoForm(instance=piloto)
    return render(request, "transporte/pilotos/form_piloto.html", {"form": form})

@login_required
def piloto_eliminar(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    piloto.delete()
    messages.success(request, "Piloto eliminado correctamente.")
    return redirect("transporte:pilotos_listado")

# -----------------------------
#             CLIENTES
# -----------------------------
def clientes_listado(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | 
            Q(rut__icontains=query) |
            Q(direccion__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()
    return render(request, "transporte/clientes/listado_clientes.html", {"clientes": clientes})

def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "transporte/clientes/detalle_cliente.html", {"cliente": cliente})

@login_required
def cliente_crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado correctamente.")
            return redirect("transporte:clientes_listado")
    else:
        form = ClienteForm()
    return render(request, "transporte/clientes/form_cliente.html", {"form": form})

@login_required
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado correctamente.")
            return redirect("transporte:clientes_listado")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "transporte/clientes/form_cliente.html", {"form": form})

@login_required
def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    messages.success(request, "Cliente eliminado correctamente.")
    return redirect("transporte:clientes_listado")

# -----------------------------
#             CARGAS
# -----------------------------
def cargas_listado(request):
    query = request.GET.get('q')
    if query:
        cargas = Carga.objects.filter(
            Q(descripcion__icontains=query) | 
            Q(tipo_mercancia__icontains=query) |
            Q(cliente__nombre__icontains=query)
        )
    else:
        cargas = Carga.objects.all()
    return render(request, "transporte/cargas/listado_cargas.html", {"cargas": cargas})

def carga_detalle(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    return render(request, "transporte/cargas/detalle_carga.html", {"carga": carga})

@login_required
def carga_crear(request):
    if request.method == "POST":
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Carga creada correctamente.")
            return redirect("transporte:cargas_listado")
    else:
        form = CargaForm()
    return render(request, "transporte/cargas/form_carga.html", {"form": form})

@login_required
def carga_editar(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    if request.method == "POST":
        form = CargaForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            messages.success(request, "Carga actualizada correctamente.")
            return redirect("transporte:cargas_listado")
    else:
        form = CargaForm(instance=carga)
    return render(request, "transporte/cargas/form_carga.html", {"form": form})

@login_required
def carga_eliminar(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    carga.delete()
    messages.success(request, "Carga eliminada correctamente.")
    return redirect("transporte:cargas_listado")

# -----------------------------
#             DESPACHOS
# -----------------------------
def despachos_listado(request):
    query = request.GET.get('q')
    if query:
        despachos = Despacho.objects.filter(
            Q(ruta__origen__icontains=query) | 
            Q(ruta__destino__icontains=query) |
            Q(estado__icontains=query) |
            Q(vehiculo__patente__icontains=query) |
            Q(aeronave__matricula__icontains=query) |
            Q(conductor__nombre__icontains=query) |
            Q(piloto__nombre__icontains=query)
        )
    else:
        despachos = Despacho.objects.all()
    return render(request, "transporte/despachos/listado_despachos.html", {"despachos": despachos})

def despacho_detalle(request, pk):
    despacho = get_object_or_404(Despacho, pk=pk)
    return render(request, "transporte/despachos/detalle_despacho.html", {"despacho": despacho})

@login_required
def despacho_crear(request):
    if request.method == "POST":
        form = DespachoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Despacho creado correctamente.")
            return redirect("transporte:despachos_listado")
    else:
        form = DespachoForm()
    return render(request, "transporte/despachos/form_despacho.html", {"form": form})

@login_required
def despacho_editar(request, pk):
    despacho = get_object_or_404(Despacho, pk=pk)
    if request.method == "POST":
        form = DespachoForm(request.POST, instance=despacho)
        if form.is_valid():
            form.save()
            messages.success(request, "Despacho actualizado correctamente.")
            return redirect("transporte:despachos_listado")
    else:
        form = DespachoForm(instance=despacho)
    return render(request, "transporte/despachos/form_despacho.html", {"form": form})

@login_required
def despacho_eliminar(request, pk):
    despacho = get_object_or_404(Despacho, pk=pk)
    despacho.delete()
    messages.success(request, "Despacho eliminado correctamente.")
    return redirect("transporte:despachos_listado")

# ===========================================================
#              LOGIN / LOGOUT
# ===========================================================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('transporte:dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "transporte/auth/login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect('transporte:login')

@login_required
def dashboard(request):
    context = {
        "total_rutas": Ruta.objects.count(),
        "total_vehiculos": Vehiculo.objects.count(),
        "total_aeronaves": Aeronave.objects.count(),
        "total_conductores": Conductor.objects.count(),
        "total_pilotos": Piloto.objects.count(),
        "total_clientes": Cliente.objects.count(),
        "total_cargas": Carga.objects.count(),
        "total_despachos": Despacho.objects.count(),
    }
    return render(request, "transporte/dashboard.html", context)