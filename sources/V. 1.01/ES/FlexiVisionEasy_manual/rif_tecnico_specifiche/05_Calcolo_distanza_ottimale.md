(distanza_lavoro)=
# **Calcular la distancia óptima de trabajo**

Esta sección define la distancia de trabajo recomendada entre la cámara y la superficie de trabajo del FlexiBowl, junto con la consiguiente selección de objetivos necesarios para garantizar el campo de visión (FOV) correcto.

La elección correcta de la distancia de trabajo y del objetivo es crucial para:
- Garantizar la visibilidad de toda la superficie útil del FlexiBowl®
- Obtener la resolución necesaria para detectar piezas
- Minimizar las distorsiones ópticas
- Facilitar la calibración del sistema

---

## Distancias de trabajo recomendadas y selección de objetivos

La elección del objetivo depende estrictamente de la distancia de montaje recomendada entre la cámara y la superficie de trabajo FlexiBowl®. Mantener la distancia de trabajo estándar garantiza el FOV correcto y minimiza los problemas de distorsión óptica.


```{note}
**Lente ya incluida**

El objetivo adecuado para el modelo de FlexiBowl® especificado en el pedido se incluye siempre en el paquete de FlexiVision One y se suministra en un paquete separado de la cámara. No es necesario adquirirlo por separado.
```

### *Esquema de distancias y campo visual*

El siguiente diagrama ilustra la relación entre la distancia de trabajo, la distancia focal del objetivo y el área de visión resultante para los distintos modelos FlexiBowl®.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distancia de trabajo
:width: 40%
:align: center
```

**Leyenda del esquema:**
- **Distancia de trabajo**: Distancia vertical entre la lente de la cámara y la superficie de trabajo del FlexiBowl®
- **Área de visión**: Área de la superficie FlexiBowl® cubierta por el campo de visión de la cámara

### *Cuadro recapitulativo por modelo*

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

```{warning}
**Importancia de la distancia correcta**

Las desviaciones significativas de la distancia de trabajo recomendada pueden provocar:

- **Distancia demasiado corta**: FOV insuficiente (parte del FlexiBowl® no visible).
- **Distancia demasiado larga**: Resolución insuficiente para detectar piezas pequeñas, desenfoque

Al montar mecánicamente la cámara, respete siempre las distancias indicadas en la tabla.
```
### *Posicionamiento de la cámara*

**Configuración correcta.** La cámara debe colocarse centrada y con la misma orientación angular respecto al área de visión del FlexiBowl® (zona backlight). De este modo, el campo de visión (mostrado en verde) cubre simétricamente toda la zona de trabajo, garantizando el correcto funcionamiento del sistema de visión.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distancia de trabajo
:width: 70%
:align: center
```

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
---

## Posicionamiento TopLight 

Si el sistema incluye un TopLight (iluminador desde arriba), su posicionamiento debe tener la misma orientación angular que la cámara para garantizar una iluminación uniforme. Debe instalarse en un soporte que sea mecánicamente independiente del soporte de la cámara, de modo que ésta no tenga que aflojarse o desmontarse para retirar o sustituir el sistema de iluminación.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Valor recomendado
* - **Distancia desde la superficie FlexiBowl®**
  - Similar a la Working Distance de la cámara (±100 mm)
* - **Posición respecto a la cámara**
  - Concéntrica (mismo eje óptico de la cámara)
* - **Orientación**
  - Paralela a la superficie del FlexiBowl® y con la misma orientación angular de la cámara (lado largo del área de visión - lado largo de iluminación)
* - **Altura relativa cámara-TopLight**
  - Óptica de visión a ras de la superficie superior del Top Light (dejar libre acceso a las virolas de regulación de la óptica de visión)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Distancia de trabajo
    :width: 80%
    :align: center
    :::
```

```{tip}
Para obtener la mejor uniformidad de iluminación, seguir las indicaciones que se acaban de proporcionar 
```

```{warning}
**Evitar reflejos directos**

Al colocar el TopLight, asegúrese de que:

- La luz no se refleja directamente desde la superficie del FlexiBowl® hacia la cámara (causando deslumbramiento)
- No hay sombras causadas por componentes mecánicos
- La iluminación es lo más uniforme posible en toda la superficie útil

```

---

## Referencias relacionadas

Para completar la instalación y configuración del sistema:

- **Instalación mecánica de la cámara**: [Instalación mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Especificaciones técnicas de la cámara**: [Especificaciones de FlexiVision One](04_Specifiche_FlexiVision.md)
- **Calibración del sistema**: [Calibración de la cámara](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Cableado eléctrico**: [Cableado y conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

