(Installazione_Meccanica)=
# **Instalación mecánica del sistema**

Esta sección describe los requisitos de montaje y posicionamiento de los componentes clave del sistema de visión FlexiVision One. La instalación sólo debe llevarse a cabo una vez finalizada la instalación mecánica básica del FlexiBowl® y de la tolva, en su caso.

```{warning}
**Requisitos previos obligatorios**

Antes de proceder a la instalación de los componentes de visión, asegúrese de que:

- El FlexiBowl® se ha montado y fijado a la estructura de soporte (célula robotizada)
- La tolva se ha instalado correctamente
- Se ha preparado la estructura de soporte para la cámara y el iluminador

Para la instalación del FlexiBowl®, consulte el manual específico suministrado.
```

```{note}
**Competencias requeridas**

Requiere instalación mecánica:
- Conocimientos básicos de montaje mecánico
- Utilización de instrumentos de medida (calibre, nivel de burbuja, metro)
- Capacidad para leer dibujos técnicos
```

---

## Montaje VisionController

El VisionController (PC industrial) se encarga del procesamiento de imágenes y de la comunicación con el robot.
Como componente electrónico sensible, requiere una colocación cuidadosa para garantizar una ventilación adecuada y la protección contra contaminantes.

### *Especificaciones técnicas*
```{figure} ../../../../_shared/media/images/Dim_PC.png
:alt: Dimensiones del VisionController
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60
* - **Orificios para tornillos**
  - M5
* - **Característica**
  - **Valor**
* - Anchura (total con soportes)
  - 245.00 mm
* - Anchura (cuerpo)
  - 227.00 mm
* - Anchura del panel de conectores
  - 200.00 mm
* - Altura (total con soportes)
  - 123.00 mm
* - Altura (cuerpo)
  - 120.00 mm
* - Profundidad
  - 61.10 mm
```

### *Requisitos de montaje*

```{list-table}
:header-rows: 1
:widths: 35 65

* - Requisito
  - Especificaciones
* - **Ubicación recomendada**
  - Dentro del armario de control o en un panel dedicado cerca de la célula del robot
* - **Espacio de ventilación**
  - Mínimo 50 mm en todos los lados para la circulación del aire
* - **Fijación**
  - Carril DIN de 35 mm o tornillos M5 en el panel
* - **Temperatura ambiente**
  - 1°C ~ +50°C (consulte las especificaciones completas en la sección [Especificaciones del VisionController](specifiche_VC))
* - **Protección**
  - IP40 mínimo (se recomienda montaje en armario IP54)
```

### *Procedimiento de instalación*

#### *Conjunto con orificios*

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Fase
     - Descripción operativa
   * - **1. Preparación del sustrato**
     - Taladre los orificios según las instrucciones de la ficha técnica 
   * - **2. Desembalaje**
     - Saque el VisionController del embalaje con cuidado de no dañar los conectores. Comprobar la integridad del producto.
   * - **3. Fijación**
     - Fije el VisionController con tornillos M5  
```

#### *Montaje con carril DIN*

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Fase
     - Descripción operativa
   * - **1. Preparación del soporte**
     - compruebe que el raíl está limpio y bien fijado.
   * - **2. Desembalaje**
     - Saque el VisionController del embalaje con cuidado de no dañar los conectores. Comprobar la integridad del producto.
   * - **3. Fijación**
     - Enganche el dispositivo deslizándolo sobre el raíl hasta que encaje en su sitio.  
```

```{warning}
**Ventilación**

El VisionController genera calor durante su funcionamiento. Deje siempre un espacio libre de al menos 50 mm alrededor del aparato.
De lo contrario, se puede tener:
- Sobrecalentamiento y apagado automático
- Reducción del rendimiento
- Daños en los componentes internos
```

---

## Montaje de la cámara

El posicionamiento preciso y la alineación de la cámara son pasos críticos que influyen directamente en la precisión de calibración y el rendimiento del sistema de picking.


### *Distancia óptima de trabajo*

