(dashboard)=
# **Monitorización de aplicaciones: Cuadro de mandos**

La **Dashboard** es la interfaz principal para la supervisión en tiempo real del sistema FlexiVision One. En esta página puede comprobar la eficacia del proceso, analizar los tiempos de ciclo, validar el reconocimiento de componentes e identificar posibles cuellos de botella en el sistema.


---

## Vista general de la interfaz

La interfaz del panel de control se divide en cuatro secciones principales:
![Página de configuración de Hooper](../../../../_shared/media/images/pagina_dashboard.png)
1. [**Control operativo**](controllooperativo): Comandos y estado de ejecución
2. [**Análisis de la visión**](analisivisione): Visualización de las piezas detectadas y detalles
3. [**Indicadores de resultados**](indicatoriperformance): Conectividad y tiempos de ciclo
4. [**Análisis gráfico**](analisigrafica): Gráficos históricos de productividad y tiempo

---
(controllooperativo)=
## Control operativo - Comandos y estado de ejecución

```{list-table}
:header-rows: 1
:widths: 25 75

* - Elemento
  - Descripción y función
* - **En ejecución**
  - Indicador de estado que muestra si el sistema se está ejecutando actualmente.  
    **Verde** 🟢: Sistema activo y operativo.  
    **Rojo** 🔴: Sistema parado o en pausa.
* - **En tiempo de ejecución**
  - Muestra el tiempo total de funcionamiento del sistema desde el inicio de la aplicación. 
* - **Selección de FlexiBowl®**
  - Menú desplegable para seleccionar el FlexiBowl® específico que se va a supervisar. 
* - **Test Locator**
  - Toma una foto del área de visión e inicia el reconocimiento de los componentes presentes. 
```

```{tip}
**Test Locator**
Útil para:
- Verificar que los componentes sean reconocidos efectivamente por el sistema de visión 
- En caso de colisión entre el robot y el componente, para comprobar la fiabilidad de las clearances
```

---
(analisivisione)=
## Análisis de la visión

El centro del cuadro de mandos muestra los datos de los componentes identificados por el sistema de visión.

### *Partes de Visión Detectadas*

**Partes de Visión Detectadas** muestra:
- Imagen adquirida en tiempo real por la cámara
- Un **gráfico histórico** de las detecciones de los últimos 30 segundos que muestra la evolución del número de piezas reconocidas por adquisición.


### *Tabla de modelos detectados*

**Detalle de los componentes reconocidos**

La tabla que aparece debajo de la imagen enumera todos los componentes del área de selección con los siguientes parámetros:

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Campo
  - Tipo de datos
  - Descripción
* - **Id**
  - Entero
  - Identificador único de componente progresivo (0, 1, 2, ...).   
  Id 0 = componente con la puntuación más alta (mejor coincidencia con el modelo si se ordena con Puntuación Descendente como se recomienda).
* - **X**
  - Milímetros
  - Coordenada X del componente.
* - **Y**
  - Milímetros
  - Coordenada Y del componente.
* - **Rot (Rotación)**
  - Grados
  - Ángulo de rotación del componente. 
* - **Puntuación**
  - Porcentaje
  - Valor porcentual (0,00-1,00 o 0%-100%) que expresa el grado de fiabilidad del reconocimiento. Representa la cercanía/fidelidad al modelo de referencia. Mayor puntuación = mejor coincidencia.
```

```{list-table} **Puntuación de interpretación**

* - **Puntuación > 0,90 (90%)**:
  - 
    - Correspondencia excelente con el modelo
    - Picking de alta confianza

* - **Puntuación 0,80-0,90 (80-90%)**:
  - 
    - Buena correspondencia
    - Picking seguro si Accept Threshold está configurado correctamente

* - **Puntuación 0,70-0,80 (70-80%)**:
  - 
    - Correspondencia aceptable
    - Verificar la consistencia a lo largo del tiempo

* - **Puntuación < 0,70 (< 70%)**:
  - 
    - Correspondencia deficiente
    - Si es recurrente, revisar el modelo o Accept Threshold.
```

---
(indicatoriperformance)=
## Indicadores de situación y resultados

### *Conectividad*

Indicadores de estado de comunicación con dispositivos externos:

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indicador
  - Descripción
* - **FlexiBowl®**
  - Estado de la conexión de hardware entre el VisionController (PC) y el FlexiBowl®.  
    **Verde**: Conectado y comunicando.  
    **Rojo**: Desconectado o error de comunicación.
* - **Robot**
  - Estado de la comunicación con el robot.   
    **Verde**: Conexión TCP/IP establecida.  
    **Rojo**: Desconectado o tiempo de espera de la comunicación.
```

