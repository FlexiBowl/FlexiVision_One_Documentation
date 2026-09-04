(hoppersetup)=
# **Hopper Setup**
 
Esta sección describe el procedimiento para configurar la tolva (Hopper). El Hopper es el componente que alimenta automáticamente piezas en el FlexiBowl® cuando el nivel desciende por debajo de un umbral mínimo.
 
:::{important}  **Lógica de funcionamiento**  
 
FlexiVision gestiona la lógica de activación de la tolva. Enviará la cadena `Hopper;signalnumber;time` cuando considere necesaria la activación. 
:::
````{note}
**Requisitos previos**
 
Antes de continuar, asegúrese de que:
- El Hopper se haya instalado mecánicamente 
- Las conexiones eléctricas se hayan completado (señales de control y alimentación)
- El FlexiBowl® ya esté conectado
````
---
## Preparación de la configuración física
 
````{list-table}
* - **0**
  - Desmontar la rejilla de calibración y restablecer la disposición inicial:
    - Reposicionar la superficie
    - reposicionar la brida central 
    - fijar la brida central con sus cuatro tornillos
````
---
## Acceso a la configuración del Hopper
 
````{list-table}
* - **1** 
  - Desde la página principal del software, haga clic en <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - En la página SETUP, localice y haga clic en el icono **Hopper Setup**
```{dropdown} Página Setup 
       ![Página Setup](../../../../../_shared/media/images/pagina_setup1.png)
```
* - **3** 
  - Se abre la página de configuración del Hopper
````
 
---
 
## Descripción general de la interfaz Hopper Setup
 
La página Hopper Setup presenta varias secciones para la configuración de los parámetros operativos de las distintas tolvas:
 