La cámara debe montarse de forma que la cara frontal del objetivo se sitúe a una distancia determinada (Distancia de trabajo) de la superficie de trabajo del FlexiBowl®.
Para un cálculo detallado de la distancia óptima para su aplicación, consulte la sección dedicada: [Cálculo óptimo de la distancia](distanza_lavoro)

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distancia de trabajo
:width: 40%
:align: center
```

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modelo FlexiBowl®
  - Distancia de trabajo recomendada
  - Lente incluida en el kit (Longitud focal)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

### *Posicionamiento y alineación*

La correcta alineación de la cámara es crucial para obtener imágenes de calidad y garantizar la precisión de la recogida.

**Configuraciones incorrectas.** Las imágenes muestran ejemplos de colocación incorrecta de la cámara: el campo de visión (indicado en rojo) está descentrado con respecto a la zona de visión, cubre sólo una parte de la zona de trabajo o incluye zonas fuera de la zona de trabajo. Estas configuraciones comprometen el reconocimiento de las piezas y el funcionamiento del sistema de visión.

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distancia de trabajo
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distancia de trabajo
:width: 60%
:align: center
```
**Configuración correcta.** La cámara debe colocarse centrada respecto a la zona de visión del FlexiBowl® (zona de contraluz). De este modo, el campo de visión (mostrado en verde) cubre simétricamente toda la zona de trabajo, garantizando el correcto funcionamiento del sistema de visión.

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distancia de trabajo
:width: 70%
:align: center
```

```{list-table}
* - **Centrado:**
  - 
    - La cámara debe colocarse exactamente por encima del área de visión del FlexiBowl®
    - Tolerancia máxima de centrado: ±5 mm
* - **Ortogonalidad:**
  - 
    - La cámara debe montarse perfectamente paralela a la superficie de trabajo del FlexiBowl®
    - No se admiten inclinaciones laterales (tilt) ni rotaciones respecto a la vertical
    - Tolerancia máxima de inclinación: ±1°
```

```{tip}
Para facilitar la puesta a punto y permitir ajustes futuros, se recomienda encarecidamente diseñar el soporte mecánico de la cámara con posibilidad de microajustes:
- **Eje Z (altura)**: -10 mm / +30 mm (para adaptación de la distancia de trabajo)
- **Eje X (izquierda-derecha)**: ±10 mm (para centrado fino)
- **Eje Y (adelante-atrás)**: ±10 mm (para centrado fino)
Esta flexibilidad resulta especialmente útil durante la calibración inicial y para posibles recalibraciones futuras.
```

### *Dimensiones de la cámara* 
```{figure} ../../../../_shared/media/images/Dimensioni_Cam.png
:alt: Dimensiones de la cámara CAM-CIC-5000-20G-1
:align: center
:width: 100%

CAM-CIC-5000-20G-1 Dimensiones de la cámara (mm)
```
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Característica**
  - **Valor**
* - Anchura × Altura (cuerpo)
  - 29 × 29 mm
* - Profundidad (cuerpo)
  - 42,0 mm
* - Profundidad total (incluido el conector trasero)
  - 48,9 mm
* - Proyección frontal (montaje del objetivo)
  - 12.60 mm
* - Distancia central de los orificios de fijación laterales (M2)
  - 20,0 × 23,7 mm
* - Orificios de fijación frontales
  - 2× M2 profundidad 3 mm
* - Orificios de fijación laterales
  - 4× M2 profundidad 3,5 mm + 3× M3 profundidad 3,5 mm
* - Peso
  - 88 g
```
```{warning}
**Fijación:**
- Utilice los 4 orificios de montaje M3 del cuerpo de la cámara
- Tornillos recomendados: M3 A2 / M3 8.8
- Par de apriete: 0.5 Nm (no apretar demasiado para evitar deformaciones)
```
```{tip}
**Ajuste de la posición de la cámara**

Para permitir futuros ajustes y evitar problemas de alineación, diseñe el soporte mecánico con posibilidades de microajuste en todos los ejes:

- **Eje Z (altura)**: -10 mm / +30 mm
- **Eje X (izquierda-derecha)**: ±10 mm
- **Eje Y (adelante-atrás)**: ±10 mm

Un soporte con tornillos permanentemente apretados sin posibilidad de ajuste hace imposible corregir la posición de la cámara tras el montaje inicial.
```
### *Comprobación del montaje de la lente*

```{warning}
Antes de proceder con la fijación definitiva:
1. Verificar visualmente que la lente esté instalada
2. Comprobar que la longitud focal sea correcta para su modelo de FlexiBowl® (etiqueta en la lente o documentación del pedido)
3. Asegurarse de que la lente esté completamente enroscada (contacto metal-metal entre la lente y el cuerpo de la cámara)
4. NO retirar ni aflojar la lente si ya está montada correctamente
```
### *Instalación de la cámara*
Para garantizar el correcto funcionamiento del sistema de visión, la cámara debe instalarse sobre un soporte rígido y estable.
El sistema FlexiBowl® no genera vibraciones; sin embargo, en las líneas automatizadas existen otras fuentes de vibración (robots industriales, sistemas de manipulación, otras máquinas de la línea)

