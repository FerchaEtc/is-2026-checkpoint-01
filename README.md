# is-2026-checkpoint-01

## **Integrantes:**

|  Feature  |   Responsable                 |
|-----------|-------------------------------|
|     1     |   Etchanchu Paoltroni Fermin  |
|     2     |   Flores Bautista             |
|     3     |   Iroz Nahuel                 |
|     4     |   Etchanchu Paoltroni Fermin  |
|     5     |   Flores Bautista             |
 -----
## **Instrucciones de uso:**

 1- Clonar el repositorio.\
 2- Crear el archivo .env en la raiz del proyecto con las variables de entorno correspondientes, usando como base el archivo .env.ejemplo.\
 3- Tener Docker abierto y en ejecución.\
 4- Una vez en la terminal, ejecutar el comando `docker compose up --build`.\
 5- Para acceder a cada servicio:
  + Frontend → http://localhost:8080;
  + Backend → http://localhost:5000;
  + Portainer → http://localhost:9000.

### Instrucciones para Portainer

1. **Acceso a la Interfaz:** Ingresar desde la web a [http://localhost:9000](http://localhost:9000).
2. **Credenciales (Primer ingreso):** - Al ser una instalación limpia montada en un volumen nuevo, Portainer solicita la creación de un usuario administrador. 
   - Definir un nombre de usuario y una contraseña segura.
3. **Conexión al Entorno Local:** - Una vez iniciada la sesión, selecciona la opción "Get Started".
   - Esto conecta a Portainer con el socket de Docker del host (`/var/run/docker.sock`), le otorga permisos para visualizar y administrar los contenedores del proyecto.

(La imagen con los contenedores corriendo se encuentra en el directorio `/docs` del repositorio).