from django.urls import path, include

urlpatterns = [
    path('validadores/', include('validadores.urls')),

]