Si tales vibraciones se transmiten a la cámara, la imagen capturada puede ser inestable y las coordenadas calculadas por el sistema de visión pueden no ser fiables, comprometiendo la precisión de la recogida robótica.

![Instalación de la cámara](../../../../_shared/media/images/installazionecamera.png)

:::{tip}
Por este motivo se recomienda:

- instale la cámara en una estructura rígida y estable

- evitar soportes sometidos a vibraciones de robots u otras máquinas

- utilizar preferentemente una estructura independiente de la máquina
:::

```{warning}
**Tornillos de fijación de la cámara: prevención del aflojamiento**

Los tornillos de fijación de la cámara pueden aflojarse con el tiempo debido a las siguientes causas:

- **Par de apriete excesivo (> 0,5 Nm)**: puede provocar la deformación del cuerpo de la cámara y su posterior aflojamiento. Apriete siempre con un par máximo de **0,5 Nm.**
- **Vibración de la línea**: utilice **fijador de roscas medio** en todos los tornillos de fijación.
- Tornillos **inadecuados**: compruebe el uso de tornillos de **acero inoxidable M3 × 8 mm** como se recomienda.
```

### *Ajuste de la posición de la cámara:*

El soporte de la cámara debe permitir ajustar la posición para permitir una alineación correcta con la zona de recogida del FlexiBowl®.

![Ajustes de la cámara](../../../../_shared/media/images/regolazionicamera.png)

:::{note}
Partiendo de una posición nominal con inclinación, altura y posicionamiento correctos en el centro del área retroiluminada, se recomienda prever los siguientes ajustes:

Ajuste X/Y → ± 50mm
Ajuste Z → ± 50mm
Rotación θ → ± 10°
:::

```{caution}
**Cámara dañada durante el montaje**

Para evitar daños en la cámara durante la instalación y el ajuste:

- Par de **apriete excesivo**: no sobrepasar un par de **0,5 Nm** en los tornillos M3. Superar este valor puede deformar irreversiblemente el cuerpo óptico.
- **Manipulación indebida**: Manipule siempre la cámara con cuidado, evitando ejercer presión directa sobre el cuerpo óptico y el sensor.
- **Impactos durante la instalación**: proteja la cámara durante cualquier trabajo mecánico circundante (taladrado, fresado, tensado de estructuras).
```
---

## Montaje Toplight

Si el pedido incluye un Toplight (iluminador desde arriba), éste debe montarse en la misma estructura de soporte que la cámara para garantizar una iluminación uniforme de la superficie de trabajo.

:::{attention}
Durante el montaje, el equipo debe estar apagado y desconectado de la corriente.
:::
### *Dimensiones del Toplight*
![Dimensiones del Toplight](../../../../_shared/media/images/toplight_dim.JPG)

| Longitud x Anchura (mm)| Altura (mm)| Altura con placa de fijación (mm)| Diámetro del orificio central| Superficie útil máxima \[A x B]| Perímetro útil máximo
|:---:|:---:|:---:|:---:|:---:|:---:|
| **A x B**| **C**| **C + 10 mm**| **D**| **-**| **-**
| 500x300| 45| 55| 65| 0,15 m²| 1,6 m
| 700x300| 45| 55| 65| 0,21 m²| 2 m
| 700x500| 45| 55| 65| 0,35 m²| 2,4 m
| 900x600| 45| 55| 65| 0,54 m²| 3 m

### *Posicionamiento del Toplight*
El toplight debe colocarse centrado respecto a la superficie útil del panel luminoso,
con la óptica de la cámara montada en el interior del orificio central, a ras de la superficie superior del toplight.
Las flechas rojas indican los tornillos para fijar los anillos del objetivo, uno para ajustar el enfoque y otro para ajustar el diafragma. Como se muestra en la figura, el Toplight superior debe montarse de modo que los dos tornillos queden accesibles desde arriba.

![Toplight y posición de la leva](../../../../_shared/media/images/posizione_cam_TPL_B.png)

