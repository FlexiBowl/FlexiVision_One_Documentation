

# **Página DashBoard**
<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Descripción de la página del panel de control
:header-rows: 1
:widths: 10 90

* - **#**
  - **Descripción**

* - 1
  - **Visión y área de detección**
    * **Detected vision parts con grafico**: cuántos componentes se detectaron en la imagen actual y la tendencia en el tiempo (30s).
    

* - 2
  - **Estado de funcionamiento**
    * **In run**: indicador luminoso que muestra si el sistema está en marcha o parado.
    * **In run time**: cronómetro que indica el tiempo total de funcionamiento del sistema.

* - 3
  - **Controles y Selección**
    * **Menú desplegable FlexiBowl®**: permite seleccionar el dispositivo FlexiBowl® sobre el que se desea operar.
    * **Test Locator**: inicia movimientos cíclicos del FlexiBowl® y la tolva mientras haya componentes en la zona de visión.

* - 4
  - **Estado de la conexión**
    * **FlexiBowl®**: indica el estado de la conexión en tiempo real con el FlexiBowl®.
    * **Robot**: indica el estado de la conexión en tiempo real con el robot.

* - 5
  - **Análisis del tiempo de ciclo (Timings)**
    * **Camera/Locator processing time**: tiempos de toma de imágenes individuales y reconocimiento de componentes.
    * **Total vision processing Time**: suma de los tiempos de la cámara y del localizador.
    * **Total FlexiBowl® / Robot time**: tiempo para una secuencia de movimiento FB y un solo robot pick & place.
    * **Total processing time**: tiempo total del proceso (Visión + FB + Robot).
    * **Fill hopper**: historial de descargas de la tolva sobre el disco FlexiBowl®.
    * **Vision - FlexiBowl® - Robot**: gráfico comparativo de las tres funciones para comprender el impacto de cada proceso individual en el tiempo total.
* - 6
  - **Gráficos de rendimiento e historial**
    * **Lista de modelos detectados**: tabla con las coordenadas (**X**, **Y**), la rotación (**Rot**) del componente y la **Puntuación** (grado de similitud del objeto detectado con el modelo de referencia).
    * **Parts per minute**: gráfico de la media de piezas tomadas por minuto.
```
(recipes)=
# **Página de recetas**
<img src="../../../../_shared/media/images/pagina_recipesW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_recipesB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Descripción Página Recetas
:header-rows: 1
:widths: 10 90

* - **#**
  - **Descripción**

* - 1
  - **Gestión de la base de datos de recetas**
    * **Backup**: realiza una copia de seguridad de todas las recetas en un único archivo .xml, que puede guardarse en la ubicación deseada.
    * **Import backup**: permite importar cualquier copia de seguridad realizada previamente con FlexiVision One.
    * **Load recipe**: carga la receta seleccionada en la lista anterior para dejarla operativa.
    * **Delete recipe**: elimina definitivamente la receta seleccionada de la lista.

* - 2
  - **Crear y guardar**
    * **New recipe**: inicia la creación de una nueva receta. Tras elegir el nombre y el FlexiBowl® con el que vamos a trabajar, se abre directamente el menú de creación de modelos.
      :::{note}
        A continuación, debe guardar la receta haciendo clic en Save.
      :::
    * **Save recipe**: guarda la receta actual sobrescribiendo los parámetros modificados o crea un nuevo archivo si aún no existe.

* - 3
  - **Editar receta**
    * **Edit recipe**: botón directo que le lleva al menú de configuración y creación de modelos de la receta actualmente seleccionada.
```

# **Página de configuración**
<img src="../../../../_shared/media/images/pagina_setupW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_setupB.png" class="only-dark" style="width: 20%; height: auto;">


```{list-table} Descripción Página de configuración
:header-rows: 1
:widths: 10 90

* - **#**
  - **Descripción**

* - 1
  - **Información de estado**
     - **Current selected recipe**: indica el nombre de la receta actualmente en uso.
     - **Current user name**: muestra el usuario conectado y el nivel de acceso correspondiente.
     - **In Run**: indica si la aplicación está activa.

* - 2
  - **Panel de acceso**
     - **Name**: campo para introducir el nombre de usuario.
     - **Login**: botón para confirmar las credenciales e iniciar sesión en el sistema.

* - 3
  - **Camera setup**: sección dedicada a la configuración de los parámetros de la cámara.
* - 4
  - **FlexiBowl® setup**: zona para configurar los parámetros de movimiento y control del FlexiBowl®.
     
* - 5
  - **Hopper setup**: configuración de los parámetros de la tolva (vibración y descarga).
     
* - 6
  - **Robot setup**: sección para configurar la comunicación con el robot.

* - 7
  - **Protocol setup**: página de configuración de parámetros que define cuántos objetos debe o puede devolver la visión en cada ciclo, en qué orden se priorizan y qué valores estadísticos utilizar en función del número de tomas del robot y del tiempo máximo de manipulación de cada componente.
     
* - 8
  - **Account setup**: permite configurar las distintas cuentas de usuario en función de los niveles de acceso.

* - 9
  - **Laser pointer**: permite utilizar un instrumento láser para simular un pick en ausencia del robot.
* - 10
  - **Evaluate PPM**: permite estimar las partes por minuto (PPM) al utilizar el puntero láser.

* - 11
  - **Licence software**: página para la activación de la licencia de software.
```
# **Los botones INFO**
En cada una de las secciones operativas, está disponible un botón INFO en la parte superior derecha.
Dentro de este botón está disponible la explicación del procedimiento Step By Step; el mismo procedimiento puede verse en el videotutorial.
```{dropdown} Botón Info de la página [Camera FLB](cameraFLB)

   :::{video} ../../../../_shared/media/videos/TastoInfo_CameraFLB_1280x720.mp4
   :width: 100%
   :align: center
   :::

```

```{dropdown} Botón Info de la página [Calibration](calibrazione)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Calibration_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Train Model](modello)

   :::{video} ../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Define Robot Picking Area](robotarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Locator Model](locator)

   :::{video} ../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Clearances](clearances)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearances_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Clearance 1](clearance1)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearance1_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Picking Offset](pickingoffset)

   :::{video} ../../../../_shared/media/videos/TastoInfo_PickingOffset_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Define Hopper Area](definehopperarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Botón Info de la página [Define Value Hopper](definevaluehopper)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
