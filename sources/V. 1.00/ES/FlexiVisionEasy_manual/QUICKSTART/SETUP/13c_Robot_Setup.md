(robotsetup)=
# **Configuración del Robot** 

Esta sección describe el procedimiento para configurar la comunicación TCP/IP entre el sistema FlexiVision One y el robot industrial. Una comunicación adecuada es esencial para permitir el intercambio de coordenadas y comandos entre los dos sistemas.

```{note}
**Requisitos previos**

Antes de continuar, asegúrese de que:
- El robot está encendido y operativo
- El cable Ethernet entre VisionController y el robot está conectado
- El robot está configurado para aceptar conexiones TCP/IP (consulte el manual del robot)
- Se conoce el puerto de comunicación configurado en el código del robot
```

---

## Acceso a la configuración del Robot

```{list-table}

* - **1** 
  - Desde la página principal del software, hacer clic en <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - En la página SETUP, identificar y hacer clic en el icono **Robot Setup**
    ```{dropdown} Página de configuración 
       ![Página de configuración](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Se abre la página de configuración de la comunicación con el robot
```

---

## Visión general de la interfaz Robot Setup

La página Configuración del robot presenta varias secciones para configurar y probar la comunicación:
![Página de configuración del robot](../../../../../_shared/media/images/pagina_robotsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sección
  - Descripción
* - **Port**
  - Puerto TCP/IP con el que el robot comunica (configurado en el controlador del robot)
* - **Reconfigure Server**
  - Botón para reconfigurar el servidor de comunicación con nuevos parámetros
* - **Server Online**
  - Indicador de estado del servidor FlexiVision One (verde = servidor activo y accesible)
* - **Client Connect**
  -  Indicador de estado del cliente robot (verde = robot conectado)
* - **Mensajes robot-flexivision**
  - Ventanas de registro que muestran los mensajes intercambiados entre el robot y FlexiVision One (utilizadas para depuración):
      - la primera ventana (la más pequeña) indica los mensajes que FlexiVision One o el operador envían
      - la segunda ventana indica los mensajes que FlexiVision recibe
```

---
## Procedimiento de configuración

### *Paso 1: Inserción del puerto de comunicación*

El puerto TCP/IP es el parámetro crítico que debe coincidir entre el robot y FlexiVision One:

```{list-table}
* - **4** 
  - En el campo **Port**, introducir el número del puerto TCP/IP con el que se comunicará el robot
```
```{note}
Valor predeterminado:      (puerto estándar FlexiVision One)  
El número de puerto debe ser:
   - El mismo configurado en el programa del robot
   - Comprendido entre 1024 y 65535 (puertos de usuario)
   - Sin conflictos con otros servicios en la red
```

```{warning}

Es **esencial** que el número de puerto sea idéntico en ambos lados:
- **FlexiVision One**: Puerto configurado en esta página
- **Robot**: Puerto configurado en el programa del robot 

Si los números no coinciden, la conexión siempre fallará.

Ejemplo:
- ❌ INCORRECTO: FlexiVision One puerto 2000, Robot puerto 2001 → Sin comunicación
- ✅ CORRECTO: FlexiVision One puerto 2000, Robot puerto 2000 → Comunicación funcionando
```

### *Paso 2: Reconfiguración del servidor*

Después de configurar el puerto correcto, es necesario reiniciar el servidor de comunicación:

```{list-table}
* - **5** 
  - Hacer clic en el botón **Reconfigure Server**
* - **6**
  - Esperar unos segundos hasta que finalice la reconfiguración
```

```{note}

Es necesario hacer clic en **Reconfigure Server** cada vez que:
- Se modifica el número de puerto
- Se desea reiniciar el servidor tras un error
- Se ha modificado la configuración de red del VisionController
- Se desea forzar el cierre de las conexiones existentes

El servidor se inicia automáticamente al abrir el software FlexiVision One, pero requiere una reconfiguración manual después de realizar cambios.
```

### *Paso 3: Verificación del estado del servidor*

Tras la reconfiguración, compruebe que el servidor está activo:

```{list-table}

* - **7**
  - Observar el indicador **Server Online**:
   - **Verde**: Servidor activo   
     **Rojo**: Servidor no activo  
* - **8**
  - después de iniciar el programa desde el robot, observar el indicador **Client Online**:
   - **Verde**: robot conectado  
     **Rojo**: robot no conectado 

```
```{note}
Si los indicadores están verdes, el sistema está correctamente conectado. 

Si uno de los indicadores está rojo, verificar:
   - Comprobar que el programa en el robot se ha iniciado 
   - Comprobar que las direcciones IP están en la misma subred
   - Que el puerto no está siendo utilizado por otro programa
   - Los registros del sistema para mensajes de error
```
### *Paso 4: Guardado y finalización*

```{list-table}
:header-rows: 0
:widths: 10 90

* - **9**
  - Comprobar que la conexión robot → FlexiVision One es estable

* - **10**
  - Los parámetros de comunicación se guardan automáticamente

* - **11**
  - Volver a la página principal **SETUP**
```

---

## Próximos pasos

Una vez completada la Configuración del Robot, proceda con:

- [Configuración del protocolo](protocol_setup)
- [Guardar la receta](ricettabase)


