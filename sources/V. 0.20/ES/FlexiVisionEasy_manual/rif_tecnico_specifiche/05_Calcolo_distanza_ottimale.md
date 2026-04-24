(distanza_lavoro)=
# **Cálculo de la Distancia de Trabajo Óptima**

Esta sección define la distancia de trabajo (Working Distance) recomendada entre la cámara y el plato FlexiBowl, junto con la consiguiente selección de los objetivos necesarios para garantizar el correcto Campo Visual (Field of View, FOV).

La elección correcta de la distancia de trabajo y del objetivo es fundamental para:
- Garantizar que toda la superficie útil del FlexiBowl sea visible
- Obtener la resolución necesaria para detectar las piezas
- Minimizar las distorsiones ópticas
- Facilitar la calibración del sistema

---

## Distancias de trabajo recomendadas y selección de objetivos

La elección del objetivo depende estrechamente de la distancia de montaje recomendada entre la cámara y la superficie del plato FlexiBowl. Mantener la distancia de trabajo estándar garantiza el FOV correcto y minimiza los problemas de distorsión óptica.


```{note}
**Objetivo ya incluido**

El objetivo adecuado para el modelo FlexiBowl especificado en el pedido siempre está incluido en el paquete FlexiVision One y se suministra en un embalaje separado respecto a la cámara. No es necesario comprarlo por separado.
```

### Esquema de distancias y campo visual

El siguiente diagrama ilustra la relación entre distancia de trabajo, distancia focal del objetivo y área de visión resultante para los distintos modelos de FlexiBowl.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distancia De Trabajo
:width: 40%
:align: center
```

**Leyenda del esquema:**
- **Distancia de Trabajo**: Distancia vertical entre la cara frontal del objetivo y la superficie del plato FlexiBowl
- **Área de visión**: Zona de la superficie del FlexiBowl cubierta por el campo visual de la cámara

### Tabla resumen por modelo

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modelo FlexiBowl
  - Distancia de Trabajo Recomendada (Working Distance)
  - Objetivo Incluido en el Kit (Distancia Focal)
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

```{warning}
**Importancia de la distancia correcta**

Desviaciones significativas respecto a la distancia de trabajo recomendada pueden causar:

- **Distancia demasiado corta**: FOV insuficiente (parte del FlexiBowl no visible).
- **Distancia demasiado larga**: Resolución insuficiente para detectar piezas pequeñas, desenfoque

Respetar siempre las distancias indicadas en la tabla durante el montaje mecánico de la cámara.
```
### Posicionamiento Cámara 

**Configuración correcta.** La cámara debe posicionarse centralmente y con la misma orientación angular respecto al área de visión del FlexiBowl (zona backlight). De este modo, el campo visual (indicado en verde) cubre simétricamente toda el área de trabajo, garantizando el correcto funcionamiento del sistema de visión.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distancia De Trabajo
:width: 70%
:align: center
```

**Configuraciones incorrectas.** Las imágenes muestran ejemplos de posicionamiento incorrecto de la cámara: el campo visual (indicado en rojo) resulta descentrado respecto al área de visión, cubriendo solo parcialmente el área de trabajo o incluyendo zonas externas a ella. Estas configuraciones comprometen el reconocimiento de las piezas y el funcionamiento del sistema de visión.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distancia De Trabajo
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distancia De Trabajo
:width: 60%
:align: center
```
---

## Posicionamiento TopLight 

Si el sistema incluye un TopLight (iluminador desde arriba), su posicionamiento debe tener la misma orientación angular que la cámara para garantizar una iluminación uniforme. Debe instalarse en un soporte mecánicamente independiente del soporte de la cámara, de modo que para retirar o sustituir el sistema de iluminación no sea necesario aflojar ni desmontar la cámara.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Valor Recomendado
* - **Distancia desde la superficie FlexiBowl**
  - Similar a la Working Distance de la cámara (±100 mm)
* - **Posición respecto a la cámara**
  - Concéntrica (mismo eje óptico que la cámara)
* - **Orientación**
  - Paralela a la superficie del FlexiBowl y misma orientación angular de la cámara (Lado largo área de visión - Lado largo de iluminación)
* - **Altura relativa cámara-TopLight**
  - Óptica de visión a ras de la superficie superior Top Light (dejar libre acceso a los anillos de regulación de la óptica de visión)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Distancia De Trabajo
    :width: 80%
    :align: center
    :::
```

```{tip}
Para obtener la mejor uniformidad de iluminación, seguir las indicaciones recién indicadas 
```

```{warning}
**Evitar reflexiones directas**

Al posicionar el TopLight, asegurarse de que:

- La luz no se refleje directamente desde la superficie del FlexiBowl hacia la cámara (causando deslumbramiento)
- No haya sombras causadas por componentes mecánicos
- La iluminación sea lo más uniforme posible en toda la superficie útil

```

---

## Referencias relacionadas

Para completar la instalación y la configuración del sistema:

- **Instalación mecánica cámara**: [Instalación Mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Especificaciones técnicas cámara**: [Especificaciones FlexiVision One](04_Specifiche_FlexiVision.md)
- **Calibración sistema**: [Calibración de la Cámara](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Cableado eléctrico**: [Cableado y Conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

