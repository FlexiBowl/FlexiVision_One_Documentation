# **Configuración inicial**
```{warning}
**Componentes no accesibles**

Si no se puede acceder al FlexiBowl®, al robot o a la cámara:

1. Compruebe que todos los cables Ethernet están correctamente conectados
2. Compruebe que el Switch/enrutador está encendido
3. Compruebe las direcciones IP de todos los dispositivos:
   - Deben estar en la misma subred (p. ej: 192.168.1.x)
   - No debe haber conflictos de IP (dos dispositivos con la misma IP)
4. Utilice el comando `ping` terminal para probar la accesibilidad
5. Desactive temporalmente el cortafuegos de Windows en el puerto/adaptador utilizado para las cámaras GigE

Para más detalles sobre la configuración de la red, consulte [Cableado y conexiones](cablaggio).
```
(troubleshooting_cam_setup)=
## Solución de problemas de la sección Configuración de la cámara

```{warning}
**Problemas de enfoque**

Si la imagen aparece borrosa:

1. Compruebe que la cámara está a la distancia de trabajo correcta ([Cálculo de distancia óptima](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Compruebe que el objetivo esté completamente enroscado
3. Compruebe que no haya suciedad ni huellas dactilares en el objetivo
4. Asegúrese de que la cámara está montada perfectamente paralela a la superficie de trabajo FlexiBowl

```
```{tip}
**Problemas de luminosidad**

Si la imagen escaneada es demasiado oscura o demasiado clara:

**Demasiado oscuro**:
- Compruebe que la retroiluminación/iluminación superior está encendida (Config FlexiBowl®)
- Aumente el tiempo de exposición (parámetro Cam Exposure en [Camera FLB])

**Demasiado brillante (sobreexpuesta)**:
- Reduzca el tiempo de exposición (parámetro Cam Exposure en [Camera FLB])
- Compruebe que no haya excesiva luz ambiental
- Ajuste la apertura del diafragma en el cuerpo de la óptica de la cámara 
  :::{warning}
  Tenga especial cuidado al manipular la cámara, ya que, si la calibración ya se ha realizado, incluso un pequeño desplazamiento de la cámara puede comprometer la fiabilidad de la calibración
  :::
```
```{note}
**Adquisición de prestaciones**

Si la adquisición de imágenes es lenta:
- Compruebe que el cable Ethernet es Gigabit (Cat6 o superior)
- Compruebe que el Switch de red es Gigabit Ethernet (no Fast Ethernet 100Mbps)
- Cambie el nivel de latencia si no hay problemas con las pantallas azules
- Reduzca el tamaño de los paquetes a 1500-2000


La frecuencia de imagen máxima de la cámara es de 24 fps (imágenes por segundo), suficiente para todas las aplicaciones de picking estándar.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **Imagen demasiado oscura**
  - • Exposición de la cámara demasiado baja
    
    • Toplight apagada o defectuosa

    • Retroiluminación apagada o defectuosa

    • Toplight con potencia insuficiente
    
    • Objetivo con tapa protectora
  - • Aumente la exposición en Configuración de la cámara
    
    • Compruebe que la Toplight está encendida
    
    • Compruebe que la marca Light On está activada en la configuración FlexiBowl®
    
    • Compruebe la alimentación del Toplight
    
    • Retire la tapa del objetivo
* - **Imagen demasiado brillante (sobreexpuesta)**
  - • Exposición de la cámara demasiado alta
    
    • Reflejos de la superficie FlexiBowl®
  - • Disminuya la exposición en la configuración de la cámara
    
    • Sustituya la superficie de agarre por una menos reflectante
* - **Imagen borrosa**
  - • Objetivo desenfocado
    
    • Lente no totalmente atornillada
    
    • Lente sucia
    
    • Cámara en movimiento/vibración
  - • Enfoque correcto de la cámara
    
    • Atornille la lente hasta el contacto metal-metal
    
    • Limpie la lente con un paño de microfibra
    
    • Fije mejor la cámara y reduzca las vibraciones
* - **Imagen con artefactos o líneas**
  - • Interferencias electromagnéticas
    
    • Cable de cámara dañado
    
    • Sensor de cámara dañado
  - • Aleje el cable de la cámara de fuentes de EMI; utilice un cable apantallado
    
    • Sustituya el cable Ethernet de la cámara
    
    • Sustituya la cámara
* - **La cámara no adquiere durante el ciclo**
  - • Disparador no configurado
    
  - • Configure correctamente el disparador de adquisición
* - **La cámara no procesa durante el ciclo**
  - 
```
(scelta_camera)=
### *Procedimiento de configuración*