El campo de visión de la cámara y el haz luminoso de la Toplight (en verde) deben estar alineados concéntricamente y perpendicularmente a la zona de visión en el FlexiBowl®.
Como se muestra en las tres vistas (frontal, superior y axonométrica), el toplight debe iluminar exactamente la zona encuadrada por la cámara, con ambos componentes centrados en el eje óptico vertical del sistema.

![Toplight Cam + posición FB](../../../../_shared/media/images/posizioneTPL_giusta.png)

La colocación incorrecta se produce cuando la Toplight y la cámara no están centradas en la zona de visión del FlexiBowl®.
Como se ilustra (en rojo), dos errores típicos son:
- avanzar o retroceder en relación con el área de visión.
- girar el Toplight en relación con él.
  
En ambos casos, la iluminación está desplazada y no es perpendicular, lo que compromete la calidad de la adquisición.

![Toplight Cam + FB Posición incorrecta](../../../../_shared/media/images/posizioneTPL_sbagliata.png)

### *Procedimiento de instalación*
```{list-table}
:header-rows: 1
:widths: 35 65

* - **Fase**
  - **Instrucciones de uso**
* - **1. Posicionamiento**
  - Fije el Toplight en la estructura de soporte en posición concéntrica con respecto a la cámara.
* - **2. Distancia de la superficie**
  - Coloque el iluminador a una distancia de la superficie del FlexiBowl® similar a la de la cámara para:
    
    * Minimizar las sombras proyectadas por las piezas
    * Maximizar la uniformidad de la luz
    * Evitar los reflejos directos hacia la cámara
* - **3. Orientación**
  - Asegúrese de que la superficie emisora del Toplight esté paralela a la superficie de trabajo del FlexiBowl®.
* - **4. Ángulo de iluminación**
  - Perpendicular a la superficie (0° de inclinación).
* - **5. Fijación**
  - Según especificaciones del modo elegido (ver apartado siguiente).
```

### *Modos de fijación*

El Toplight puede fijarse de dos maneras: en la [esquina](angolo) o en el [lateral](lato).

:::{note}
Los componentes de fijación **no están incluidos** en el suministro del Toplight. El montaje puede personalizarse en función de las necesidades de la instalación.

- Fijación en el lateral (ranura): tuercas M4 **suministradas**
- Fijación en la esquina: tornillos CHC M4x20 **no suministrados**

En ambos casos, se recomienda utilizar un **fijador de roscas** (no suministrado) para evitar que se aflojen con el tiempo. El par de apriete recomendado oscila entre **0,5 y 1,5 Nm.**
:::

(angolo)=
#### *1. Fijación en la esquina*

La fijación en la esquina se realiza con tornillos CHC M4x20 (no suministrados) aplicados en los orificios de las cuatro esquinas del Toplight.
```{figure} ../../../../_shared/media/images/fissaggio_angolo.png
:alt: Fijación del Toplight en la esquina con tornillo CHC M4x20
:align: center
:width: 60%

Fijación en la esquina mediante tornillo CHC M4x20 (no suministrado).
```

(lato)=
#### *2. Fijación lateral (ranura)*

Para la fijación lateral se utilizan 4 tuercas M4 (suministradas) que se introducen en la ranura lateral del perfil Toplight.
   La profundidad máxima de inserción de la tuerca en la ranura es de **5 mm.**
     Los tornillos recomendados son M4x8.

```{figure} ../../../../_shared/media/images/fissaggio_lato.JPG
:alt: Fijación del Toplight en el lateral
:align: center
:width: 100%

Fijación lateral
```
(montaggio_staffa)=
##### Fijación lateral con soportes
Si el Toplight se fija con soportes:

:::{error}
![Montaje lateral](../../../../_shared/media/images/errorimontaggiolaterale.png)
:::

:::{tip}
![Montaje lateral](../../../../_shared/media/images/montaggiolaterale.png)
:::

:::{card}
  Para el montaje lateral es posible adquirir **por separado** el correspondiente [soporte](staffa).
:::



### *Cablado del iluminador*


