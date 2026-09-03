# **Creación de recetas y modelos** 

(troubleshooting_nuova_ricetta)=
## Solución de problemas para la sección Creación de una nueva receta 

```{warning}
**Error durante el guardado**

Si guardar la receta falla:
- Compruebe que hay espacio suficiente en el disco 
- Asegúrese de que el nombre no contiene caracteres no permitidos (` \ : * ? " < > |`)
- Compruebe que no existe ya una receta con el mismo nombre
- Compruebe que tiene permiso de escritura en la carpeta de software
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **No se puede crear una nueva receta**
  - • Disco lleno
    
    • El nombre de la receta contiene caracteres inadmisibles
  - • Libere espacio en disco
    
    • Evite los caracteres especiales en el nombre (`/ \ : * ? " < > |`)

* - **Receta guardada pero configuraciones perdidas**
  - • Guardado no confirmado correctamente
    
    • Apagado forzado del software
    
    • Error de escritura en disco
  - • Haga siempre clic en "Guardar receta" y espere la confirmación
    
    • Cierre el software correctamente
    
    • Compruebe el registro de errores de Windows
* - **No se puede cargar la receta creada**
  - • Archivo de receta corrupto
    
    • Ruta de archivo modificada
  - • Restaure desde copia de seguridad si está disponible
    
    • Compruebe la ruta de la carpeta de recetas en la configuración
* - **La receta cargada tiene una configuración incorrecta**
  - • Receta incorrecta seleccionada
    
    • Cambios no guardados previamente
    
    • Conflicto entre recetas con nombres similares
  - • Compruebe el nombre de la receta en la barra superior
    
    • Recargue la receta correcta de la lista
    
    • Utilice convenciones de nomenclatura inequívocas
```

(troubleshooting_nuovo_modello)=
## Solución de problemas para la sección Creación de un nuevo modelo 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones

* - **Grab Train Image captura la imagen en negro**
  - • La cámara no está conectada
    
    • Toplight apagada

    • Retroiluminación apagada 
    
    • Exposición demasiado baja
    
    • Objetivo con tapa protectora
  - • Compruebe la conexión de la cámara en Configuración de la cámara
    
    • Encienda la Toplight y compruebe la alimentación

    • Compruebe que la marca Light On está activada en la configuración FlexiBowl®
    
    • Aumente la exposición de la cámara
    
    • Retire la tapa del objetivo
* - **El ROI no se mueve ni cambia de tamaño**
  - • Imagen no adquirida
    
    • Software bloqueado
  - • Ejecute Grab Train Image primero
    
    • Reinicie el software

* - **Apply Train no genera el modelo**
  - • ROI demasiado pequeño
    
    • Imagen sin suficiente contraste
  
  - • Amplíe el ROI para incluir todo el componente
    
    • Mejore el contraste/iluminación

* - **El modelo creado incluye la textura de la superficie**
  - • Umbral de características demasiado bajo
    
    • Contraste componente-superficie insuficiente
  - • Aumente el umbral de características (p. ej.: de 0,3 a 0,6)
    
    • Mejore la iluminación para aumentar el contraste
* - **El modelo creado tiene muy pocas líneas**
  - • Umbral de características demasiado alto
    
    • Imagen borrosa

    • Imagen sin suficiente contraste
  - • Disminuya el umbral de características (p. ej.: de 0,8 a 0,5)
    
    • Compruebe el enfoque de la cámara y corríjalo si es necesario

     • Mejore el contraste/iluminación

* - **El modelo incluye reflejos de luz**
  - • Umbral de características demasiado bajo
    
    • Iluminación no uniforme
    
  - • Aumente el umbral de características
    
    • Ajuste la posición/ángulo de la Toplight


* - **No se puede asignar nombre al modelo**
  - • El nombre contiene caracteres inadmisibles
    
    • Longitud del nombre excesiva
  - • Utilice solo letras, números, guiones bajos y guiones
    
    • Limite el nombre a un máximo de 50 caracteres
```

(troubleshooting_modelli_roi)=
## Solución de problemas para la sección Definición de ROI y tolerancias 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones

