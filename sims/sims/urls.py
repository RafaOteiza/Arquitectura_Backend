from django.urls import path, include

urlpatterns = [
    path('sims/', include('sim_msisdn.urls')),  # Incluir las rutas del microservicio `sims`
]