```{list-table}
* - **Acceso a la configuración**
  - 1. Hacer clic en el botón **Config Camera X** (donde X es el número de la cámara)
    2. Se abre la primera página del asistente de calibración, en la que se puede modificar el parámetro **Cam Exposure**

* - **Activación del modo avanzado**
  - 3. Haz clic en el botón **Experto** (abajo a la derecha)
    4. Este modo permite acceder a todos los ajustes avanzados de la cámara necesarios para la configuración inicial
* - **Configuración dispositivo de adquisición de imágenes**
  - 5. En el panel **Experto**, haga clic en la sección **Adquisición de imágenes** de **Ajustes**
    6. Haga clic en **Dispositivo de Adquisición de Imágenes**
    7. Se abre un menú para seleccionar los dispositivos de adquisición disponibles
* - **Identificación específica de la cámara**
  - 8. En el menú de dispositivos, seleccione la cámara deseada
        - Busque en la lista el número de serie o el modelo de la cámara
        - Ejemplo: "CAM-CIC-5000-20G-XXXXX" (donde XXXXX es el número de serie)
    9. Haga clic en la cámara para seleccionarla
```
:::{video} ../../../../_shared/media/videos/Step2_calib.mp4
  :width: 100%
  :align: center
:::

```{tip}
**Identificación del número de serie correcto**

Si aparecen varias cámaras o dispositivos:
- El número de serie se encuentra en una etiqueta en la cámara física
- Compare el último grupo de caracteres del número de serie para identificar la cámara correcta
- En caso de duda, desconecte físicamente otras cámaras para identificar la que está en uso
```


```{list-table} 
* - **Selección del formato de vídeo**
  - 11. Hacer clic en **Video Formats**
    12. En la lista de formatos disponibles, seleccionar **Generic GigEVision**
    13. Seleccionar **Mono** (monocromático) como tipo de sensor
```


```{warning}
**Formato correcto obligatorio**

Es esencial seleccionar **Generic GigEVision Mono**:
- Es posible que otros formatos no funcionen o provoquen errores
- Los formatos en color no son compatibles con esta cámara
- Si el formato no está disponible, es posible que falten controladores o configuraciones del sistema
```

```{list-table}
* - **Activación del sistema de adquisición**
  - 14. Después de seleccionar el formato correcto, haga clic en **Initialize Acquisition**  
    15. Espere a que finalice la inicialización (unos segundos)
* - **Verificación del funcionamiento de la adquisición**
  - 16. Localice el botón **Run** en la parte superior izquierda de la interfaz (icono "play")
    17. Haga clic en **Run** repetidamente (5-10 veces) para adquirir imágenes de prueba
    18. Observe el área de visualización de la imagen:
        - Debería mostrar la vista de la cámara sobre el FlexiBowl®
        - La imagen debería actualizarse con cada clic en Run
```

(schermo_blu)=
```{warning}
**Diagnóstico pantalla completamente azul**

Si la imagen escaneada aparece **completamente azul** al menos una vez durante la prueba:

**Causa**: Problema de comunicación GigE (latencia de red o tamaño de paquete subóptimo)

**Solución**

1. En el menú superior, seleccione **GigE** (o **GigE Vision Settings**)

2. Cambie los siguientes parámetros:
   - **Latency Level**
   - **Packet Size**

Proceda a los pasos siguientes para la configuración óptima de estos parámetros.
```

---

#### *Nivel de latencia*

```{note}
**Ajuste de latency**

El parámetro **Nivel de latencia** controla el búfer de comunicación entre la cámara y VisionController.

**Valores típicos**:
- Valor por defecto: 0
- Gama disponible: 0-3

**Cómo ajustar**:

1. Aumente gradualmente el valor
2. Después de cada cambio, pruebe la adquisición (botón Run) 5-10 veces
3. Si no aparecen más pantallas azules, el valor es correcto
4. Si persisten los pantallazos azules, aumente más o pruebe a cambiar el parámetro Tamaño de paquete
```

