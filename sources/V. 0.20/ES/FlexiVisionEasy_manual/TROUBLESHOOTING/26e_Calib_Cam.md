(troubleshooting_calib_cam)=
# **Calibración Cámara**

## **Pattern no detectado**

```{warning}
**Error: "Unable to detect calibration pattern"**

Causa: El software no consigue identificar el pattern de la rejilla.

**Soluciones**:
- Aumentar el contraste (regular exposición o iluminación)
- Verificar que toda la rejilla sea visible en la imagen
- Mejorar el enfoque
- Limpiar la superficie de la rejilla (polvo o huellas pueden interferir)
- Verificar que la rejilla sea la correcta (cuadrados, no círculos u otros patterns)
```

## **Calibración siempre "Bad" o "Acceptable"**

```{warning}
**Calidad de calibración insuficiente**

Si a pesar de los ajustes la calibración permanece por debajo de "Excellent":

1. Verificar la distancia de trabajo cámara-FlexiBowl (debe ser la calculada)
2. Controlar que la cámara sea paralela respecto al plano del FlexiBowl (debe estar perfectamente horizontal)
3. Asegurarse de que la cámara esté estable (sin vibraciones durante la adquisición)
4. Verificar que el objetivo esté completamente enroscado 

Si el problema persiste, podría haber un problema mecánico en el montaje. Consultar [Instalación Mecánica]009_Installazione_Meccanica.md) para revisión.
```

## **Errores después de cambio de iluminación**

```{tip}
**Recalibración después de cambio backlight/toplight**

Si se pasa de backlight a toplight (o viceversa):

1. La calibración geométrica sigue siendo válida (no es necesario repetirla)
2. Solo es necesario regular la exposición de la cámara para el nuevo tipo de iluminación
3. Adquirir una imagen de prueba para verificar que el pattern siga siendo bien visible

En general, se recomienda decidir desde el principio el tipo de iluminación que se va a utilizar y mantener esa configuración.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles Causas
  - Soluciones
* - **Calibración falla (error software)**
  - • Rejilla de calibración no detectada correctamente
    
    • Iluminación insuficiente/excesiva
    
    • Rejilla de calibración dañada o sucia
    
  - • Posicionar el target plano y bien visible
    
    • Regular la exposición de la cámara para visualizar bien el target
    
    • Utilizar rejilla de calibración limpia e íntegra
    
* - **Error de calibración demasiado elevado**
  - • Cámara no perfectamente ortogonal a la superficie
    
    • Rejilla de calibración no plana
    
    • Distorsión óptica excesiva
    
  - • Verificar ortogonalidad cámara con nivel (tolerancia ±1°)
    
    • Posicionar el target sobre superficie rígida y plana
    
    • Verificar calidad óptica del objetivo, limpiar o sustituir
    
* - **Coordenadas reales no corresponden a las medidas**
  - • Factor de escala incorrecto (Tile Size incorrecto)
    
    • Cámara desplazada después de calibración
    
  - • Repetir calibración completa
    
    • Fijar firmemente la cámara para evitar desplazamientos
    
    • Verificar dimensiones target calibración según documentación
* - **Calibración válida solo en el centro de la imagen**
  - • Distorsión óptica periférica
    
    • Calibración con demasiado pocos puntos
  - • Utilizar objetivo de calidad superior con baja distorsión
    
    • Verificar que la distancia de trabajo sea correcta
```



