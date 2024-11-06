from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MSISDNViewSet, SimMsisdnViewSet, EstadoSimViewSet, TestUsuarioView

router = DefaultRouter()
router.register(r'msisdn', MSISDNViewSet)
router.register(r'sim-msisdn', SimMsisdnViewSet)
router.register(r'estado-sim', EstadoSimViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluir el router
    path('test-usuario/<int:id_usuario>/', TestUsuarioView.as_view(), name='test-usuario'),

]
