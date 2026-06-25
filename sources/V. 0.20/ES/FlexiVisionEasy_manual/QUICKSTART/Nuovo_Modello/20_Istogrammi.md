(istogrammi)=
# **Las Clearances** 
 En esta página veremos cómo configurar las Clearances para verificar que las áreas críticas estén libres de obstáculos.

 **¿Qué es una Clearance?**  
Una **Clearance** en FlexiVision One es una herramienta que supervisa un área específica de la imagen para verificar que está despejada. Sirve para comprobar, por ejemplo, que el espacio necesario para que la pinza agarre el componente no está ocupado por otros objetos.
````{note} Principio de funcionamiento.

La Clearance analiza los cambios en los niveles de gris en un área definida:
- 🟢 **Verde** → Zona libre (OK para la recogida)
- 🔴 **Rojo** → Zona ocupada (presencia de obstáculos)
````
:::{attention}
El uso de las Clearances varía en función de la pieza que se vaya a modelar. Se trata de una evaluación que debe realizar la persona encargada de crear la aplicación. 
:::
--- 
(setupclearances)=
## Paso 1: Configuración física

:::{danger} **¡Atención!**
  Le mostraremos el procedimiento con la Herramienta Pinza, ya que requiere obligatoriamente la configuración de Clearances para los modelos. Otras herramientas robóticas pueden no necesitar las Clearances para simular la huella. 
:::
:::{video} ../../../../../_shared/media/videos/Step1.mp4
    :width: 100%
    :align: center
:::
````{list-table}
:widths: 5 95

* - **1**
  - Desde la **botonera del robot**:
    - Seleccionar el **frame** y el **tool** calibrado en FlexiVision One
    - Llevar el **último eje** de la herramienta a **rotación cero** (Rz = 0°)
* - **2**
  - Simular un agarre:
    - Abrir la pinza
    - Acercar la herramienta del robot al componente a nivel de la superficie, como para agarrarlo
* - **3**
  - Colocar **dos objetos** a los lados de la pinza para disponer, una vez retirado el robot, de las zonas libres entre el componente de referencia y los dos objetos.  
  Representarán las áreas de huella de la pinza del robot. 
    
    :::{important}
    Deje los objetos ligeramente más separados de lo necesario para evitar errores en la creación del modelo. (margen 2-3 mm)
    :::
    
* - **4**
  - Anotar las coordenadas:
    - Guardar las coordenadas del último eje del robot:
      - **X** (coordenada X)
      - **Y** (coordenada Y)
      - **Rz** (rotación alrededor de Z)
    
    :::{important}
    ¡Anote estas coordenadas! Serán indispensables en la fase de calibración del robot.
    :::
* - **5**
  - Alejar el robot con la botonera **sin mover nada** en la superficie
````
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::
---

## Paso 2: Acceso a la página Clearance
````{list-table}
:widths: 5 95

* - **6**
  - Desde la página **Locator Model**, tras hacer clic en **Next**, se abrirá la lista de Clearances disponibles (hasta 8 por modelo).
    
    :::{dropdown} **Página Clearances**
    
      ![Página Clearances](../../../../../_shared/media/images/pagina_clearances.png)
    
      | Elemento | Descripción |
      |----------|-------------|
      | **Clearance 1...8** | Ranuras disponibles para crear hasta 8 Clearances distintas para el mismo modelo |
      | **Test (global)** | Botón para probar simultáneamente todas las Clearances habilitadas |
      | **Next** | Avance a la fase siguiente (Robot Pick) tras la configuración de Clearances |
    :::
* - **7**
  - Haga clic en **Clearance 1**; se abrirá la página de configuración de la primera Clearance "Clearance 1"
    
    :::{dropdown} **Página Clearance 1**

      ![Página Clearance 1](../../../../../_shared/media/images/pagina_clearance1.png)

      | Parámetro | Función |
      |-----------|----------|
      | **Enable Clearance** | Activa esta Clearance y la deja operativa |
      | **Expression Builder** | Herramienta para configurar automáticamente los umbrales de detección |
      | **Mean and Standard Deviation** | Valores estadísticos calculados en el área seleccionada (media y desviación estándar de los niveles de gris) |
      | **Test** | Verificación inmediata del funcionamiento de la Clearance |
      | **Result** | Indicador visual del estado (Verde = OK, Rojo = Triggered) |
    :::
