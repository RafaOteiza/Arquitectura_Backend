from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'msisdn', views.MSISDNViewSet, basename='msisdn')
router.register(r'sim-msisdn', views.SimMsisdnViewSet, basename='sim-msisdn')
router.register(r'estado-sim', views.EstadoSimViewSet, basename='estado-sim')

urlpatterns = router.urls