#### *Tamaño del paquete*

```{note}
**Ajuste de packet size**

El parámetro **Tamaño de paquete** define el tamaño de los paquetes de datos transmitidos a través de la red Ethernet.

**Valores típicos**:
- Valor por defecto: 8164 bytes

**Cómo ajustar**:

1. Reduzca gradualmente 08000, 7000, etc.
2. Después de cada cambio, pruebe la adquisición (botón Run) 5-10 veces
3. Si no aparecen más pantallas azules, el valor es correcto
4. Si persisten los pantallazos azules, disminuya aún más o pruebe a modificar el parámetro Nivel de latencia
```


---

```{list-table}
* - **Verificación final y guardado**
  - 19. Haga clic en **Run** al menos 2-3 veces consecutivas  
    20. Compruebe que:  
      - Ninguna imagen aparezca completamente azul o negra
      - Las imágenes se actualicen regularmente
      - La superficie del FlexiBowl® sea claramente visible
      - La iluminación sea uniforme
    21. Si todas las pruebas son positivas, la configuración es correcta
```

(troubleshooting_calib_cam)=
## Calibración de la cámara

### *Patrón no detectado*

```{warning}
**Error: "Unable to detect calibration pattern"**

Causa: El software no puede identificar el patrón de cuadrícula.

**Solución**
- Aumente el contraste (ajuste la exposición o la iluminación)
- Compruebe que toda la cuadrícula es visible en la imagen
- Mejore el enfoque
- Limpie la superficie de la cuadrícula (el polvo o las huellas dactilares pueden interferir)
- Compruebe que la cuadrícula es correcta (cuadrados, no círculos u otros patrones)
```

### *Calibración siempre "Mala" o "Aceptable"*

```{warning}
**Calidad de calibración insuficiente**

Si, a pesar de los ajustes, el calibrado sigue siendo inferior a "Excelente":

1. Compruebe la distancia de trabajo cámara-FlexiBowl® (debe ser la calculada)
2. Compruebe que la cámara es paralela al plano del FlexiBowl® (debe estar perfectamente horizontal)
3. Asegúrese de que la cámara está estable (sin vibraciones durante la adquisición)
4. Compruebe que el objetivo está completamente enroscado

Si el problema persiste, puede haber un problema mecánico en el montaje. Consulte [Instalación mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md) para su revisión.
```

### *Errores tras el cambio de iluminación*

```{tip}
**Recalibración tras cambio de backlight/toplight**

Al pasar de retroiluminación a iluminación (o viceversa):

1. La calibración geométrica sigue siendo válida (no es necesario rehacerla)
2. Sólo es necesario ajustar la exposición de la cámara para el nuevo tipo de iluminación
3. Adquirir una imagen de prueba para verificar que el patrón sigue siendo claramente visible

En general, conviene decidir desde el principio el tipo de iluminación que se va a utilizar y mantener esa configuración.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **La calibración falla (error de software)**
  - • La rejilla de calibración no se detecta correctamente
    
    • Iluminación insuficiente/excesiva
    
    • Rejilla de calibración dañada o sucia
    
  - • Coloque el objetivo plano y bien visible
    
    • Ajuste la exposición de la cámara para obtener una buena visión del objetivo
    
    • Utilice una rejilla de calibración limpia y sin daños
    
* - **Error de calibración demasiado alto**
  - • Cámara no perfectamente ortogonal a la superficie
    
    • Rejilla de calibración no plana
    
    • Distorsión óptica excesiva
    
  - • Compruebe la perpendicularidad de la cámara con un nivel (tolerancia ±1°)
    
    • Coloque el objetivo sobre una superficie rígida y plana
    
    • Compruebe la calidad de la lente óptica; límpiela o sustitúyala
    
* - **Las coordenadas reales no se corresponden con las medidas**
  - • Factor de escala incorrecto (Tile Size erróneo)
    
    • Cámara desplazada después de la calibración
    
  - • Repita la calibración completa
    
    • Fije firmemente la cámara para evitar desplazamientos
    
    • Compruebe las dimensiones del objetivo de calibración según la documentación
* - **Calibración válida solo en el centro de la imagen**
  - • Distorsión óptica periférica
    
    • Calibración con muy pocos puntos
  - • Utilice una lente de mayor calidad y baja distorsión
    
    • Compruebe que la distancia de trabajo es correcta
```



