# **Glosario** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Término
  - Definición
* - **Accept Threshold**
  - Umbral mínimo de similitud (score 0.0–1.0) para que un objeto detectado sea aceptado por el pattern matching. Valores típicos: 0.70–0.90.
* - **Air-blow**
  - Módulo neumático opcional para separar los componentes sobre el disco mediante chorros de aire comprimido. Requiere alimentación a 5–6 bar.
* - **Artefacto**
  - Defecto en la imagen adquirida causado por interferencias electromagnéticas, problemas de cableado o fallos del sensor.
* - **Calibración de Cámara**
  - Correlación entre píxeles y coordenadas reales mediante un target de calibración con patrón conocido. Calcula los parámetros intrínsecos y extrínsecos de la cámara.
* - **Clearance**
  - Análisis de la distribución de los niveles de gris en un área definida. Se utiliza para detectar presencia/ausencia de objetos (control de pinza, área libre).
* - **Cámara POE**
  - Cámara industrial alimentada y conectada mediante un único cable Ethernet. Estándar: IEEE 802.3af (15.4W) o 802.3at (30W).
* - **CAPTURE**
  - Comando de software para adquirir las imágenes de referencia del disco vacío y lleno, necesarias para el cálculo automático de los umbrales del hopper.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Categorías geométricas de los componentes en el FlexiBowl Wizard. *FLAT*: formas planas (arandelas, juntas). *CYLINDRICAL*: formas cilíndricas (pasadores, tornillos). *COMPLEX*: geometrías irregulares o asimétricas.
* - **Distancia de Trabajo**
  - Distancia óptima entre el objetivo y la superficie del disco. Normalmente 950–1000mm en configuraciones estándar.
* - **Distorsión Óptica**
  - Deformación geométrica de la imagen debida al objetivo. Se compensa automáticamente durante la calibración de la cámara.
* - **Exposición**
  - Tiempo de captación de luz del sensor de la cámara. Se mide en μs o ms; influye directamente en la calidad de la imagen en producción.
* - **Feature Threshold**
  - Umbral de extracción de características (bordes, líneas) durante el entrenamiento del modelo. Valores típicos: 0.3–0.8.
* - **FlexiBowl**
  - Sistema de alimentación con disco giratorio vibrante para el posicionamiento y la orientación aleatoria de componentes con fines de recogida robótica.
* - **FlexiBowl Wizard**
  - Procedimiento guiado para el cálculo automático de los parámetros óptimos del FlexiBowl según la geometría y el comportamiento de los componentes.
* - **Flip**
  - Impulso neumático bajo el disco para reposicionar los componentes. Configurable mediante *Flip Count* (número de impulsos) y *Flip Delay* (intervalo en ms entre impulsos).
* - **Grab Train Image**
  - Comando de software para adquirir la imagen que se usará en el entrenamiento de un nuevo modelo.
* - **Gripper Offset**
  - Vector de corrección (ΔX, ΔY, ΔRZ) que compensa el desplazamiento entre el centro óptico del sistema de visión y el TCP del gripper.
* - **Hotspot**
  - Zona de reflexión directa de la luz en la imagen. Aparece como un área sobreexpuesta y puede comprometer el reconocimiento.
* - **Objetivo**
  - Componente óptico de la cámara. Debe enroscarse hasta el contacto metal-metal; la distancia focal (p. ej. 16mm, 25mm) determina el campo visual a la distancia de trabajo.
* - **Model (Modelo)**
  - Plantilla geométrica del componente creada durante el entrenamiento. Cada receta admite hasta 8 modelos.
* - **Origen del Modelo**
  - Punto de referencia sobre el componente usado como centro del sistema de coordenadas para el cálculo de posiciones. Normalmente corresponde al TCP de agarre.
* - **Ortogonalidad**
  - Perpendicularidad de la cámara respecto al disco (tolerancia ±1°). Puede verificarse con un nivel de precisión.
* - **Pattern Matching**
  - Algoritmo que localiza los componentes en la imagen comparándolos con el modelo de referencia registrado durante el entrenamiento.
* - **Protocol (Protocolo)**
  - Formato de comunicación entre VisionController y robot. Define la estructura de los mensajes, el orden de las coordenadas y las unidades de medida.
* - **Recipe (Receta)**
  - Archivo XML que contiene todos los parámetros de configuración del sistema: modelos, umbrales, calibraciones, setup FlexiBowl y robot.
* - **Region Search**
  - Área rectangular en la imagen dentro de la cual el pattern matching realiza la búsqueda. Reduce los tiempos de procesamiento y aumenta la precisión.
* - **ROI (Region of Interest)**
  - Área rectangular que delimita el componente en la imagen durante el entrenamiento del modelo.
* - **RZ / Rotation Z**
  - Ángulo de rotación alrededor del eje Z comunicado al robot para la orientación del componente. Expresado en grados (0–360°).
* - **Score**
  - Índice de similitud (0.0–1.0) entre el modelo y el objeto detectado. Determina la confianza del reconocimiento.
* - **Simuladores de Ocupación de la Pinza**
  - Objetos físicos colocados alrededor del componente durante el entrenamiento para excluir del modelo las áreas ocupadas por la pinza durante la recogida.
* - **Steps**
  - Número de ciclos de vibración del hopper necesarios para que los componentes alcancen el área de recogida. Parámetro crítico para la sincronización con el ciclo del robot.
* - **Subnet**
  - FlexiBowl y VisionController deben compartir la misma subnet (p. ej. 192.168.1.x) para la comunicación TCP/IP.
* - **Synchronize Parameters**
  - Comando de software que transfiere los parámetros del VisionController al FlexiBowl. Obligatorio después de cada modificación para que los ajustes sean efectivos.
* - **Target de Calibración**
  - Patrón geométrico impreso (círculos o tablero de ajedrez) con dimensiones conocidas y superficie plana, usado para la calibración de la cámara.
* - **Timeout**
  - Tiempo máximo de espera para una respuesta en comunicación. Al superarlo se genera un error.
* - **Tilt**
  - Inclinación de la cámara respecto al plano horizontal. Valor permitido: 0° ± 1°.
* - **Toplight**
  - Iluminador LED situado sobre el disco que garantiza una iluminación uniforme desde arriba. Alimentación: 24V DC.
* - **Training**
  - Proceso de creación del modelo de reconocimiento mediante la selección de las características distintivas del componente a partir de una imagen de referencia.
* - **Trigger**
  - Señal de inicio de la adquisición de imagen. Puede ser software (temporizada) o hardware (señal eléctrica externa).
* - **Vision Result**
  - Salida del sistema de visión: coordenadas (X, Y, RZ) y score del componente detectado, transmitidos al robot para la recogida.
* - **VisionController**
  - Ordenador industrial que ejecuta FlexiVision One, gestiona las cámaras, procesa las imágenes y se comunica con FlexiBowl y el robot.
```

