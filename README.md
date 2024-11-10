# Arquitectura de Microservicios

Este proyecto se compone de cuatro microservicios, cada uno gestionando una parte específica del sistema de validadores y SIMs. La modularidad permite escalabilidad y una separación clara de responsabilidades, con cada microservicio teniendo su base de datos y lógica independientes.

## ¿Cómo probar el proyecto?

### Instalación de dependencias
- Al ejecutar `python manage.py runserver`, es posible que aparezcan errores por dependencias faltantes. Instala los paquetes necesarios con los siguientes comandos:

   ```bash
   pip install djangorestframework
   pip install requests

### Ejecución de los microservicios
- Cada microservicio debe ejecutarse de forma independiente, ya que no pueden compartir el mismo puerto. A continuación se detalla cómo levantar cada uno:

   - **Usuarios**: utiliza el puerto 8000.
   - **Sims**: utiliza el puerto 8001.
   - **Validadores**: utiliza el puerto 8002.


- Para ejecutar cada microservicio, abre un terminal separado y ejecuta:

   ```bash
   python manage.py runserver 8000  # Para el microservicio Usuarios
   python manage.py runserver 8001  # Para el microservicio Sims
   python manage.py runserver 8002  # Para el microservicio Validadores

### Microservicios y Endpoints

### 1. Microservicio de Usuarios (Puerto 8000)

- **URLs principales:**
  - **Roles**: [http://127.0.0.1:8000/usuarios/roles/](http://127.0.0.1:8000/usuarios/roles/)
  - **Usuarios**: [http://127.0.0.1:8000/usuarios/usuarios/](http://127.0.0.1:8000/usuarios/usuarios/)

#### Endpoints

- **Usuarios (`/usuarios/`)**
  - `GET /usuarios/`: Lista todos los usuarios.
  - `POST /usuarios/`: Crea un nuevo usuario.
  - `GET /usuarios/<id>/`: Obtiene un usuario específico.
  - `PUT /usuarios/<id>/`: Actualiza todos los datos de un usuario.
  - `PATCH /usuarios/<id>/`: Actualiza datos parciales de un usuario.
  - `DELETE /usuarios/<id>/`: Elimina un usuario.

- **Roles (`/roles/`)**
  - `GET /roles/`: Lista todos los roles.
  - `POST /roles/`: Crea un nuevo rol.
  - `GET /roles/<id>/`: Obtiene un rol específico.
  - `PUT /roles/<id>/`: Actualiza todos los datos de un rol.
  - `PATCH /roles/<id>/`: Actualiza datos parciales de un rol.
  - `DELETE /roles/<id>/`: Elimina un rol.

---

### 2. Microservicio de Sims (Puerto 8001)

- **URLs principales:**
  - **MSISDN**: [http://127.0.0.1:8001/sims/msisdn/](http://127.0.0.1:8001/sims/msisdn/)
  - **SimMsisdn**: [http://127.0.0.1:8001/sims/sim-msisdn/](http://127.0.0.1:8001/sims/sim-msisdn/)
  - **EstadoSim**: [http://127.0.0.1:8001/sims/estado-sim/](http://127.0.0.1:8001/sims/estado-sim/)

#### Endpoints

- **MSISDN (`/msisdn/`)**
  - `GET /msisdn/`: Lista todos los registros de MSISDN.
  - `POST /msisdn/`: Crea un nuevo MSISDN.
  - `GET /msisdn/<id>/`: Obtiene un MSISDN específico.
  - `PUT /msisdn/<id>/`: Actualiza un MSISDN.
  - `DELETE /msisdn/<id>/`: Elimina un MSISDN.

- **SimMsisdn (`/sim-msisdn/`)**
  - `GET /sim-msisdn/`: Lista todos los registros de SimMsisdn.
  - `POST /sim-msisdn/`: Crea un nuevo SimMsisdn.
  - `GET /sim-msisdn/<id>/`: Obtiene un SimMsisdn específico.
  - `PUT /sim-msisdn/<id>/`: Actualiza un SimMsisdn.
  - `DELETE /sim-msisdn/<id>/`: Elimina un SimMsisdn.

- **EstadoSim (`/estado-sim/`)**
  - `GET /estado-sim/`: Lista todos los registros de EstadoSim.
  - `POST /estado-sim/`: Crea un nuevo EstadoSim.
  - `GET /estado-sim/<id>/`: Obtiene un EstadoSim específico.
  - `PUT /estado-sim/<id>/`: Actualiza un EstadoSim.
  - `DELETE /estado-sim/<id>/`: Elimina un EstadoSim.

---

### 3. Microservicio de Validadores y Ubicaciones (Puerto 8002)

- **URLs principales:**
  - **Ubicaciones**: [http://127.0.0.1:8002/validadores/ubicaciones/](http://127.0.0.1:8002/validadores/ubicaciones/)
  - **EstadoValidador**: [http://127.0.0.1:8002/validadores/estados-validador/](http://127.0.0.1:8002/validadores/estados-validador/)
  - **Validadores**: [http://127.0.0.1:8002/validadores/validadores/](http://127.0.0.1:8002/validadores/validadores/)
  - **SimValidador**: [http://127.0.0.1:8002/validadores/sim_validador/](http://127.0.0.1:8002/validadores/sim_validador/)
  - **HistorialUbicaciones**: [http://127.0.0.1:8002/validadores/historial-ubicaciones/](http://127.0.0.1:8002/validadores/historial-ubicaciones/)

#### Endpoints

- **Ubicaciones (`/ubicaciones/`)**
  - `GET /ubicaciones/`: Lista todas las ubicaciones.
  - `POST /ubicaciones/`: Crea una nueva ubicación.
  - `GET /ubicaciones/<id>/`: Obtiene una ubicación específica.
  - `PUT /ubicaciones/<id>/`: Actualiza una ubicación.
  - `DELETE /ubicaciones/<id>/`: Elimina una ubicación.

- **EstadoValidador (`/estados-validador/`)**
  - `GET /estados-validador/`: Lista todos los estados de validadores.
  - `POST /estados-validador/`: Crea un nuevo estado.
  - `GET /estados-validador/<id>/`: Obtiene un estado específico.
  - `PUT /estados-validador/<id>/`: Actualiza un estado.
  - `DELETE /estados-validador/<id>/`: Elimina un estado.

- **Validadores (`/validadores/`)**
  - `GET /validadores/`: Lista todos los validadores.
  - `POST /validadores/`: Crea un nuevo validador.
  - `GET /validadores/<id>/`: Obtiene un validador específico.
  - `PUT /validadores/<id>/`: Actualiza un validador.
  - `DELETE /validadores/<id>/`: Elimina un validador.

- **SimValidador (`/sim_validador/`)**
  - `GET /sim_validador/`: Lista todos los registros de SimValidador.
  - `POST /sim_validador/`: Crea una nueva relación SimValidador.
  - `GET /sim_validador/<id>/`: Obtiene un SimValidador específico.
  - `PUT /sim_validador/<id>/`: Actualiza un SimValidador.
  - `DELETE /sim_validador/<id>/`: Elimina un SimValidador.

- **HistorialUbicaciones (`/historial-ubicaciones/`)**
  - `GET /historial-ubicaciones/`: Lista el historial de ubicaciones de los validadores.
  - `POST /historial-ubicaciones/`: Registra un nuevo movimiento.
  - `GET /historial-ubicaciones/<id>/`: Obtiene un movimiento específico.
  - `PUT /historial-ubicaciones/<id>/`: Actualiza un movimiento.
  - `DELETE /historial-ubicaciones/<id>/`: Elimina un movimiento.

