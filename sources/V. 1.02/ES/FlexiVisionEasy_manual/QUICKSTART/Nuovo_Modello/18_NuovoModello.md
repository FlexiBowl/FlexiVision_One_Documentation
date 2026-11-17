(nuovomodello)=
# **Crear un nuevo modelo**

En esta página veremos cómo crear un modelo de referencia para el reconocimiento de componentes.


## Paso 1: Preparación de la configuración física
Si aún no lo ha hecho, siga estos pasos:
````{list-table}
* - **1**
  - Retire la rejilla de calibración y restablezca la disposición inicial:
    - Vuelva a colocar la superficie
    - vuelva a colocar la brida central 
    - fije la brida central con sus cuatro tornillos
* - **2**
  - Coloque un objeto en el centro de la zona de visión
````
---

## Paso 2: Acceso al modelo

Una vez finalizada la preparación física, proceda a la adquisición de imágenes y creación de modelos
````{list-table}
* - **3**
  - Desde la página "Recipes", con la receta adecuada seleccionada, haga clic en <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
* - **4**
  - Seleccione el FlexiBowl® con el que está trabajando
    :::{dropdown} **Elección FlexiBowl®**
    ![Elección FB](../../../../../_shared/media/images/scelta_FB.png)
    :::
* - **5**
  - Se mostrarán las ranuras de modelos disponibles (hasta 8 modelos por receta)
* - **6**
  - Haga clic en **Modelo 1** para acceder a la página "Train Model 1 Cam 1"
````

### *Visión general de la interfaz Train Model*

![Página Modelo de tren](../../../../../_shared/media/images/pagina_trainmodel.png)
````{list-table}
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Función
* - **Enable Model**
  - Activa esta ranura de modelo haciéndola utilizable
* - **Grab Train Image**
  - Toma una imagen del componente de referencia para el entrenamiento
* - **Score Threshold**
  - Ajusta el nivel de detalle del modelo (de 0 = máximo detalle a 1 = mínimo detalle)
* - **Train**
  - Genera realmente el modelo procesando la imagen capturada
* - **Model Name**
  - Campo de texto para asignar un nombre descriptivo al modelo
````
````{tip}
**Gestión de modelos múltiples**

En esta fase sólo se activa el primer modelo. Una vez terminado, será posible:
- Habilitar ranuras adicionales (Modelo 2, Modelo 3, etc.) para diferentes piezas en la misma receta
- Modificar modelos existentes
- Deshabilitar modelos que ya no son necesarios

Por ahora, concéntrese en completar el primer modelo.
````
---

## Paso 3: Procedimiento de entrenamiento
````{video} ../../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
:width: 100%
:align: center 
````
````{list-table}
:widths: 5 95

* - **7**
  - Haga clic en **Enable Model** para activar este modelo. El modelo está ahora activo y listo para ser configurado.

* - **8**
  - Haga clic en **Grab Train Image** para tomar una fotografía del componente de referencia que hemos colocado en el FlexiBowl®
    
    :::{warning}
    El componente de referencia deberá permanecer inmóvil en ese punto durante todo el proceso de creación de la aplicación
    :::

* - **9**
  - Mueva el **cuadro ROI** para encuadrar completamente el componente

* - **10**
  - Mueva el **origen** (punto de referencia) al centro del área del marco
    
    :::{tip}
    **¿Dónde colocar el origen?**
    
    El origen se coloca automáticamente en el centro del componente.  
    Si el punto de agarre no coincide con el centro geométrico, mueva el origen al:
    - **Punto de agarre**: Para piezas asimétricas, colóquelo donde la pinza agarra
    
    *El origen define el punto (0,0) del sistema de coordenadas del modelo.*
    :::

* - **11**
  - Utilice el **Score Threshold** para ajustar el nivel de detalle deseado
    
    ::::{note}
    **Score Threshold**
     
      ![Comparación de umbral de puntuación](../../../../../_shared/media/images/confrontomodello.png)
    
    **Valor cercano a 0** → Detecta MÁS detalles (modelo más preciso)
    
    **Valor cercano a 1** → Detecta MENOS detalles (modelo más simple)
    ::::
    
    :::{tip}
    **¿Cómo elegir el Score Threshold óptimo?**
    
    **Usar valor BAJO (0.1-0.3) cuando:**
    - La pieza tiene muchos detalles distintivos (incisiones, logotipos, textura)
    - Las piezas son siempre muy similares entre sí (tolerancias estrechas)
    - Se desea máxima precisión incluso con orientaciones difíciles
    
    **Usar valor ALTO (0.4-0.6) cuando:**
    - La pieza tiene forma distintiva pero sencilla
    - Se desea equilibrio entre precisión y tolerancia
    - Primera configuración de un modelo (punto de partida)
    
    **Usar valor MUY ALTO (0.7-0.9) cuando:**
    - Hay variaciones significativas entre las piezas (tolerancias amplias)
    - La superficie de la pieza es muy reflectante o variable
    :::

* - **12**
  - Haga clic en **Train**
````
:::{tip}
Si tiene alguna duda durante la configuración, consulte el botón **INFO** de la página actual.
:::
---

## Paso 4: Inspección visual

Tras generar el modelo, es esencial comprobar su calidad antes de continuar.
````{list-table}

* - **13**
  - Haga **Zoom** en la imagen para inspeccionar los detalles del modelo creado y verificar que el modelo es correcto
    
    :::{tip}
      **Características de un modelo válido**  
      ✓ Tener suficientes líneas para reconocer el componente  
      ✓ No incluir la textura de la superficie de fondo  
      ✓ Evitar reflejos de luz  
    :::

    ![Comparación de modelos](../../../../../_shared/media/images/confrontomodello2.png)
````
````{attention}
Si el modelo no es satisfactorio:
- Modifique el **Score Threshold**
- Haga clic de nuevo en **Train**
- Repita hasta obtener un modelo óptimo
````
````{tip}
**Estrategia de optimización**

**Problema: El modelo incluye la textura de la superficie**  
→ Solución: Aumentar el Score Threshold o el valor Cam Exposure (SETUP > Camera Setup > Cam Exposure)

**Problema: El modelo tiene muy pocas líneas, no es distintivo**  
→ Solución: Disminuir el Score Threshold 

**Problema: El modelo incluye reflejos**  
→ Solución: Aumentar el Score Threshold o ajustar la exposición de la cámara

Realice cambios graduales (pasos de 0,1-0,2) y pruebe cada vez.
````
---

## Paso 5: Almacenamiento
````{list-table}
* - **14**
  - Denomine el modelo con un nombre descriptivo  
    :::{tip}
    **Evitar nombres genéricos**

    ❌ Nombres a evitar:
    - `Test`, `Prova`, `Modello1`, `Nuovo_Modello`

    ✓ Nombres recomendados:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    Un nombre claro facilita la gestión cuando se tienen muchos modelos diferentes.
    :::
* - **15**
  - Haga clic en <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → se abrirá la página **Define Robot Pick Area**  
````
````{seealso}
Proceda a [Definir ROI](roitest) para continuar con la configuración.
````

