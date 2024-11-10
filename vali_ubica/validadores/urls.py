from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UbicacionViewSet, EstadoValidadorViewSet, ValidadorViewSet,
    SimValidadorViewSet, HistorialUbicacionesValidadorViewSet
)

router = DefaultRouter()
router.register(r'ubicaciones', UbicacionViewSet)
router.register(r'estados-validador', EstadoValidadorViewSet)
router.register(r'validadores', ValidadorViewSet)
router.register(r'sim_validador', SimValidadorViewSet)
router.register(r'historial-ubicaciones', HistorialUbicacionesValidadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
