# Arquitectura de Microservicios

Este proyecto está estructurado en cinco microservicios principales para gestionar la funcionalidad del sistema de validadores y SIMs. Cada microservicio tiene su propia responsabilidad y permite la modularización y escalabilidad del sistema. Cada microservicio está diseñado para cumplir una función específica, con su propia base de datos y lógica. Los servicios se comunican entre sí según lo requiera la lógica de negocio.

## ¿Cómo probar el proyecto?

### Instalación de dependencias
- Al descargar el proyecto y al intentar ejecutar `python manage.py runserver`, es posible que aparezca un error debido a dependencias faltantes. Para solucionarlo, instala los paquetes necesarios con los siguientes comandos:

   - `pip install djangorestframework`
   - `pip install requests`

### Ejecución de los microservicios
- Cada microservicio debe ejecutarse de forma independiente, ya que no pueden compartir el mismo puerto. A continuación se detalla cómo levantar cada uno:

   - **Usuarios**: utiliza el puerto 8000.
   - **Sims**: utiliza el puerto 8001.

- Para ejecutar cada microservicio, abre un terminal separado y ejecuta:

   ```bash
   python manage.py runserver 8000  # Para el microservicio Usuarios
   python manage.py runserver 8001  # Para el microservicio Sims

### Microservicios Implementados

#### 1. Usuarios y Autenticación (antes de la url utiliza `/usuarios/`)
   - **Tablas**: `Usuarios`, `Roles`
   - **Descripción**: Este servicio gestiona el acceso y control de los usuarios en el sistema, permitiendo autenticar y autorizar según los roles definidos (administrador, técnico, consultor).
   - **Funciones**: CRUD de usuarios, autenticación (login), asignación de roles y permisos.
   - **Dependencias Externas**: No necesita interactuar directamente con otros microservicios, pero los otros microservicios pueden consultar a este para verificar roles y permisos.

   #### Endpoints para Usuarios (`/usuarios/`)
   - `GET /usuarios/`: Obtiene la lista de todos los usuarios.
   - `POST /usuarios/`: Crea un nuevo usuario.
   - `GET /usuarios/<id>/`: Obtiene la información de un usuario específico por su ID.
   - `PUT /usuarios/<id>/`: Actualiza todos los campos de un usuario específico.
   - `PATCH /usuarios/<id>/`: Actualiza uno o más campos de un usuario específico.
   - `DELETE /usuarios/<id>/`: Elimina un usuario específico.

   #### Endpoints para Roles (`/roles/`)
   - `GET /roles/`: Obtiene la lista de todos los roles.
   - `POST /roles/`: Crea un nuevo rol.
   - `GET /roles/<id>/`: Obtiene la información de un rol específico por su ID.
   - `PUT /roles/<id>/`: Actualiza todos los campos de un rol específico.
   - `PATCH /roles/<id>/`: Actualiza uno o más campos de un rol específico.
   - `DELETE /roles/<id>/`: Elimina un rol específico.

#### 2. SIMs y MSISDN (antes de la url utiliza `/sims/`)
   - **Tablas**: `msisdn`, `sim_msisdn`, `estado_sim`
   - **Descripción**: Este servicio maneja todo lo relacionado con las SIMs y sus números asociados (MSISDN). Incluye la administración de los estados de SIM y el seguimiento de las SIMs asignadas a cada MSISDN, con información sobre el estado y la disponibilidad.
   - **Funciones**: CRUD de SIMs y MSISDN, cambio de estado, asignación y disociación de SIMs a números MSISDN.
   - **Dependencias Externas**: Puede comunicarse con el microservicio de Validadores y Ubicaciones para registrar relaciones entre SIMs y validadores.

   #### Microservicio de Sims (Puerto 8001)
   
   #### Endpoints para MSISDN (`/msisdn/`)
   - `GET /msisdn/`: Lista todos los registros de MSISDN.
   - `POST /msisdn/`: Crea un nuevo MSISDN.
   - `GET /msisdn/<id>/`: Obtiene un MSISDN específico.
   - `PUT /msisdn/<id>/`: Actualiza un MSISDN específico.
   - `DELETE /msisdn/<id>/`: Elimina un MSISDN específico.

   #### Endpoints para SimMsisdn (`/sim-msisdn/`)
   - `GET /sim-msisdn/`: Lista todos los registros de SimMsisdn.
   - `POST /sim-msisdn/`: Crea un nuevo SimMsisdn.
   - `GET /sim-msisdn/<id>/`: Obtiene un SimMsisdn específico.
   - `PUT /sim-msisdn/<id>/`: Actualiza un SimMsisdn específico.
   - `DELETE /sim-msisdn/<id>/`: Elimina un SimMsisdn específico.

   #### Endpoints para EstadoSim (`/estado-sim/`)
   - `GET /estado-sim/`: Lista todos los registros de EstadoSim.
   - `POST /estado-sim/`: Crea un nuevo EstadoSim.
   - `GET /estado-sim/<id>/`: Obtiene un EstadoSim específico.
   - `PUT /estado-sim/<id>/`: Actualiza un EstadoSim específico.
   - `DELETE /estado-sim/<id>/`: Elimina un EstadoSim específico.

3. **Validadores y Ubicaciones**  
   - **Tablas**: `validador`, `estado_validador`, `Ubicacion`
   - **Descripción**: Este es el núcleo del sistema, ya que maneja los validadores, incluyendo su estado, ubicación actual y serie. Este servicio gestiona la ubicación y el estado de los validadores para simplificar las consultas.
   - **Funciones**: CRUD de validadores, actualización de estado, cambio de ubicación, creación y administración de ubicaciones.
   - **Dependencias Externas**: Consulta al microservicio de SIMs y MSISDN para la asignación de SIMs a los validadores.

4. **Relación y Movimiento de SIMs y Validadores**  
   - **Tablas**: `sim_validador`, `HistorialUbicacionesValidador`
   - **Descripción**: Este servicio es el intermediario para gestionar la relación entre las SIMs y los validadores, además de rastrear los movimientos de los validadores a través de sus ubicaciones. Es aquí donde se crean los registros de entrada y salida de los validadores, y se mantiene un historial completo de movimientos.
   - **Funciones**: Asignación y disociación de SIMs a validadores, registro de movimiento de validadores entre ubicaciones, mantenimiento del historial de ubicaciones de cada validador.
   - **Dependencias Externas**: Hace solicitudes al microservicio Validadores y Ubicaciones para validar la disponibilidad del validador y al microservicio SIMs y MSISDN para verificar la disponibilidad de SIMs.

5. **Reportes y Notificaciones**  
   - **Tablas**: No requiere tablas propias, pero consulta otras.
   - **Descripción**: Este microservicio se encarga de generar reportes y enviar notificaciones en función de los datos en otros microservicios. Si es necesario, puedes usarlo para monitorear cambios de estado, registrar eventos importantes, y generar reportes específicos para los consultores.
   - **Funciones**: Generación de reportes, consulta de estados, generación de notificaciones según eventos en otros microservicios.
   - **Dependencias Externas**: Consume datos de los microservicios SIMs y MSISDN, Validadores y Ubicaciones, y Relación y Movimiento de SIMs y Validadores.

V.2