* - **La prueba no detecta ningún componente**
  - • Umbral de aceptación demasiado alto
    
    • Componentes fuera de la búsqueda de región
    
    • Modelo incorrecto
    
    • Iluminación modificada respecto al entrenamiento
  - • Disminuya el umbral de aceptación (p. ej.: de 0,90 a 0,75)
    
    • Amplíe la búsqueda de región para incluir componentes
    
    • Repita el entrenamiento del modelo
    
    • Estabilice la iluminación
* - **La prueba detecta demasiados falsos positivos**
  - • Umbral de aceptación demasiado bajo
    
    • Modelo demasiado simple/genérico
    
    • Hay componentes muy similares que presentan muchas diferencias a la vez
  - • Aumente el umbral de aceptación (p. ej.: de 0,70 a 0,85)
    
    • Rehaga el modelo con un umbral de características más bajo (más detallado)
    
    • Separe en modelos distintos si es necesario
* - **La prueba detecta componentes pero con puntuación demasiado baja**
  - • Variabilidad de componentes reales frente al modelo de entrenamiento
    
    • Iluminación diferente
    
    • Componentes sucios/dañados
    
    • Modelo demasiado detallado
  - • Compruebe la calidad de los componentes y límpielos si es necesario
    
    • Estandarice la iluminación
    
    • Descarte los componentes dañados
    
    • Rehaga el modelo con un umbral de características más alto (menos detallado)

* - **Panel de resultados vacío incluso con componentes visibles**
  - • Ningún componente supera el umbral de aceptación
    
    • La búsqueda de región no incluye componentes
    
    • Prueba no ejecutada
  - • Disminuya el umbral de aceptación
    
    • Compruebe y amplíe la búsqueda de región
    
    • Haga clic en el botón Test
* - **Coordenadas X, Y, rotación incorrectas**
  - • Calibración de la cámara no realizada o realizada incorrectamente 
    
    • Sistema de referencia incorrecto
    
    • Cámara desplazada después de la calibración
  - • Realice la calibración completa de la cámara o revise la actual 
    
    • Compruebe el origen del sistema de coordenadas
    
    • Repita la calibración de la cámara
```

(troubleshooting_istogrammi)=
## Solución de problemas para la sección Histogramas 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **No se puede activar el histograma**
  - • Modelo no reconocido
    
    • Límite máximo de histogramas alcanzado (8 por modelo)
    
    • Ranura ya ocupada
  - • Complete la configuración del modelo antes
    
    • Desactive histogramas no utilizados
    
    • Seleccione una ranura libre

* - **AUTO no calcula correctamente**
  - • Área del histograma demasiado pequeña
    
    • Histograma fuera de la imagen
    
    • Imagen no cargada
  - • Amplíe el área del histograma
    
    • Mueva el histograma dentro del área visible
    
    • Adquiera una nueva imagen
* - **Prueba siempre ROJA incluso con área libre**
  - • Calibración AUTO realizada con área ocupada
    
    • Sombra o reflejo en el área
    
    • Borde FlexiBowl® incluido en el área
    
    • Suciedad en la superficie
  - • Repita AUTO con el área completamente libre
    
    • Excluya zonas con sombras/reflejos
    
    • Reduzca el área excluyendo bordes
    
    • Limpie la superficie FlexiBowl®
* - **Prueba siempre VERDE incluso con área ocupada**
  - • Calibración AUTO realizada con componentes ya presentes
    
    • Umbrales calculados incorrectamente
    
    • Contraste insuficiente
  - • Repita AUTO asegurándose de que el área esté completamente vacía
    
    • Repita la calibración con iluminación estable
    
    • Mejore el contraste de la iluminación
* - **El histograma se activa aleatoriamente**
  - • Área demasiado grande incluye zonas variables
    
    • Iluminación inestable
    
    • Umbral demasiado estricto
  - • Reduzca el área al mínimo necesario
    
    • Estabilice la iluminación
    
    • Repita la calibración AUTO
* - **El histograma no se activa cuando debería**
  - • Área demasiado pequeña no incluye el obstáculo
    
    • Umbral demasiado permisivo
    
  - • Amplíe el área del histograma
    
    • Repita la calibración AUTO con mayor contraste
    
* - **No se puede crear un segundo histograma para la pinza**
  -  • Ranura de histograma incorrecta seleccionada
  -  • Vuelva a la lista y seleccione Histogram 2
* - **La prueba de histogramas múltiples no funciona**
  - • No todos los histogramas están activados
    
    • Configuración incompleta
    
    • Conflicto entre histogramas
  - • Compruebe la activación de todos los histogramas necesarios
    
    • Complete la configuración AUTO para cada histograma
    
    • Compruebe que las áreas no se solapen
```

