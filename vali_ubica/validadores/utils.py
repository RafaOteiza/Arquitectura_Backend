import requests
from django.conf import settings

def obtener_datos_usuario(id_usuario):
    url = f'{settings.USUARIOS_AUTH_URL}/usuarios/usuarios/{id_usuario}/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Usuario con id {id_usuario} no encontrado. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servicio de usuarios: {e}")
        return None
