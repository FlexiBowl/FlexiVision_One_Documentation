# **Página Dashboard**
La interfaz de FlexiVision One está estructurada en secciones funcionales que guían al usuario desde la configuración inicial hasta la gestión operativa del sistema.
Cada página proporciona información en tiempo real sobre el estado de la máquina, las conexiones, el rendimiento y los parámetros del proceso, con acceso directo a las funciones clave.
La navegación está diseñada para facilitar el uso, el control inmediato de las operaciones y la supervisión continua de la visión, la alimentación y el rendimiento del robot.


<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Descripción Página Dashboard
:header-rows: 1
:widths: 10 90

* - **#**
  - **Descripción**

* - 1
  - **Área de visión y detección**
    * **Detected vision parts con grafico**: cuántos componentes se detectaron en la imagen actual y la tendencia en el tiempo (30 s).
    

* - 2
  - **Estado operativo**
    * **In run**: indicador luminoso que muestra si el sistema está en marcha o parado.
    * **In run time**: cronómetro que indica el tiempo total de funcionamiento del sistema.

* - 3
  - **Controles y selección**
    * **Menú desplegable FlexiBowl®**: permite seleccionar el dispositivo FlexiBowl® sobre el que se desea operar.
    * **Test Locator**: inicia movimientos cíclicos del FlexiBowl® y de la tolva mientras haya componentes en el área de visión.

* - 4
  - **Estado de las conexiones**
    * **FlexiBowl®**: indica el estado de la conexión en tiempo real con el FlexiBowl®.
    * **Robot**: indica el estado de la conexión en tiempo real con el robot.

* - 5
  - **Análisis del tiempo de ciclo (Timings)**
    * **Camera/Locator processing time**: tiempos individuales de captura de imagen y reconocimiento de componentes.
    * **Total vision processing Time**: suma de los tiempos de cámara y localizador.
    * **Total FlexiBowl® / Robot time**: tiempo para una secuencia de movimiento FB y un solo pick & place del robot.
    * **Total processing time**: tiempo total del proceso (Visión + FB + Robot).
    * **Fill hopper**: historial de descargas de la tolva sobre el disco FlexiBowl®.
    * **Vision - FlexiBowl® - Robot**: gráfico comparativo de las tres funciones para comprender el impacto de cada proceso individual en el tiempo total.
* - 6
  - **Gráficos de rendimiento e historial**
    * **Lista de modelos detectados**: tabla con coordenadas (**X**, **Y**), rotación (**Rot**) del componente y **Score** (grado de similitud del objeto reconocido respecto al modelo de referencia).
    * **Parts per minute**: gráfico de la media de componentes recogidos por minuto.
```