(troubleshooting_fb_setup)=
## Solución de problemas de la sección FlexiBowl® Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **FlexiBowl® no responde a los comandos del software**
  - • Dirección IP desconfigurada o incorrecta
    
    • FlexiBowl® no conectado en red
    
    • El cortafuegos bloquea la comunicación
    
    • FlexiBowl® no se enciende
  - • Compruebe y configure correctamente la IP en FlexiBowl® Setup
    
    • Pruebe la conexión con ping desde VisionController
    
    • Desactive temporalmente el cortafuegos para realizar pruebas
    
    • Compruebe el LED READY del FlexiBowl®
* - **No se puede guardar la configuración del FlexiBowl®**
  - • Disco lleno

  - • Libere espacio en disco
 
* - **Los parámetros FlexiBowl® no se aplican**
  - • El botón "Sincronizar parámetros" no está pulsado
    
    • Conexión FlexiBowl® perdida
    
    • FlexiBowl® en error
  - • Haga clic siempre en "Sincronizar parámetros" después de los cambios
    
    • Compruebe la estabilidad de la conexión Ethernet
    
    • Reinicie FlexiBowl®
* - **Asistente FlexiBowl® calcula parámetros incorrectos**
  - • Caracterización incorrecta del componente (geometría/comportamiento)
    
    • Modelo FlexiBowl® seleccionado incorrecto
    
    • Sentido de giro mal ajustado
  - • Revise la selección de geometría (FLAT/CYLINDRICAL/COMPLEX)
    
    • Compruebe el tamaño del FlexiBowl® instalado frente al seleccionado
    
    • Compruebe el sentido físico de giro y compárelo con el ajuste
```

(troubleshooting_hopper_setup)=
## Solución de problemas de la sección Hopper Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **La tolva nunca se activa automáticamente**
  - • La tolva no está habilitada en el software    
    • Campo de señal erróneo  
    • Área de control no definida  
    
    • Umbrales no calibrados  
    
    • Tolva no conectada eléctricamente
  - • Habilite la casilla de verificación "Habilitar Tolva X"  
    • Compruebe que el número **Señal** se corresponde con la DO conectada físicamente
    • Defina el área de control en "Definir comprobación de área"
    
    • Realice la calibración del umbral con CAPTURE vacía/llena
    
    • Compruebe las conexiones eléctricas
* - **La tolva se activa continuamente**
  - • Umbrales mal calibrados
    
    • Tiempo de vibración insuficiente (descarga muy pocas piezas)
    
    • Parámetro "Pasos" incorrecto
  - • Repita la calibración retirando TODAS las piezas para CAPTURE vacía
    
    • Aumente el parámetro "Tiempo" (p. ej.: de 500 ms a 700 ms)
    
    • Recalcule "Pasos" contando los ciclos reales
* - **Tolva de prueba siempre roja (no se activa)**
  - • Demasiados componentes en la zona durante el calibrado
    
    • Cambio de iluminación entre la calibración y la prueba
    
    • Reflejos/sombras en la zona de control
  - • Repita la calibración con el número mínimo correcto de piezas
    
    • Realice calibraciones y pruebas con iluminación estable
    
    • Reposicione el área excluyendo zonas con reflejos
* - **Tolva de prueba siempre verde (siempre activa)**
  - • El área de control incluye zonas irrelevantes
    
    • Calibrado en vacío realizado con piezas presentes
    
    • Expression Builder no se calcula correctamente
  - • Redefina un área de control más estrecha
    
    • Repita CAPTURE vacía asegurándose de limpiar completamente la zona
    
    • Haga clic de nuevo en AUTO para volver a calcular la media y la desviación estándar
* - **Flujo de componentes no uniforme**
  - • Cálculo incorrecto del tiempo de vibración  
    
    • Carga inicial demasiado elevada que supera la carga útil
  - • Revise el cálculo de vibraciones en función del llenado inicial 
    
    • Compruebe que la carga no supere la carga útil de la tolva
```

