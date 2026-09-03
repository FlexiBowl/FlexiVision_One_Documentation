(calibrazione)=
# **Calibración de la cámara y el robot**

La calibración es el paso crucial que establece la relación geométrica exacta entre el mundo real (coordenadas en milímetros) y la imagen captada por la cámara (píxeles). Sin una calibración precisa, la precisión del sistema de picking se ve comprometida, lo que hace que toda la aplicación no sea fiable.


:::{tip}
No es necesario volver a calibrar si se altera la posición del FlexiBowl®.
:::
---

## ¿Por qué es necesaria la calibración?

La calibración es necesaria porque cada combinación de sensor y objetivo introduce alteraciones específicas en la imagen. Su principal objetivo es corregir estas distorsiones.

### *Tipos de distorsiones ópticas*

```{figure} ../../../../../_shared/media/images/distorsioni_new.png
:alt: Tipos de distorsiones ópticas
:width: 80%
:align: center

Ejemplos de distorsiones ópticas: sin distorsión (izquierda), distorsión de barrilete (centro), distorsión de cojinete (derecha)
```

---


## Paso 1: La rejilla de calibración

:::{error}
Asegúrese de tener: 
- Backlight encendido (SETUP > FlexiBowl® Setup > Config FlexiBowl® > Light ON activo)
- Toplight apagado
:::

:::{video} ../../../../../_shared/media/videos/Step1_calib.mp4
    :width: 100%
    :align: center
:::

La rejilla de calibración ARS específica debe colocarse en el FlexiBowl®:

````{list-table}
:widths: 10 50 40
:header-rows: 1

* - Paso
  - Operación
  - Imagen
* - **0**
  - Si están presentes, retire los desviadores montados en el FlexiBowl®.
  - ```{image} ../../../../../_shared/media/images/rimuoveredeviatori.jpg
      
    ```
* - **1**
  - **Afloje los cuatro tornillos** de la brida central del FlexiBowl®.
  - ```{image} ../../../../../_shared/media/images/rimuovereflangia.jpg
      
    ```
* - **2**
  - **Gire ligeramente la brida** central en sentido antihorario y **retírela**.
  - 
* - **3**
  - **Levante con cuidado** y **retire la superficie**.
  - ```{image} ../../../../../_shared/media/images/rimuoveredisco.jpg
      
    ```
* - **4**
  - En caso necesario, coloque separadores magnéticos en los cuatro lados de la rejilla.
  - ```{image} ../../../../../_shared/media/images/aggiungerespacer.jpg
      
    ```
* - **5**
  - **Coloque la rejilla ARS** en el FlexiBowl® alineando las clavijas de posicionamiento con los orificios predefinidos en el borde de la retroiluminación.
  - ```{image} ../../../../../_shared/media/images/posizionaregriglia.jpg
      
    ```
````

```{figure} ../../../../../_shared/media/images/griglia_su_flexibowl.png
:alt: Posicionamiento de la rejilla de calibración
:width: 60%
:align: center

Colocación correcta de la rejilla de calibración ARS en el FlexiBowl®
```
:::{attention} 
 La rejilla de calibración debe colocarse **a la misma altura que el objeto** utilizado en la aplicación.
 
   Por esta razón, se suministra con **separadores** que deben insertarse en las clavijas de la rejilla antes de instalarla en el FlexiBowl®.
   Los separadores tienen la función de **elevar la rejilla** hasta el nivel de la altura de la pieza, garantizando una calibración precisa.
  ![Separadores](../../../../../_shared/media/images/distanziali_griglia.JPG)
  
  ```{figure} ../../../../../_shared/media/images/altezzacalibrazione.png
    :width: 100%
    :align: center
  ```
:::

## Paso 2: Ajustes fundamentales

```{list-table}

* - **5**
  - Acceda a la sección Camera SETUP desde la sección SETUP 
* - **6**
  - Haga clic en el botón Config Camera de la cámara correspondiente 
* - **7**
  - Haga clic en EXPERT desde la página Camera FLB 
* - **8**
  - **Ponga la cámara en modalidad "live display"**
      Antes de ajustar la apertura, active el modo de visualización continua:
      :::{figure} ../../../../../_shared/media/images/livedisplay.jpg
    :width: 100%
    :align: center
    :::
* - **9**
  - **Ajuste el diafragma**
    - Desenrosque ligeramente el tornillo del anillo superior de la cámara 
    - Gire el anillo mientras observa la imagen en directo hasta que entre la cantidad adecuada de luz en la cámara 
    - Apriete el tornillo del anillo superior de la cámara 

    :::{figure} ../../../../../_shared/media/images/Esp_Corretta.png
    :width: 100%
    :align: center
    :::
* - **10**
  - **Ajuste manualmente el enfoque de la cámara**
    - Afloje ligeramente el tornillo del anillo inferior de la cámara
    - Gire el anillo lentamente mientras observa la imagen en directo
    - Cuando el patrón aparezca nítido, el enfoque es correcto
    - Apriete el tornillo del anillo inferior de la cámara 
    - Cierre la pantalla
    :::{figure} ../../../../../_shared/media/images/Fuoco_Corretto.png
    :width: 100%
    :align: center
    :::
* - **11**
  - Haga clic en Back 
```