```{warning}
**Acciones en caso de desconexión**

**FlexiBowl® rojo**:
- Compruebe el cable Ethernet FlexiBowl® → VisionController
- Compruebe la fuente de alimentación de FlexiBowl®
- Compruebe la IP de FlexiBowl® en FlexiBowl® Setup
- Intente reconectar o reiniciar el software

**Robot rojo**:
- Compruebe el cable Ethernet Robot → VisionController
- Compruebe que el robot tiene una conexión TCP/IP abierta
- Compruebe el puerto TCP/IP en la configuración del robot
- Compruebe el programa del robot (la dirección IP del VisionController y el puerto se han introducido correctamente en la sección de configuración del robot )

En producción, ambos indicadores deben estar siempre en verde.
```

### *Análisis del tiempo*

El sistema proporciona un desglose detallado de los tiempos de ciclo para identificar posibles cuellos de botella y optimizar el proceso.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Hora Elemento
  - Descripción
* - **Tiempo de procesamiento de la cámara**
  - Tiempo necesario para adquirir la imagen del sensor de la cámara. Incluye el tiempo de exposición y la transferencia de datos. 
* - **Tiempo de procesamiento del localizador**
  - Tiempo requerido por el algoritmo de visión para localizar y reconocer componentes en la imagen adquirida. Depende de: número de modelos activos, complejidad de los modelos, número de Clearances. 
* - **Procesamiento de visión total**
  - Suma de los tiempos de cámara y localizador. Representa el tiempo total que tarda el sistema de visión en procesar una imagen y enviar la(s) coordenada(s).       
* - **Tiempo total FlexiBowl®**
  - Tiempo que tarda el FlexiBowl® en realizar una secuencia de manipulación completa. 
* - **Tiempo total del Robot**
  - Tiempo estimado o detectado para la operación completa Pick & Place del robot. Incluye: aproximación → recogida → depósito → devolución. 
* - **Tiempo total de procesamiento**
  - Tiempo total de ciclo (Visión + FlexiBowl® + Robot). Representa el tiempo transcurrido desde el inicio de un ciclo hasta el inicio del siguiente. Determina la productividad máxima teórica (PPM).
```

```{tip}
**Interpretación de tiempos para optimización**

El gráfico temporal permite identificar el **cuello de botella** del sistema:

**Si el Procesamiento de visión total es el mayor**:
- Demasiados modelos activos → Desactivar modelos innecesarios
- Modelos demasiado complejos → Simplificar con un Umbral de puntuación más alto
- Demasiados Clearances → Reducir el número o el tamaño de los Clearances
- Procesamiento de cámara alto → Reducir el tiempo de exposición

**Si el Tiempo total FlexiBowl® es el mayor**:
- Demasiadas pausas → Optimice la sincronización Voltear/Mover y reduzca la pausa de estabilización (Pausa X ms)
- Secuencia de movimiento demasiado lenta → Aumente la velocidad en Config FlexiBowl®
- Ángulo de rotación excesivo → Reduzca el ángulo de movimiento
- Sacudida demasiado larga → Aumente la velocidad de Sacudida y reduzca los ciclos de Sacudida  

**Si el Tiempo total del Robot es el mayor**:
- Trayectoria del robot no optimizada → Optimizar la planificación de la trayectoria del robot
- Velocidad del robot demasiado baja → Aumentar la velocidad de movimiento (si es seguro)
- Distancia de depósito demasiado larga → Reposicionar el punto de depósito más cerca
- Tiempos de agarre demasiado largos → Optimizar la apertura/cierre de la pinza

**Objetivo de optimización**: Equilibrar los tres tiempos para reducir el tiempo total de procesamiento.
```

---
(analisigrafica)=
## Análisis gráfico

Los gráficos de la parte inferior del cuadro de mandos permiten realizar análisis predictivos y de diagnóstico del rendimiento del sistema a lo largo del tiempo.

### *1. Piezas por minuto (PPM)*

```{list-table}
* - **Gráfico de productividad**
  - Muestra la productividad media del sistema expresada en **componentes recogidos por minuto** (Parts Per Minute).

