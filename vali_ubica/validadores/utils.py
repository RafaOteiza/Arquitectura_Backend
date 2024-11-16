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

#BUSCAR SIMS
def obtener_datos_sim(iccid):
    url = f'{settings.SIMS_URL}/sims/{iccid}/'  # Ajusta la URL según el endpoint del microservicio de SIMs
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: SIM con ICCID {iccid} no encontrada. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servicio de SIMs: {e}")
        return None

#Obtener para listarlos
def obtener_iccids_disponibles():
    url = f'{settings.SIMS_URL}/sims/sim-msisdn/'  # Endpoint del microservicio sims
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Devuelve una lista de tuplas con (ICCID, ICCID)
            return [(sim['iccid']) for sim in data]
        else:
            print(f"Error al obtener ICCIDs. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servicio de SIMs: {e}")
        return []

