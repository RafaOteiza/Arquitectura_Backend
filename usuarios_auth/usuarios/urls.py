from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RolViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
# Esta es la vista que me returna todos los usuarios para después usar en lasplantillas :p
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#Aqui se definen las rutas para los endpoints de la API
#Seria weno que alguno probara con POSTMAN porque yo lo estoy haciendo directamente desde DJANGO. 