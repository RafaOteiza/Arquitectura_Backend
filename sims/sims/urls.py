from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sims/', include('sim_msisdn.urls')),  # Incluir las rutas del microservicio SIMs
]