```{warning}
**Atención a la profundidad de campo**

El enfoque debe garantizar la nitidez en **toda la superficie** del FlexiBowl®, no solo en el centro.

Si el centro es nítido pero los bordes están borrosos:
- Compruebe que la óptica está limpia
- Compruebe que la distancia de trabajo es correcta
- Compruebe que la cámara está perfectamente paralela a la superficie de trabajo del FlexiBowl®
- Cierre ligeramente el diafragma para aumentar la profundidad de campo

Si el problema persiste, puede ser necesario revisar el montaje mecánico de la cámara.
```
:::{video} ../../../../../_shared/media/videos/Step2b_calib.mp4
    :width: 100%
    :align: center
:::

:::{error}
Si al hacer clic varias veces en el botón RUN aparece aunque sea una vez una pantalla completamente azul, consulte [Troubleshooting Camera Setup](schermo_blu)
:::


```{list-table}
* - **12** 
  - **Ajuste la exposición de la cámara**
    - Desde la página **Camera FLB x**, localice el parámetro **Cam Exposure** (Exposición de la cámara):
    - Ajuste el parámetro "Cam Exposure" y haga clic en <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">; repita este paso hasta encontrar la exposición adecuada para la imagen: 
   		- Patrón de la rejilla claramente visible (negro sobre blanco o viceversa)
   		- Contraste elevado entre cuadrados blancos y negros
   		- Sin sobreexposición (áreas completamente blancas "quemadas")
   		- Sin subexposición (imagen demasiado oscura)
* - **13** 
  - Haga clic en NEXT
```

```{figure} ../../../../../_shared/media/images/Esposizioni.png
:alt: Esempio esposizione corretta
:width: 60%
:align: center

Ejemplo de exposición correcta: alto contraste, patrón bien definido, sin áreas quemadas
```

```{tip}
**Optimización de la exposición**

**Cuanto mayor sea el tiempo, más luz entrará en la óptica**

- **Tiempo demasiado breve**: Imagen oscura, patrón poco visible
- **Tiempo demasiado largo**: Imagen sobreexpuesta, pérdida de detalle
- **Tiempo óptimo**: Máximo contraste sin saturación
```
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::


## Paso 3: Calibración de la cámara

:::{video} ../../../../../_shared/media/videos/Step3_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
:widths: 5 95

* - **14**
  - Compruebe que la rejilla esté centrada, nítida y totalmente visible antes de adquirir la imagen de calibración.
* - **15**
  - Haga clic en "Grab Image" para tomar una fotografía de la rejilla de calibración.
    
    Verifique visualmente que:
    - Toda la rejilla sea visible
    - El patrón sea nítido
    - No haya sombras ni reflejos

* - **16**
  - Ajuste los valores "Tile Size X" y "Tile Size Y" ambos a 10 para todos los modelos FlexiBowl® 500 a 1200.  
     **Para los modelos FlexiBowl® 200 y FlexiBowl® 350, en cambio, ajuste los tile sizes a 2,5.**

* - **17**
  - Haga clic en "Calibrate" para realizar la calibración

* - **18**
  - **Evalúe la calidad de la calibración**
    
    El parámetro "Result Calibration" devolverá un valor:
    
    🟢 **Excellent (Verde)**: Calibración excelente, precisión óptima. 
    
    🟠 **Acceptable (Naranja)**: Calibración aceptable, precisión buena pero no óptima.
    
    🔴 **Bad (Rojo)**: Calibración deficiente, precisión insuficiente. Debe repetirse obligatoriamente.
    
    :::{important}
    Acepte solo calibraciones Excellent 🟢; otros resultados comprometerán el funcionamiento de toda la aplicación.
    :::

```

```{note}
**Criterio de aceptabilidad**

Un resultado satisfactorio incluye ajustar el diafragma, enfocar y establecer la mejor exposición para la aplicación.

```

```{warning}
**Errores durante el cálculo**

Si falla el cálculo de la calibración:

**Posibles causas**:
- Patrón no detectado (imagen demasiado oscura o sobreexpuesta)
- Cuadrados de la rejilla parcialmente oscurecidos
- Distorsión excesiva (cámara demasiado cerca o lejos)
- Tile Size introducido incorrectamente

**Solución**:
- Compruebe y mejore la calidad de la imagen adquirida
- Asegúrese de que toda la rejilla sea visible y esté bien iluminada
- Compruebe el valor Tile Size
- Repita la adquisición de la imagen (Grab Image) e inténtelo de nuevo
```

:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::



---

### *Cuándo es necesario repetir la calibración*
```{list-table}
:widths: 50 50
:header-rows: 0

* - **Recalibrar cuando:**
  - Primera configuración del sistema (obligatoria). Después de cambiar la posición de la cámara. Después de mover el robot. Si se detectan errores sistemáticos de picking.