![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Requisito / Acción
* - **Tensión**
  - 24V DC (±10%). Tensión mínima de funcionamiento: 20V DC en la entrada de luz.
* - **Conector**
  - M12 de 5 polos (codificación T).
* - **Pinout conector**
  - Pin 1: +24V (marrón) — Pin 3: GND (azul) — Pin 4: STROBE PNP (negro)
* - **Modo STROBE (PNP)**
  - 5V a 24V para un encendido al 100%. 0V a 1V para una desconexión del 100%.
* - **Modo CONTINUO**
  - Pin 1 (+24V) y Pin 3 (GND) conectados; Pin 4 (PNP) conectado al Pin 1.
* - **Caída de tensión (cable M12, 10m)**
  - 1,15V @ 5A — 2,3V @ 10A — 3,5V @ 15A — 4,6V @ 20A (máx 20A)
* - **Blindaje**
  - Utilice cables blindados para reducir las interferencias electromagnéticas (EMI).
```
```{warning}
**Seguridad eléctrica**

- Observe las tensiones de alimentación y los bornes de conexión indicados.
- No modifique ni desmonte el producto.
- No conecte ni limpie el aparato cuando esté bajo tensión.
- No mires directamente a la fuente de luz.
```
```{note}
Para más detalles sobre las conexiones eléctricas, consulte la sección [Cableado y conexiones](10_Cablaggio_Connessioni.md).
```
---

## Disposición completa

```{raw} html
<div style="
    border: 2px solid #0d6efd;
    border-radius: 8px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
    background-color: #f0f6ff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
">
    <div>
        <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem;">📐 Flexibowl General Layout.STEP</div>
        <div style="font-size: 0.95rem; color: #444;">Archivo CAD con el diseño completo de la disposición entre FlexiBowl®, Toplight y Cámara. Para utilizar en la integración mecánica del sistema.</div>
    </div>
    <a href="https://arsautomationsrl-my.sharepoint.com/:f:/g/personal/documentation_arsautomation_com/IgBMPLcyTzL8TbeSdjCwp6miAZlpuvrhEkqWnkK4AxLJEHU?e=gXEc2x" target="_blank" style="
        display: inline-block;
        padding: 0.7rem 1.4rem;
        background-color: #0d6efd;
        color: white !important;
        font-weight: 600;
        font-size: 1rem;
        border-radius: 6px;
        text-decoration: none !important;
        white-space: nowrap;
        flex-shrink: 0;
    ">⬇ Descargar</a>
</div>
```
---
(luce_ambientale)=
## Blindaje frente a la luz ambiental

La estabilidad del sistema de visión depende en gran medida de la constancia de las condiciones de iluminación. La variación de la luz ambiental puede provocar lecturas incoherentes.

El sistema de visión funciona comparando cada imagen adquirida con un modelo de referencia. Si las condiciones de iluminación varían entre exploraciones, el sistema puede tener dificultades para reconocer las piezas correctamente. La luz ambiental —solar, artificial o reflejada— que entra en la célula es la principal causa de inestabilidad del rendimiento en aplicaciones reales.

![Blindaje contra la luz ambiental](../../../../_shared/media/images/LIGHTSHIELDING.png)

### *Síntomas típicos de la luz ambiental incontrolada*

- **Reconocimiento inestable**: el sistema funciona bien en ciertos momentos y empeora en otros, por ejemplo, cuando entra luz solar en la célula.
- **Puntuación de reconocimiento variable**: las piezas se detectan con puntuaciones muy diferentes de un ciclo a otro, aunque sean físicamente idénticas.
- **Falsos positivos**: las piezas poco fiables se reconocen con puntuaciones altas y viceversa.

### *Mejores prácticas de instalación*

- Proteja los lados de la celda expuestos a una iluminación irregular con paneles opacos.
- Evite la iluminación artificial variable (lámparas con regulador de intensidad, fluorescentes parpadeantes) encima o cerca de la célula.
- Prefiera la iluminación de flujo constante en la zona que rodea la celda.
- Compruebe el apantallamiento antes de calibrar y crear el modelo.

```{warning}
**Protección frente a fuentes luminosas externas**

Las condiciones durante el calibrado deben ser las mismas que durante el funcionamiento normal. Se recomienda encarecidamente proteger la célula robotizada de:
- Luz solar directa o indirecta
- Iluminación artificial variable (por ejemplo, lámparas con regulador de intensidad)
- Reflejos de superficies brillantes circundantes
- Destellos o luces intermitentes en la zona
```
---

## Referencias relacionadas

Para más información sobre la instalación mecánica:

- **Cálculo de la distancia óptima de la cámara**: [Cálculo óptimo de la distancia](distanza_lavoro)
- **Especificaciones técnicas completas**: [Especificaciones FlexiVision One](specifiche_tecniche)
- **Siguiente paso - Conexiones eléctricas**: [Cableado y conexiones](cablaggio)
- **Calibración de la cámara**: [Calibración de la cámara](calibrazione)

