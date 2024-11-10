from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UbicacionViewSet, EstadoValidadorViewSet, ValidadorViewSet

router = DefaultRouter()
router.register(r'ubicaciones', UbicacionViewSet)
router.register(r'estados_validador', EstadoValidadorViewSet)
router.register(r'validadores', ValidadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