![Página Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
 
````{list-table}
:header-rows: 1
:widths: 30 70
 
* - Sección
  - Descripción
* - **Enable Hopper**
  - Interruptor para habilitar/deshabilitar el uso del Hopper en el sistema
* - **Steps**
  - Número de secuencias necesarias con las que la sección del disco que se encuentra actualmente en el área de visión llega bajo el área de descarga de la tolva
* - **Wizard Steps**
  - Inicia el procedimiento guiado para el cálculo automático del parámetro Steps (véase [Wizard Steps](wizardsteps))
* - **Time**
  - Duración de la activación de la tolva en milisegundos
* - **Wizard Time**
  - Inicia el procedimiento guiado para el cálculo automático de los parámetros de activación de la tolva (véase [Wizard Time](wizardtime))
* - **Signal**
  - Número de la señal digital utilizada para controlar el Hopper
* - **Config Hopper**
  - Botón para configurar la tolva (para usar a continuación)
````
 
---
(confighopper)=
# **Configuración de la Tolva (Hopper)**
 
La configuración de la tolva permite gestionar el reabastecimiento automático de los componentes en el disco del FlexiBowl®. El sistema utiliza la visión para determinar cuándo el nivel de llenado es insuficiente y activar la tolva.
 
## Paso 1: Acceso a la Configuración
````{list-table}
* - **1**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">.   
    Desde la sección **Hopper Setup**, es posible visualizar y gestionar las unidades de carga conectadas.
    
    :::{dropdown} Página Hopper Setup 
    ![Página Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **2**
  - En el campo **Signal**, introduzca el número de la señal digital (DO - Digital Output) utilizada para controlar el Hopper
    :::{warning}
      Es fundamental introducir el número de señal correcto:
      - Un número erróneo activará la señal equivocada (potencialmente peligroso)
      - Consulte el esquema eléctrico realizado durante la instalación
      - En caso de duda, contacte con quien haya realizado el cableado
    :::
* - **3**
  - Seleccione la casilla **Enable Hopper X** para activar la tolva correspondiente.
      :::{important}
      Habilite el Hopper solo si el dispositivo está correctamente instalado
      :::
* - **4**
  - Haga clic en el botón **Config Hopper X** para acceder a la configuración específica 
````
## Paso 2: Definición del Área de Control
 
:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::
 
En esta fase se define la porción del disco que la cámara debe monitorizar para la descarga.
````{list-table}
* - **5**
  - Modifique el recuadro azul en pantalla para encuadrar el área en la que se detectarán los componentes.
````
:::{tip}
Para cualquier duda durante la configuración, consulte el botón **INFO** presente en la página actual.
:::
 
## Paso 3: Definición de los Valores Umbral
 
:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::
````{list-table}
* - **6**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> para acceder a la página **Define Value Hopper Cam**, donde se instruye al sistema para distinguir entre disco vacío y disco lleno.
    :::{dropdown} Página Define Value Hopper Cam 
    ![Página Define Value Hopper Cam](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Retire todos los componentes del área de visión y haga clic en el primer botón **CAPTURE**.
* - **8**
  - Coloque el número mínimo de componentes que desea mantener en el área de visión. Si el número desciende por debajo de este umbral, la tolva se activará.
* - **9**
  - Haga clic en el segundo botón **CAPTURE**.
* - **10**
  - Al hacer clic en <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> en el Expression Builder, el sistema calcula automáticamente los valores de **Mean** (Media) y **Standard Deviation** (Desviación estándar).
* - **11**
  - Retire algunas piezas y haga clic en <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">. 
* - **12**
  - Observe el indicador de resultado:
    - **Verde** 🟢: Nivel insuficiente, el Hopper se activa (descarga necesaria)
    - **Rojo** 🔴: Nivel suficiente, el Hopper NO se activa (OK)
 
      :::{warning}
      **Calibración insuficiente**
 
      Si el sistema no detecta correctamente el nivel:
 
      **Problema: Siempre verde (activa siempre el Hopper)**  
      → Umbral demasiado bajo o interferencias en el área  
      → Solución: Aumentar el número de piezas en la segunda adquisición, verificar la limpieza del área  
 
      **Problema: Siempre rojo (no activa nunca el Hopper)**  
      → Umbral demasiado alto o área de monitorización no representativa  
      → Solución: Reducir el número de piezas en la segunda adquisición CAPTURE, repetir AUTO  
 
      **Problema: Comportamiento erróneo (alterna verde/rojo aleatoriamente)**  
      → Iluminación inestable o área demasiado pequeña  
      → Solución: Verificar que el backlight sea estable, ampliar el área de monitorización, repetir la calibración  
      :::
````
````{note}
**Hopper Fill Threshold**
 
El parámetro **Hopper Fill Threshold** define el umbral porcentual de llenado del área de visión por debajo del cual la tolva se activa automáticamente.
 
El valor del 100% corresponde a la cantidad de piezas adquirida durante la segunda CAPTURE (área llena). Por consiguiente, un umbral del 50% corresponde a la mitad de dicha cantidad.
 
El sistema establece automáticamente el valor inicial en **70%**, que representa un buen equilibrio para la mayoría de las aplicaciones.
 
**Modificación sobre la marcha**
 
Es posible ajustar el umbral sin repetir el procedimiento de adquisición:
 
- Para descargar **menos piezas** → reducir el porcentaje (p. ej. 50%) y hacer clic en **AUTO**
- Para descargar **más piezas** → aumentar el porcentaje (p. ej. 85%) y hacer clic en **AUTO**
 
````
 
:::{tip}
Para cualquier duda durante la configuración, consulte el botón **INFO** presente en la página actual.
:::
 
## Paso 4: Parámetros Operativos
 
Vuelva a la pantalla principal de Hopper Setup para definir el comportamiento mecánico.
![Página Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
 
````{list-table} Parámetros de Funcionamiento
:widths: 20 80
:header-rows: 1
 
* - **Parámetro**
  - **Descripción y Procedimiento**
* - **Steps**
  - Número de avances del FlexiBowl® (secuencias) necesarios para llevar las piezas desde el área de visión hasta el área de descarga de la tolva. Puede configurarse manualmente o calcularse mediante el [Wizard Steps](wizardsteps).
* - **Time**
  - Milisegundos de activación de la tolva. Valor recomendado: **100 – 1000 ms** (Media: **500 ms**). Ajustar en ±50 ms en función del flujo deseado. Puede configurarse manualmente o calcularse mediante el [Wizard Time](wizardtime).
````
````{tip}
   El tiempo de activación depende no solo del valor establecido, sino también del volumen de componentes presentes actualmente en el depósito de la tolva. Es esencial mantener una carga constante para un flujo uniforme.
````
````{tip}
El valor Time está estrechamente relacionado con el volumen de carga de la tolva: 
- Con la tolva llena habrá un mayor número de piezas en el área de descarga 
- Con la tolva medio llena habrá un menor número de piezas en el área de descarga 
 
````
:::{important}
En general, es importante no superar nunca la carga máxima de la tolva utilizada. 
:::
 
---
 
(wizardsteps)=
### *Wizard Steps: Cálculo Guiado del Parámetro Steps*
 
El **Wizard Steps** guía al operador en el cálculo del número de secuencias necesarias para que una pieza, colocada en el centro del área de visión, alcance el área de descarga de la tolva.
 
:::{dropdown} Hopper Step Setup Cam X
![Hopper Step Setup](../../../../../_shared/media/images/pagina_hopperstepwizard.png)
:::
 
````{list-table}
* - **1**
  - Coloque una única pieza en el centro del área de visión.
    :::{important}
    Asegúrese de que la secuencia actualmente cargada en el FlexiBowl® sea la definitiva, es decir, la misma que se utilizará en producción. Un cambio de secuencia posterior invalidaría el valor calculado.
    :::
* - **2**
  - Haga clic en **Reset Steps** para poner a cero el contador e iniciar el procedimiento de calibración.
* - **3**
  - Haga clic en **Test Sequence** para ejecutar una única secuencia del FlexiBowl®.
    :::{tip}
    Espere a que finalice la secuencia antes de ejecutar otra.
    :::
* - **4**
  - Repita el clic en **Test Sequence** hasta que la pieza alcance el área de la tolva. El **Current Step Count** se actualiza automáticamente después de cada secuencia ejecutada.
* - **5**
  - Cuando la pieza alcance el área de la tolva, haga clic en **Save Hopper Step** para guardar el valor actual como parámetro Steps.
````
 
:::{warning}
El valor calculado con el Wizard Steps **no se conserva tras reiniciar** el software si la receta no se guarda. Recuerde guardar la receta al finalizar el procedimiento (véase [Guardado de la Configuración](#salvataggio-configurazione)).
:::
 
El indicador **Calibration Active** muestra el estado de la calibración en curso:
 
| Color | Estado |
| --- | --- |
| 🔴 Rojo | Calibración no activa / aún no iniciada |
| 🟢 Verde | Calibración en curso / completada |
 
 
### *Calcular el Parámetro Steps*
 
![Primera Página Steps](../../../../../_shared/media/images/Steps1.png)
![Segunda Página Steps](../../../../../_shared/media/images/Steps2.png)
![Tercera Página Steps](../../../../../_shared/media/images/Steps3.png)
![Cuarta Página Steps](../../../../../_shared/media/images/Steps4.png)
 
---
 
(wizardtime)=
### *Wizard Time: Cálculo Guiado de los Parámetros de Activación*
 
El **Wizard Time** guía al operador en el ajuste de los parámetros de activación de la tolva (amplitud, frecuencia y tiempo de activación), verificando su efecto mediante una prueba directa sobre el flujo de las piezas.
 
:::{dropdown} FlexiBowl® X Hopper – Time and Parameter Setup
![Hopper Time Setup](../../../../../_shared/media/images/pagina_hoppertimewizard.png)
:::
 
````{list-table}
* - **1**
  - Llene la tolva con una cantidad de piezas suficiente para simular las condiciones normales de funcionamiento.
* - **2**
  - Verifique que las piezas estén correctamente colocadas y puedan moverse libremente hacia la salida de la tolva.
* - **3**
  - Establezca los valores de **Amplitude (V)**, **Frequency (Hz)** y **Activation Time (ms)** mediante los controles deslizantes correspondientes o introduciendo el valor directamente en el campo numérico.
* - **4**
  - Haga clic en **Test Hopper** para activar la tolva con los parámetros establecidos y verificar el flujo de piezas.
* - **5**
  - Ajuste los valores y repita la prueba hasta obtener el comportamiento de alimentación deseado.
````
 
:::{tip}
Proceda con la configuración de la siguiente sección (Hopper Step) solo una vez que el flujo de piezas resulte satisfactorio.
:::
 
## Guardado de la Configuración
````{warning}
**Guardado de la receta obligatorio**
 
Al finalizar la configuración del Hopper:
 
  :::{list-table}
    * - 1. 
      - Verificar que todos los parámetros estén configurados correctamente:
        - Área de monitorización posicionada
        - Umbrales calibrados (TEST funcionando)
        - Steps y Time establecidos
    * - 2. 
      - Volver a la página principal <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon icon-small">
    * - 3. 
      - Hacer clic en <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon icon-small">
    * - 4. 
      - Confirmar el guardado
  :::
**IMPORTANTE**: Cada variación realizada se guarda **SOLO** si la receta se guarda correctamente antes de salir o cambiar de página.
 
Sin guardar, ¡todas las configuraciones del Hopper se perderán al cerrar FlexiVision One!
````
 
---
 
 
## Próximos pasos
 
Una vez completada la configuración del Hopper (u omitida si no está presente), proceda con:
 
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Guardar la Receta](ricettabase)