(troubleshooting_robot_pick)=
## Solución de problemas para la sección Calibración Robot Pick 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **Coordenadas del robot no disponibles (perdidas/olvidadas)**
  - • No anotadas durante la preparación física
    
    • Hoja de notas perdida
    
    • Coordenadas sobrescritas
  - • **OBLIGATORIO**: Repita toda la preparación física del punto 1 al punto 9 de [Creación de modelo](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)
    
    • Guarde las coordenadas en un archivo digital además de en papel
    
    • Fotografíe la pantalla del pendant del robot
* - **Find Object no detecta el componente**
  - • Componente de referencia desplazado
    
    • Umbral de aceptación demasiado alto
    
    • Componente fuera de la búsqueda de región
  - • Compruebe la posición del componente de referencia
    
    • Reduzca temporalmente el umbral de aceptación
    
    • Compruebe que la búsqueda de región incluye el componente
* - **Vision Result muestra coordenadas erróneas**
  - • Calibración de la cámara no realizada
    
    • Sistema de coordenadas no configurado
    
    • Cámara desplazada después de la calibración
  - • Realice la calibración de la cámara antes de Robot Pick
    
    • Compruebe el origen del sistema de referencia
    
    • Repita la calibración de la cámara
* - **No se pueden introducir las coordenadas del robot**
  - • Campos bloqueados
    
    • Enable Robot Pick no activado
    
    • Formato numérico incorrecto
  - • Haga clic en Enable Robot Pick primero
    
    • Active los campos haciendo clic sobre ellos
    
    • Utilice el punto como separador decimal
* - **Gripper Offset calcula valores incorrectos**
  - • Coordenadas del robot introducidas incorrectamente
    
    • X e Y intercambiados
    
    • Signo +/- incorrecto
    
    • Decimales incorrectos o aproximados
  - • **CRÍTICO**: Compruebe cuidadosamente cada coordenada
    
    • Compruebe el orden X, Y, RZ
    
    • Compruebe los signos de las coordenadas
    
    • Copie los valores exactamente como se anotaron, sin aproximaciones
* - **El robot recoge en posiciones incorrectas tras la calibración**
  - • Las coordenadas del robot anotadas eran incorrectas
    
    • Marco/herramienta del robot cambiados después de la anotación
    
    • El componente de referencia estaba desplazado durante la anotación
    
    • Gripper Offset no guardado
  - • Repita la preparación física comprobando marco/herramienta correctos
    
    • Asegúrese del mismo marco/herramienta para anotación y recogida
    
    • Repita la configuración con el componente correctamente posicionado
    
    • Guarde la receta tras calcular Gripper Offset
* - **Desplazamiento del robot válido solo para el componente de referencia**
  - • Distorsión óptica elevada
    
    • Calibración de la cámara imprecisa
    
    • Búsqueda de región demasiado grande respecto a la calibración
  - • Mejore la calibración de la cámara
    
    • Utilice un objetivo de baja distorsión
    
    • Reduzca la búsqueda de región si es posible
* - **No se puede guardar Gripper Offset**
  - • Receta no cargada
    
    • Permisos insuficientes
    
    • Disco lleno
  - • Compruebe que la receta está cargada correctamente
    
    • Compruebe los permisos de escritura
    
    • Libere espacio en disco
* - **Rotación RZ del robot siempre incorrecta**
  - • RZ del robot no estaba a 0° durante la configuración
    
    • Último eje del robot incorrecto
    
    • Sistema de coordenadas rotado
  - • Repita la configuración llevando el último eje del robot a RZ=0°
    
    • Compruebe que la herramienta seleccionada es correcta
    
    • Compruebe la orientación del sistema de coordenadas
```