(troubleshooting_robot_setup)=
## Solución de problemas para la sección de configuración del robot

```{warning}
**Diagnóstico de conexión fallida**

Si el robot no puede establecer la conexión:

**Comprobaciones básicas**:
1. Servidor FlexiVision One en línea (indicador verde)
2. Dirección IP correcta en el programa del robot
3. Puerto correcto en el programa del robot (igual que FlexiVision One)
4. Cable Ethernet conectado correctamente

**Comprobaciones de la red**:
1. Ping desde el VisionController al robot:
   - Abra el símbolo del sistema en VisionController
   - `ping <IP_ROBOT>` (p. ej.: `ping 192.168.1.10`)
   - Si falla: problema de configuración de red física/IP

2. Ping desde el robot al VisionController (si está disponible la función ping en el robot)

3. Compruebe que el robot y VisionController están en la misma subred

**Comprobaciones del cortafuegos**:
1. Desactive temporalmente el cortafuegos de Windows para realizar pruebas
2. Si funciona, problema del cortafuegos → configurar excepción

**Verificaciones de robots**:
1. Compruebe la sintaxis correcta del comando de conexión TCP/IP (consulte el manual del robot)
2. Compruebe el tiempo de espera de la conexión (auméntelo si es necesario)
3. Compruebe los permisos de red en el controlador del robot
```

```{note}
**Estabilización de la conexión**

Si la conexión se interrumpe con frecuencia:

1. Compruebe la calidad del cable Ethernet (utilice Cat6 en adelante)
2. Evite los cables excesivamente largos
3. Compruebe que no haya un tráfico de red excesivo en la misma subred; pueden utilizarse programas como Wireshark o TCP dump
4. Compruebe la estabilidad de la alimentación del VisionController
5. Compruebe si hay errores de red en los registros de Windows

Si el problema persiste, póngase en contacto con el servicio de asistencia técnica para un análisis en profundidad.
```
```{warning}
**Sintaxis de comando incorrecta**

Si FlexiVision One responde con "Comando no válido":

1. Compruebe la sintaxis exacta del comando (distingue entre mayúsculas y minúsculas, guión bajo, etc.)
2. Asegúrese de enviar el carácter terminador CHR(13) después de cada comando
3. No añada espacios adicionales al principio o al final del comando
4. Compruebe en el registro de mensajes de la sección Configuración del robot el comando que recibió FlexiVision One

Ejemplos correctos frente a incorrectos:
- ✅ `start_Locator` (con guión bajo, minúsculas)
- ❌ `Start_Locator` (mayúsculas incorrectas)
- ❌ `start Locator` (espacio en lugar de guión bajo)
- ❌ `startLocator` (falta guión bajo)

Consulte [Protocolo TCP/IP](protocollo) para obtener la lista completa y correcta de comandos.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **El robot no se conecta a FlexiVision One**
  - • La dirección IP del robot no está en la misma subred que VisionController
    
    • Puerto TCP/IP no configurado
    
    • El cortafuegos de VisionController bloquea la comunicación
    
  - • Compruebe y configure la subred correcta en Configuración del robot
    
    • Configure el puerto TCP/IP (normalmente 5000 o segundo robot)
    
    • Desactive el cortafuegos para las pruebas
    
    • Seleccione el protocolo compatible con el robot en [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md)
* - **El robot se desplaza a posiciones erróneas**
  - • La calibración del robot no se ha realizado o no se ha realizado correctamente
    
    • Marco/herramienta del robot incorrectos
    
    • Desplazamiento incorrecto de la pinza
    
    • Coordenadas guardadas incorrectamente durante la configuración del modelo
  - • Realice la calibración completa del robot
    
    • Compruebe el bastidor y la herramienta seleccionados en el robot
    
    • Repita la calibración del Robot Pick con las coordenadas correctas
    
    • Vuelva a entrenar el modelo guardando coordenadas precisas
* - **Imposible conectar con el robot**
  - • Robot apagado
    
    • Cable Ethernet no conectado
    
    • Robot y VisionController en subredes diferentes

  - • Encienda el robot y póngalo en automático
    
    • Compruebe la conexión física Ethernet robot-VisionController
    
    • Configure el robot y VisionController en la misma red
```