````
---

## Paso 3: Activación y posicionamiento del área

:::{video} ../../../../../_shared/media/videos/Step3.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **8**
  - Haga clic en **Enable Clearance** para activar la Clearance 
* - **9**
  - Desplace el **cuadro** de la Clearance hasta la zona que debe quedar libre
      - Normalmente: zona de agarre de la pinza (una Clearance por zona de agarre de la pinza)
      - Márgenes alrededor del componente
      - Zonas de paso del robot
    :::{important}
    Tenga siempre en cuenta estos dos aspectos importantes:
    - La ROI de la Clearance, cuando se configura, debe estar completamente libre (es decir, sin objetos, sombras ni artefactos)
    - Cree siempre una Clearance ligeramente mayor que lo estrictamente necesario para evitar falsos errores.

    La inobservancia de estos dos puntos podría provocar colisiones del robot que dañarían el FlexiBowl®, los componentes o el propio robot. 
    :::
````
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::
---

## Paso 4: Configuración automática

:::{video} ../../../../../_shared/media/videos/Step4.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **10**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> en Expression Builder
* - **11**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">
* - **12**
  - Compruebe que el recuadro se vuelva **verde** 
* - **13**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
````
````{warning}
**¿Qué hacer si el test falla (recuadro rojo)?**

Si después de AUTO el recuadro se vuelve rojo:

**Posibles causas:**
- Realmente hay algo en la zona (pieza, sombra, suciedad)
- La iluminación ha cambiado entre la configuración AUTO y TEST
- La zona seleccionada incluye bordes del FlexiBowl® o artefactos

**Soluciones:**
1. Compruebe visualmente que la zona está completamente despejada
2. Repita AUTO con condiciones de luz estables
3. Repita TEST para verificar
````
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::
---

## Clearances múltiples — cuándo usarlas

Cree más Clearances cuando:
- La herramienta del robot es una pinza: se necesita una Clearance para cada una de las dos zonas ocupadas por la pinza a cada lado del componente de referencia 
- Hay varios puntos críticos que controlar
- La zona de agarre tiene geometrías especiales

### *Paso 2-3: Repetición*
Seleccione una nueva Clearance en la página de la lista de Clearances, como "Clearance 2" y repita los pasos 2-3.
Repita el procedimiento para cada Clearance necesaria (hasta 8 por modelo). 

### *Paso 4: Prueba global* 

En la página de lista de todas las Clearances, haga clic en **TEST** para ver todas las Clearances a la vez  

![Página Clearances](../../../../../_shared/media/images/activatedclearances.png)
---

## Interpretación de estados

### *Estados de las Clearances*

````{list-table}
:header-rows: 1
:widths: 10 15 30 45

* - Color
  - Estado
  - Significado
  - Imagen
* - 🟢 Verde
  - OK
  - Zona libre, recogida posible
  - ![](../../../../../_shared/media/images/greenclearances.png)
* - 🔴 Rojo
  - Triggered
  - Zona ocupada, recogida no posible
  - ![](../../../../../_shared/media/images/redclearances.png)
````

### *¿Qué significa "Triggered"?*

Una Clearance se vuelve roja (triggered) cuando detecta en su interior:
- Presencia de otros componentes
- Sombras o reflejos significativos
- Cualquier elemento que haga que el área no esté libre

---

## Paso 5: Finalización
````{list-table}
* - **14**
  - Después de configurar todas las Clearances necesarias, haga clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **15**
  - Se abrirá la página **Robot Model Pick Cam**
````
````{seealso}
Proceda a la [Calibración del robot](robotpick) para completar la configuración.
````