* - **Características**:
  - 
    - Eje X: Tiempo 
    - Eje Y: PPM (piezas/minuto)
    - Línea de tendencia: Media móvil para identificar tendencias

* - **Uso**:
  - 
    - Supervisar la estabilidad de la productividad a lo largo del tiempo
    - Identificar las degradaciones del rendimiento
    - Calcular el rendimiento real frente al teórico
```

```{tip}

  :::{list-table} **Interpretación de PPM**

    * - **PPM constante y estable**:
      - 
        ✓ Sistema bien configurado  
        ✓ Parámetros optimizados  
        ✓ Ningún cuello de botella crítico  

    * - **PPM en disminución progresiva**:
      -   
        ⚠️ Posible desgaste de componentes (superficie de agarre de FlexiBowl®)    
        ⚠️ Hopper que se vacía   
        ⚠️ Acumulación de suciedad en la cámara/iluminación    

    * - **PPM con fluctuaciones amplias**:
      - 
        ⚠️ Inestabilidad en el proceso  
        ⚠️ Problemas de reconocimiento intermitente  
        ⚠️ Interferencias externas (vibraciones, luz variable)  

    * - **Medidas correctivas**:
      - 
        - Analizar la correlación con los gráficos de tiempos
        - Identificar qué componente (Vision/FlexiBowl®/Robot) causa variaciones
        - Intervenir en parámetros específicos
  :::
```

### *2. Fill Hopper*

```{list-table}
* - **Gráfico de activaciones del Hopper**
  - Representa el historial de los impulsos de descarga enviados al Hopper.

* - **Características**:
  - 
    - Eje X: Tiempo
    - Eje Y: Activaciones de tolvas (eventos)
    - Picos: Cada pico representa una descarga de activación

* - **Uso**:
  - 
    - Comprobar la eficacia de la configuración de la tolva
    - Identificar anomalías en el comportamiento de la descarga
```

```{tip}
  
  :::{list-table} **Análisis del patrón de llenado de la tolva**

    * - **Activaciones regulares y constantes**:
      - 
        ✓ Configuración óptima del Hopper  
        ✓ Flujo de piezas estable y previsible  
        ✓ Autonomía calculable (ej.: activación cada 10 min)  

    * - **Activaciones cada vez más frecuentes**:
      - 
        ⚠️ El Hopper se está vaciando (menos piezas = más activaciones para mantener el nivel)  
        ⚠️ Tiempo de descarga insuficiente para el volumen reducido    
        **Acción**: Planificar la recarga del Hopper a corto plazo

    * - **Ninguna activación durante un periodo prolongado**:
      - 
        ⚠️ Robot detenido o ralentizado (las piezas no se consumen)  
        ⚠️ Posible problema del sistema que no solicita piezas    
        **Acción**: Verificar el estado de producción

    * - **Activaciones muy próximas (burst)**:
      - 
        ⚠️ Umbral del Hopper mal configurado (demasiado alto)  
        ⚠️ Steps insuficientes (las piezas no llegan a tiempo)  
        **Acción**: Revisar Config Hopper
  :::
```

### *3. Vision - FlexiBowl® - Robot (Cuadro comparativo)*

```{list-table} 
* - **Gráfico de tiempos superpuestos**
  - Gráfico comparativo de tres líneas que superpone los tiempos de cada proceso a lo largo del tiempo.

* - **Uso**: 
  - Identifique al instante qué proceso influye más en la duración total del ciclo y cómo varía con el tiempo.
```
---

## Control de calidad - Indicadores críticos que deben controlarse

```{list-table}
* - **Puntuación de los componentes**
  - Asegúrese de que la **Puntuación** de los componentes detectados esté constantemente por encima del umbral de tolerancia (Accept Threshold) configurado durante la configuración del modelo.

* - **Seguimiento de la puntuación**:
  - 
    - Comprobar periódicamente la tabla Modelos detectados
    - Comprobar que las puntuaciones típicas son de 0,85-0,95
    - Investigar si las puntuaciones caen por debajo de 0,80 con regularidad

* - **Puntuaciones gradualmente decrecientes**:
  - 
    ⚠️ Piezas reales diferentes de las del entrenamiento (variaciones de producción)  
    ⚠️ Iluminación cambiada (luz de fondo más débil, suciedad)  
    ⚠️ Cámara desenfocada (vibración, golpes)  
    ⚠️ Superficie FlexiBowl® sucia (patrón de interferencia)  

