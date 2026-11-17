# V. 0.24

## **Nuevas funcionalidades**

### Cámaras de control

- Añadida la gestión de **3 cámaras de control** independientes, asociadas respectivamente a FLB1, FLB2 y FLB3.
- Implementado el comando de robot `start_control_` con soporte para parámetros personalizados, reenviados a los scripts de VisionPro.
- Añadida la gestión de scripts de VisionPro personalizables, con salida de texto e imágenes `CogRecord` que incluyen los resultados gráficos.
- Implementados Main Tasks dedicados a las cámaras de control, con gestión de errores, registro (logging) y envío de los resultados al robot.
- Habilitada la ejecución de los controles incluso sin robot conectado, para realizar pruebas locales desde la HMI.
- Añadidas páginas HMI compartidas para la configuración de la cámara, la configuración de VisionPro y la visualización runtime de las tres cámaras de control.

## **Mejoras**

### Clearances (Histogramas)

- Actualizada la gestión de regiones para los 8 modelos, los 8 Histogram y las 3 cámaras, preservando la posición, las dimensiones y la geometría de las ROI guardadas.

## **Problemas resueltos**

### Recetas

- Corregido el reinicio de las ROI de los Histogram al cambiar de receta.
