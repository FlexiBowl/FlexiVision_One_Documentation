# **Creación de recetas y modelos - Visión general**

Esta sección guía al usuario a través del proceso completo de creación de una receta de aplicación y de los modelos de piezas necesarios para el reconocimiento y la recogida por parte del robot.

```{note}
**Requisitos previos**

Antes de proceder a la creación de recetas y modelos, asegúrese:
- Todas las configuraciones de hardware se han completado ([Configuración de componentes](setupcomponenti))
- La calibración de la cámara se ha realizado correctamente ([Calibración de la cámara](calibrazione))
- La calibración del robot se ha completado
- Las piezas físicas que se van a reconocer están disponibles
```

---

## Receta vs. Modelo: Diferencias fundamentales

Antes de empezar, es importante entender la diferencia entre **Receta** y **Modelo**:

```{list-table}
   :widths: 50 50
   :header-rows: 1

   * - ¿Qué es una receta?
     - ¿Qué es un modelo?
   * - El contenedor global de toda la aplicación de picking.
     - La definición específica de un único componente que debe reconocerse.
   * - Incluye hasta 8 modelos, parámetros FlexiBowl®, tolvas y lógicas de comunicación.
     - Incluye imágenes de entrenamiento, ROI, características visuales, filtros y desplazamientos del robot.
   * - Gestiona los parámetros de hardware (vibración, velocidad) y de red (puerto TCP/IP, tiempo de espera).
     - Gestiona los parámetros de visión (umbral, puntuación mínima) y las coordenadas de recogida (pinza).
   * - Puede tratar varios tipos de piezas simultáneamente (multimodelo).
     - Centrado en un patrón visual específico.
```


```{tip}
Una receta puede contener hasta 8 modelos diferentes, lo que permite al robot reconocer y recoger distintos tipos de piezas de la misma aplicación sin cambiar la configuración.
```


---

## Resumen completo del proceso

El proceso de creación de una receta completa y funcional consta de varios pasos secuenciales:

```{figure} ../../../../../_shared/media/images/newmodel4.jpg
:alt: Flujo de trabajo de creación de recetas y modelos
:width: 100%
:align: center

Esquema completo del proceso de creación de recetas y modelos
```

### *Etapas principales*

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Paso
  - Nombre
  - Descripción
* - **1**
  - Creación de la receta
  - Definición de la receta de aplicación con el nombre, tipo y FlexiBowl® utilizado
* - **2**
  - Preparación física
  - Posicionamiento de la pieza de referencia en el área de visión
* - **3**
  - Training del modelo
  - Adquisición de la imagen y creación del patrón de reconocimiento
* - **4**
  - Definición del ROI
  - Definición del área de búsqueda donde buscar las piezas
* - **5**
  - Ajuste del filtro
  - Configuración del umbral de aceptación y tolerancias de reconocimiento
* - **6**
  - Preparación física
  - Simulación de picking con robot para posicionar los objetos que simularán la huella de la pinza
* - **7**
  - Memorización de coordenadas
  - Memorización de las coordenadas del robot en la posición de picking del componente de referencia
* - **8**
  - Creación de Clearances
  - Definición de las zonas que deben permanecer libres (zona de pinza, obstáculos)
* - **9**
  - Coordenadas del robot
  - Cálculo del offset de la pinza para un picking correcto
* - **10**
  - Prueba y validación
  - Comprobación completa del funcionamiento y guardado de la receta
```

---

## Secciones detalladas de la guía de navegación

Para obtener información completa sobre cada paso del proceso, consulte las secciones correspondientes:

- **[Crear una nueva receta](nuovaricetta)** - Cómo crear y configurar una nueva receta
- **[Training modelo](nuovomodello)** - Adquisición de imágenes y creación de patrones
- **[Definición de ROI y filtros](roitest)** - Configuración del área de búsqueda y tolerancias
- **[Creación de Clearances](istogrammi)** - Definición de áreas libres
- **[Coordenadas de recogida del robot](robotpick)** - Cálculo del desplazamiento de la pinza

---

## Consejos prácticos antes de empezar

### *Preparación del material*

```{tip}
**Checklist de preparación**

Antes de empezar a crear modelos, prepárese:

- Al menos 10-20 piezas del tipo que se desea reconocer (con fines de prueba)
- Piezas limpias y en buen estado (representativas de la producción)
- Simuladores del tamaño de la pinza (NO deben ser piezas del mismo tipo, ya que es importante no confundirlas con la pieza de referencia.)
- Hoja para anotar las coordenadas del robot (X, Y, RZ)
- FlexiBowl® vacío y limpio
- Backlight/Toplight encendidos
```

### *Entorno óptimo*

```{note}
**Condiciones ideales para el training**

- Iluminación estable (evitar la luz solar directa variable)
- FlexiBowl® estacionario
- Robot en posición segura (no debe interferir durante las adquisiciones)
- Software FlexiVision One abierto y base de recetas cargada
```

### *Errores comunes que hay que evitar*

```{error}
**Evitar estos errores frecuentes**

❌ **No guardar las coordenadas del robot** durante la preparación física → imposible calcular el desplazamiento de la pinza

❌ **Desplazar la pieza** después de guardar las coordenadas → desplazamiento erróneo

❌ **Umbral de características demasiado bajo** → modelo demasiado detallado, reconoce la textura de la superficie

❌ **ROI demasiado estrecha** → no se detectan las piezas de los bordes

❌ **Clearances demasiado pequeñas** → colisiones de la pinza con piezas adyacentes

❌ **No realizar pruebas con varias piezas** → los problemas no se detectan hasta la producción

Siga cuidadosamente los procedimientos detallados en las siguientes secciones para evitar estos problemas.
```

---

## Apoyo y recursos adicionales

```{note}
**Los botones INFO**
En cada una de las secciones operativas, está disponible un botón INFO en la parte superior derecha.
Dentro de este botón está disponible la explicación del procedimiento Step By Step; el mismo procedimiento puede verse en el videotutorial.

- [**Completos tutoriales en vídeo**](vidtutcompleti)
- **Asistencia técnica**: [support@arsautomation.com](mailto:support@arsautomation.com) para asistencia

Para problemas específicos al crear modelos, consulte [Solución de problemas](troubleshooting).
```

---

## Próximos pasos

Una vez comprendida la visión general del proceso, proceda a la creación propiamente dicha:

**→ [Comienza: Crear una nueva receta](nuovaricetta)**


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```
