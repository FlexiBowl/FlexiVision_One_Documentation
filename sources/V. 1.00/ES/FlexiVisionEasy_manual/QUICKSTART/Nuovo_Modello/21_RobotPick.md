(robotpick)=
# **Calibración Robot Pick**
En esta página veremos cómo enlazar las coordenadas de la visión con las del robot para permitir un picking preciso de los componentes.


**¿Qué es Robot Pick?**
La función **Robot Pick** calcula el desfase entre las coordenadas detectadas por FlexiVision One y las coordenadas reales del robot, lo que permite al robot recoger los componentes en la posición correcta.
```{danger}
**¡Coordenadas fundamentales del robot!**

Esta fase requiere **OBLIGATORIAMENTE** las coordenadas X, Y, Rz guardadas durante la preparación física de la configuración (Paso 1 de la sección Clearances).

Sin estas coordenadas, no se puede completar el calibrado. Si se pierden o se olvidan, será necesario repetir toda la preparación física con el robot.
```
---

## Visión general de la interfaz de Robot Pick

Tras hacer clic en "Siguiente" en la página de Clearances, se abre la página **Robot Model Pick**.

![Página Robot Pick](../../../../../_shared/media/images/pagina_robotpick.png)

|Sección | Parámetro | Función |
|-----------|-----------|----------|
| Activar | **Activar Robot Pick** | Activa la calibración del robot |
|Visión Resultado| **X cordón** | Coordenada X detectada por visión |
|Visión Resultado| **Cordón Y** | Coordenada Y detectada por visión |
|Visión Resultado| **Cordón RZ** | Rotación Z detectada por visión |
|Insertar coordenadas del robot| **X cordón** | Coordenada X del robot (a insertar) |
|Insertar coordenadas del robot| **Cordón Y** | Coordenada Y del robot (a insertar) |
|Insertar coordenadas del robot| **Cordón RZ** | Rotación Z del robot (a insertar) |


| Función | Descripción |
|----------|-------------|
| **Buscar objeto** | Detectar el componente y mostrar las coordenadas |
| **Desplazamiento de selección** | Calcula el desplazamiento para la recogida correcta |

---

## Paso 1: Activación y detección de componentes

:::{video} ../../../../../_shared/media/videos/Step1_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - Haga clic en **Activar Robot Pick**
* - **2**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_FIND_OBJECT1.png" class="inline-icon">:
      - El sistema detectará el componente de referencia
      - Las coordenadas aparecerán en la sección **Resultado de Visión**

      :::{note} Visión Resultado:
      Estas son las coordenadas que FlexiVision One "ve" en la imagen. Aún no están conectadas al sistema de coordenadas del robot.
      :::
```
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::

## Paso 2: Entrada de coordenadas del robot y cálculo del desplazamiento

:::{video} ../../../../../_shared/media/videos/Step2_robot.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **3**
  - En la casilla **Insertar coordenadas del robot**, introduzca las coordenadas guardadas al crear el modelo:
      - **X cordón** → Coordenada X anotada en el paso 1 de [Creación de Clearances](setupclearances)
      - **Cordón Y** → Coordenada Y anotada en el paso 1 de [Creación de Clearances](setupclearances)
      - **Cordón RZ** → Rotación Z anotada en el paso 1 de [Creación de Clearances](setupclearances)

      :::{danger}
      Utilice las coordenadas guardadas durante la configuración del modelo. ¡Sin estas coordenadas, la calibración será errónea!
      Las coordenadas deben introducirse con **máxima precisión**:
      - Copie los valores exactamente como anotados (incluidos los decimales)
      - **NO aproxime** (p. ej.: 450.23 ≠ 450.2 ≠ 450)
      - Verifique que no ha intercambiado X e Y
      - Compruebe el signo (+ o -) de cada coordenada

      **Los errores en esta fase provocan desplazamientos del robot completamente erróneos**, lo que da lugar a intentos de recogida en posiciones equivocadas (incluso decenas de centímetros de error). La inobservancia de estos dos puntos podría provocar colisiones del robot que dañarían el FlexiBowl®, los componentes o el propio robot.
      :::
* - **4**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_GRIPPER_OFFSET.png" class="inline-icon">
      - El sistema calculará automáticamente la transformación entre las coordenadas de visión y las coordenadas del robot
      - Este desplazamiento se aplicará a todos los levantamientos futuros
```
---
```{admonition} **¿Cómo funciona el Gripper Offset?**
:class: info
El sistema compara:
- **Coordenadas de visión**: donde FlexiVision One "ve" el origen del componente
- **Coordenadas del robot**: donde el robot agarró realmente el componente

Calcula la diferencia y la almacena como **offset**. Este desplazamiento se aplicará a todos los componentes detectados en el futuro, garantizando que el robot siempre recoja en la posición correcta.
```
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::
---

## Paso 3: Finalizar y guardar
```{list-table}
* - **5**
  - Haciendo clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">, volveremos a la página de las recetas <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
* - **6**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon"> para guardar toda la configuración

      :::{admonition} Guardado completo
      :class: success
      El guardado incluye:
      - ✓ Modelo creado
      - ✓ Área de trabajo (ROI)
      - ✓ Tolerancias (Accept Threshold)
      - ✓ Clearances configuradas
      - ✓ Calibración del robot (Gripper Offset)
      :::
```

---

## Modelos múltiples - Añadir más modelos

### *Paso 4: Modelos adicionales (opcional)*
```{list-table}
* - **7**
  - Para crear modelos adicionales en la misma receta:
      - Vuelva a <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
      - Seleccione un nuevo modelo aún no configurado
      - Repita todo el procedimiento desde [Creación de modelos](nuovomodello)

      :::{tip}
      Cada modelo en la receta puede tener configuraciones diferentes (ROI, clearance, offset), lo que permite gestionar componentes con características distintas en la misma aplicación.
      :::
```

```{seealso}
Para cualquier problema en los pasos recién completados, consulte [Solución de problemas](troubleshooting)
```

---


