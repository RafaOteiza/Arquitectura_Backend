import requests
from django.core.cache import cache
from django.conf import settings

def obtener_usuario(id_usuario):
    # Intenta obtener el usuario de la caché
    usuario = cache.get(f"usuario_{id_usuario}")
    if usuario is None:
        # Si no está en la caché, usa la URL completa con la estructura correcta
        url = f"{settings.USUARIOS_AUTH_URL}/usuarios/usuarios/{id_usuario}/" #tenia mala esta wea porque el primer usuarios es del micro servicio y el segundo es de la tabla usuarios
        response = requests.get(url)
        if response.status_code == 200:
            usuario = response.json()
            # Guarda el usuario en la caché por 5 minutos
            cache.set(f"usuario_{id_usuario}", usuario, timeout=300)
    return usuario


def obtener_todos():
    # Intenta obtener la lista de usuarios de la caché
    usuarios = cache.get("todos_los_usuarios")
    if usuarios is None:
        # Si no está en la caché, hace la solicitud al microservicio
        url = f"{settings.USUARIOS_AUTH_URL}/usuarios/usuarios/"
        response = requests.get(url)
        if response.status_code == 200:
            usuarios = response.json()
            # Guarda la lista de usuarios en la caché por 5 minutos
            cache.set("todos_los_usuarios", usuarios, timeout=300)
    return usuarios