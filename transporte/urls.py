# transporte/urls.py
from django.urls import path
from . import views

app_name = "transporte"

urlpatterns = [
    # =========================
    #         DASHBOARD
    # =========================
    path('', views.dashboard, name='dashboard'),

    # =========================
    #         RUTAS
    # =========================
    path('rutas/', views.rutas_listado, name='rutas_listado'),
    path('rutas/nuevo/', views.ruta_crear, name='ruta_crear'),
    path('rutas/<int:pk>/editar/', views.ruta_editar, name='ruta_editar'),
    path('rutas/<int:pk>/eliminar/', views.ruta_eliminar, name='ruta_eliminar'),
    path('rutas/<int:pk>/', views.ruta_detalle, name='ruta_detalle'),

    # =========================
    #         VEHÍCULOS
    # =========================
    path('vehiculos/', views.vehiculos_listado, name='vehiculos_listado'),
    path('vehiculos/nuevo/', views.vehiculo_crear, name='vehiculo_crear'),
    path('vehiculos/<int:pk>/editar/', views.vehiculo_editar, name='vehiculo_editar'),
    path('vehiculos/<int:pk>/eliminar/', views.vehiculo_eliminar, name='vehiculo_eliminar'),
    path('vehiculos/<int:pk>/', views.vehiculo_detalle, name='vehiculo_detalle'),

    # =========================
    #         AERONAVES
    # =========================
    path('aeronaves/', views.aeronaves_listado, name='aeronaves_listado'),
    path('aeronaves/nuevo/', views.aeronave_crear, name='aeronave_crear'),
    path('aeronaves/<int:pk>/editar/', views.aeronave_editar, name='aeronave_editar'),
    path('aeronaves/<int:pk>/eliminar/', views.aeronave_eliminar, name='aeronave_eliminar'),
    path('aeronaves/<int:pk>/', views.aeronave_detalle, name='aeronave_detalle'),

    # =========================
    #         CONDUCTORES
    # =========================
    path('conductores/', views.conductores_listado, name='conductores_listado'),
    path('conductores/nuevo/', views.conductor_crear, name='conductor_crear'),
    path('conductores/<int:pk>/editar/', views.conductor_editar, name='conductor_editar'),
    path('conductores/<int:pk>/eliminar/', views.conductor_eliminar, name='conductor_eliminar'),
    path('conductores/<int:pk>/', views.conductor_detalle, name='conductor_detalle'),

    # =========================
    #         PILOTOS
    # =========================
    path('pilotos/', views.pilotos_listado, name='pilotos_listado'),
    path('pilotos/nuevo/', views.piloto_crear, name='piloto_crear'),
    path('pilotos/<int:pk>/editar/', views.piloto_editar, name='piloto_editar'),
    path('pilotos/<int:pk>/eliminar/', views.piloto_eliminar, name='piloto_eliminar'),
    path('pilotos/<int:pk>/', views.piloto_detalle, name='piloto_detalle'),

    # =========================
    #         CLIENTES
    # =========================
    path('clientes/', views.clientes_listado, name='clientes_listado'),
    path('clientes/nuevo/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),
    path('clientes/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),

    # =========================
    #         CARGAS
    # =========================
    path('cargas/', views.cargas_listado, name='cargas_listado'),
    path('cargas/nuevo/', views.carga_crear, name='carga_crear'),
    path('cargas/<int:pk>/editar/', views.carga_editar, name='carga_editar'),
    path('cargas/<int:pk>/eliminar/', views.carga_eliminar, name='carga_eliminar'),
    path('cargas/<int:pk>/', views.carga_detalle, name='carga_detalle'),

    # =========================
    #         DESPACHOS
    # =========================
    path('despachos/', views.despachos_listado, name='despachos_listado'),
    path('despachos/nuevo/', views.despacho_crear, name='despacho_crear'),
    path('despachos/<int:pk>/editar/', views.despacho_editar, name='despacho_editar'),
    path('despachos/<int:pk>/eliminar/', views.despacho_eliminar, name='despacho_eliminar'),
    path('despachos/<int:pk>/', views.despacho_detalle, name='despacho_detalle'),

    # =========================
    #         LOGIN / LOGOUT
    # =========================
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