* - **Medidas correctivas**:
  - 
    - Limpie la cámara, la iluminación y la superficie del FlexiBowl®
    - Compruebe el enfoque de la cámara
    - Considere la posibilidad de volver a entrenar el modelo si las piezas han cambiado
    - Reduzca el umbral de aceptación si las puntuaciones siguen siendo fiables pero más bajas
```
---

## Buenas prácticas de supervisión de la producción

### *Comprobaciones diarias*

```{list-table}
* - **Al inicio de la producción** (5 minutos):
  - 
    - Verificar los indicadores de conectividad de FlexiBowl® y Robot (verdes)
    - Comprobar que los primeros ciclos muestren puntuaciones normales (>0,85)
    - Observar que el PPM se estabilice en el valor esperado

* - **Durante la producción** (comprobar cada 1-2 horas):
  - 
    - Eche un vistazo a los PPM para comprobar la estabilidad
    - Compruebe la tolva de llenado para predecir el llenado necesario
    - Compruebe el registro de errores o advertencias

* - **Al final del turno** (2 minutos):
  - 
    - Anote el PPM medio del turno
    - Compruebe el número de activaciones de la tolva
    - Compruebe si hay anomalías o eventos
    - Compare con los datos del día anterior
```
Esta rutina mínima garantiza una rápida identificación de los problemas y mantiene la trazabilidad del rendimiento.

### *Informe de resultados*  

```{tip} **Métricas clave que deben hacerse un seguimiento**
Para evaluar el rendimiento a lo largo del tiempo, haga un seguimiento:

  :::{list-table} 

    * - **Diariamente**:
      - 
        - PPM medio del turno
        - Número total de piezas recogidas
        - Número de activaciones de Hopper
        - Tiempo de inactividad total (y causas)

    * - **Semanalmente**:
      - 
        - Tendencia de PPM (¿aumenta/disminuye?)
        - Comparación entre PPM teórico y real
        - Puntuación media de los componentes detectados
        - Posibles modificaciones de configuración y su impacto

    * - **Mensualmente**:
      - 
        - Eficiencia general de los equipos (OEE)
        - Análisis de los principales cuellos de botella
        - Necesidad de mantenimiento predictivo
        - Retorno de la inversión (ROI) del sistema
  :::

Estos datos permiten una optimización continua y justifican la inversión en mejoras.
```

---

```{raw} html
<div style="border: 2px solid #0d6efd; border-radius: 12px; padding: 2rem; margin: 1.5rem 0; background-color: #f0f6ff; display: flex; align-items: flex-start; gap: 2rem;">
  <div style="flex: 1; min-width: 0;">
    <div style="font-size: 1.2rem; font-weight: 700; color: #0d6efd; margin-bottom: 0.5rem;"> ¡El sistema ya está operativo!</div>
    <div style="font-size: 0.95rem; color: #444; line-height: 1.6;">¡Enhorabuena! El sistema FlexiVision One ya está completamente configurado, optimizado y validado para la producción.</div>
  </div>
  <div style="flex: 1.4; background: white; border-radius: 8px; padding: 1.2rem 1.5rem; border: 1px solid #d0e4ff; font-size: 0.88rem; color: #333; line-height: 1.8;">
    <div style="font-weight: 600; margin-bottom: 0.5rem;">Resumen del recorrido completado:</div>
    <div>✓ Configuración de hardware (FlexiBowl®, Robot, Cámara)</div>
    <div>✓ Calibración completa (Cámara, Robot)</div>
    <div>✓ FlexiBowl® configurado para una manipulación óptima</div>
    <div>✓ Hopper configurado para alimentación automática (si está presente)</div>
    <div>✓ Modelos de pieza creados y optimizados</div>
    <div>✓ Sistema validado con monitorización mediante cuadro de mandos</div>
    <div>✓ Rendimiento verificado y estable</div>
    <div style="margin-top: 0.8rem; font-style: italic; color: #555;">El sistema está listo para operar en producción con supervisión mínima.</div>
  </div>
  <div style="flex: 0.7; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.9rem;">
    <div style="color: #555; font-weight: 600;">Últimas herramientas útiles:</div>
    <a href="../TROUBLESHOOTING/26_trb_shooting_guide.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Troubleshooting</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Guía de solución de problemas comunes</div>
    <a href="../27_Support.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Support</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Contactos de soporte técnico</div>
  </div>
</div>
```
