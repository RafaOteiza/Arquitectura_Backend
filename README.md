# Arquitectura Backend

Este repositorio contiene la implementación del backend del sistema, diseñado con una arquitectura de microservicios para gestionar la funcionalidad de diferentes módulos.

## Estructura de Microservicios

Cada microservicio está diseñado para cumplir una función específica y comparte una única base de datos centralizada para simplificar la gestión de datos. Los servicios se comunican entre sí según lo requiera la lógica de negocio.

### Microservicios Implementados

1. **Gestión de Validadores**  
   - Funciones: CRUD de validadores, cambios de estado y ubicación.
   - Base de datos: `MySQL`

2. **Gestión de SIMs**  
   - Funciones: Asignación y disociación de SIMs, cambios de estado.
   - Base de datos: `MySQL`

3. **Gestión de Movimientos**  
   - Funciones: Registro de movimientos entre ubicaciones.
   - Base de datos: `MySQL`

4. **Usuarios (Autenticación y Control de Acceso)**  
   - Funciones: Autenticación de usuarios, gestión de roles y permisos.
   - Base de datos: `MySQL`

5. **Notificaciones**  
   - Funciones: Envío de notificaciones y alertas en tiempo real.
   - Base de datos: Sin base de datos específica, recibe datos de los otros microservicios.

6. **Reportes**  
   - Funciones: Generación de reportes sobre inventario y movimientos históricos.
   - Base de datos: Sin base de datos específica, recibe datos de los otros microservicios.

7. **Backups y Recuperación**  
   - Funciones: Respaldo periódico de bases de datos y restauración en caso de fallo.

### Tecnologías Usadas

- **Lenguaje de Programación**: Java (Spring Boot)
- **Base de Datos Centralizada**: MySQL compartida entre los microservicios
- **Mensajería**: Redis o RabbitMQ para notificaciones


## Instalación

1. Clonar el repositorio
   ```bash
   git clone https://github.com/RafaOteiza/Arquitectura_Backend.git