* - **No es necesario recalibrar cuando:**
  - Si cambia el tipo de pieza para el mismo FlexiBowl® y cámara. Si modifica el enfoque o la apertura del objetivo. Si cambia la receta del software. Si ajusta los parámetros de reconocimiento. Si actualiza los programas del robot.
```

---
# **Calibración del robot**

## Paso 4: Montaje del láser

:::{video} ../../../../../_shared/media/videos/Step4_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **19** 
  - Una vez obtenida una calibración de excelente calidad, haga clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">.  
  
    Aparecerá una ventana que solicita la calibración del robot antes de continuar; **NO** haga clic en "Sí" y siga los pasos siguientes
* - **20** 
  - Monte el Laser Tool con su soporte personalizado 
    :::{important}
    El soporte para montar el Instrumento Láser en lugar de la herramienta del robot **NO** se suministra, ya que varía para cada robot y debe personalizarse.
    :::
    :::{figure} ../../../../../_shared/media/images/step1calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **21**
  - Coloque el Spacer Bracket (**A**) debajo del láser 
    :::{figure} ../../../../../_shared/media/images/step2calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **22**
  - Baje el láser hasta el nivel del spacer (**A**), de modo que el láser quede a exactamente 3 cm de la rejilla de calibración
    :::{image} ../../../../../_shared/media/images/spacerbracket.png
    :align: center 
    :width: 75%
    :::
* - **23**
  - Retire el Spacer Bracket 
    :::{figure} ../../../../../_shared/media/images/step3calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **24**
  - Encienda el láser 
    :::{figure} ../../../../../_shared/media/images/step4calrobot.jpg
    :width: 30%
    :align: center
    :::
```

:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::


## Paso 5: Dibujar un plano de 3 puntos

:::{video} ../../../../../_shared/media/videos/Step5_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **25**
  - Lleve el láser al punto de origen 
  - :::{figure} ../../../../../_shared/media/images/origine.jpg
    :width: 100%
    :align: center
    :::
* - **26**
  - Lleve el láser al punto final del eje X
  - :::{figure} ../../../../../_shared/media/images/assex.jpg
    :width: 100%
    :align: center
    :::
* - **27**
  - Lleve el láser al punto final del eje Y 
  - :::{figure} ../../../../../_shared/media/images/assey.jpg
    :width: 100%
    :align: center
    :::
```

:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::


## Paso 6: Verificación de la trayectoria del robot

:::{video} ../../../../../_shared/media/videos/Step6_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **28** 
  - Vuelva a llevar el láser al punto de origen
* - **29**
  - Mueva el robot desde su teach pendant a lo largo de los ejes X e Y. 
* - **30**
  - Verifique que se sigue la trayectoria correcta: el robot, moviéndose exclusivamente a lo largo de los ejes X e Y, debe seguir correctamente las líneas de la rejilla 
* - **31**
  - Haga clic en "YES"
    :::{figure} ../../../../../_shared/media/images/clickyes.jpg
    :width: 50%
    :align: center
    :::
```
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::


## Paso 7: Guardado de la receta base
```{list-table}
:header-rows: 0
:widths: 10 90

* - **32**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">

* - **33**
  - Compruebe que tiene seleccionada la receta que contiene todas las configuraciones y calibraciones en el menú de la izquierda y haga clic en <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon">

* - **34**
  - Esto nos permitirá tener guardados por separado todos los pasos dados hasta el momento, de forma que tendremos una base para todas las futuras recetas que contengan los distintos modelos para el sistema calibrado

* - **35**
  - Para continuar con la creación de modelos, duplique la receta base, renómbrela como prefiera y haga clic en <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">: se abrirá una página con la lista de todos los modelos disponibles
```
---

# **Problemas comunes durante la calibración**

## Patrón no detectado

```{warning}
**Error: "Unable to detect calibration pattern"**

Causa: El software no puede identificar el patrón de la rejilla.

**Soluciones**:
- Aumente el contraste (ajuste la exposición o la iluminación)
- Compruebe que toda la rejilla sea visible en la imagen
- Mejore el enfoque
- Limpie la superficie de la rejilla (el polvo o las huellas dactilares pueden interferir)
```

## Calibración siempre "Bad" o "Acceptable"

```{warning}
**Calidad de calibración insuficiente**

Si, a pesar de los ajustes, la calibración sigue por debajo de "Excellent":

1. Compruebe la distancia de trabajo cámara-FlexiBowl® (debe ser la calculada)
2. Compruebe que la cámara es paralela al plano del FlexiBowl® (debe estar perfectamente horizontal)
3. Asegúrese de que la cámara está estable (sin vibraciones durante la adquisición)
4. Compruebe que el objetivo está completamente enroscado 

Si el problema persiste, puede haber un problema mecánico en el montaje. Consulte [Instalación mecánica](../../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md) para su revisión.
```
---

## Próximos pasos

Una vez finalizadas las calibraciones de la cámara y del robot, proceda con:

- [FlexiBowl® Setup](fbsetup)
- [Hopper Setup](13b_Hopper_Setup.md)
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Guardar la receta](ricettabase)








