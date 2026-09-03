# **Glosario**

```{list-table}
:header-rows: 1
:widths: 25 75

* - Término
  - Definición
* - **Umbral de aceptación**
  - Umbral mínimo de similitud (puntuación 0,0-1,0) para que un objeto detectado sea aceptado por la concordancia de patrones. Valores típicos: 0.70–0.90
* - **Air-blow**
  - Módulo neumático opcional para separar los componentes en el disco mediante chorros de aire comprimido. Requiere alimentación a 5-6 bar.
* - **Artefacto**
  - Defecto en la imagen capturada causado por interferencias electromagnéticas, problemas de cableado o mal funcionamiento del sensor.
* - **Calibración de la cámara**
  - Correlación real de píxeles y coordenadas mediante un objetivo de calibración con patrón conocido. Calcula los parámetros intrínsecos y extrínsecos de la cámara.
* - **Clearance**
  - Análisis de la distribución de los niveles de gris en un área definida. Permite detectar la presencia/ausencia de objetos (control de pinzas, zona libre).
* - **Cámara POE**
  - Cámara industrial alimentada y conectada mediante un único cable Ethernet. estándar IEEE 802.3af (15.4 W) o 802.3at (30 W).
* - **CAPTURE**
  - Comando del software para adquirir imágenes de referencia del disco vacío y lleno, necesarias para el cálculo automático de los umbrales de la tolva.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Categorías geométricas de componentes en el Asistente FlexiBowl®. *FLAT*: formas planas (arandelas, juntas). *CYLINDRICAL*: formas cilíndricas (clavijas, tornillos). *COMPLEX*: geometrías irregulares o asimétricas.
* - **Distancia de trabajo**
  - Distancia óptima entre la lente y la superficie del disco. Normalmente 950-1000 mm en configuraciones estándar.
* - **Distorsión ópica**
  - Distorsión geométrica de la imagen debida al objetivo. Se compensa automáticamente durante la calibración de la cámara.
* - **Exposición**
  - Tiempo de captación de luz del sensor de la cámara. Se mide en μs o ms; influye directamente en la calidad de la imagen en la producción.
* - **Umbral de características**
  - Umbral de extracción de características (bordes, líneas) durante el entrenamiento del modelo. Valores típicos: 0.3–0.8
* - **FlexiBowl®**
  - Sistema de alimentación de disco giratorio vibratorio para el posicionamiento y la orientación aleatorios de componentes para el picking robotizado.
* - **FlexiBowl® Wizard**
  - Asistente para el cálculo automático de los parámetros FlexiBowl® óptimos en función de la geometría y el comportamiento los componentes.
* - **Flip**
  - Impulso neumático bajo el disco para reposicionar los componentes. Configurable mediante *Flip Count* (número de pulsos) y *Flip Delay* (intervallo en ms entre pulsos).
* - **Grab Train Image**
  - Comando de software para adquirir la imagen que se utilizará en el entrenamiento de un nuevo modelo.
* - **Desplazamiento de la pinza**
  - Vector de corrección (ΔX, ΔY, ΔRZ) que compensa el desplazamiento entre el centro óptico del sistema de visión y el TCP de la pinza.
* - **Hotspot**
  - Área de reflexión directa de la luz en la imagen. Aparece como una zona sobreexpuesta y puede dificultar el reconocimiento.
* - **Objetivo**
  - Componente óptico de la cámara. Debe enroscarse hasta hacer contacto metal-metal; la distancia focal (por ejemplo, 16 mm, 25 mm) determina el campo de visión a la distancia de trabajo.
* - **Modelo**
  - Modelo geométrico del componente creado en la fase de formación. Cada receta admite hasta 8 modelos por FlexiBowl®.
* - **Origen del modelo**
  - Punto de referencia en el componente utilizado como centro del sistema de coordenadas para el cálculo de la posición. Suele corresponder al socket TCP.
* - **Ortogonalidad**
  - Perpendicularidad de la cámara con respecto al disco (tolerancia ±1°). Verificable con nivel de precisión.
* - **Pattern Matching**
  - Algoritmo que localiza componentes en la imagen comparándolos con el modelo de referencia registrado durante el entrenamiento.
* - **Protocolo**
  - Formato de comunicación entre VisionController y el robot. Define la estructura del mensaje, el orden de las coordenadas y las unidades.
* - **Receta**
  - Archivo XML que contiene todos los parámetros de configuración del sistema: modelos, umbrales, calibraciones, configuración FlexiBowl® y robot.
* - **Búsqueda de región**
  - Área rectangular en la imagen dentro de la cual la concordancia de patrones realiza la búsqueda. Reduce el tiempo de procesamiento y aumenta la precisión.
* - **ROI (Región de interés)**
  - Área rectangular que delimita el componente en la imagen durante el entrenamiento del modelo.
* - **RZ / Rotación Z**
  - Ángulo de rotación alrededor del eje Z comunicado al robot para la orientación de los componentes. Expresado en grados (0-360°).
* - **Puntuación**
  - Índice de similitud (0,0-1,0) entre el modelo y el objeto detectado. Determina la confianza del reconocimiento.
* - **Simuladores de pinza**
  - Objetos físicos colocados alrededor del componente durante el entrenamiento para excluir del modelo las zonas ocupadas por la pinza durante el picking.
* - **Pasos**
  - Número de movimientos del FlexiBowl® necesarios para que los componentes de la zona de visión alcancen la zona de descarga de la tolva.
* - **Subred**
  - Subred que FlexiBowl® y VisionController deben compartir (por ejemplo, 192.168.1.x) para la comunicación TCP/IP.
* - **Sincronizar parámetros**
  - Comando de software que transfiere parámetros al FlexiBowl®. Obligatorio después de cada cambio para que la configuración sea efectiva.
* - **Tiempo de espera**
  - Tiempo máximo de espera para una respuesta de comunicación. Se genera un error cuando se supera.
* - **Inclinación**
  - Inclinación de la cámara con respecto al plano horizontal. Valor permitido: 0° ± 1°.
* - **Toplight**
  - Iluminador LED situado sobre el disco para una iluminación uniforme desde arriba. Fuente de alimentación: 24 V DC.
* - **Formación**
  - Proceso de creación del modelo de reconocimiento mediante la selección de las características distintivas del componente a partir de una imagen de referencia.
* - **Disparador**
  - Señal de inicio de captura de imagen. Puede ser software (temporizado) o hardware (señal eléctrica externa).
* - **Resultado de la visión**
  - Salida del sistema de visión: coordenadas (X, Y, RZ) y puntuación del componente detectado, transmitidos al robot para su recogida.
* - **VisionController**
  - Ordenador industrial que ejecuta FlexiVision One, gestiona las cámaras, procesa las imágenes y se comunica con FlexiBowl® y los robots.
```

