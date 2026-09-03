(troubleshooting_conf_tramoggia)=
# **Configuración de la tolva** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones

* - **Área de control no definible**
  - • Imagen no adquirida
    
    • Sección incorrecta
  - • Adquiera una imagen de prueba
    
    • Acceda a través de Config Hopper X


* - **AUTO no calcula correctamente la media y la desviación estándar**
  - • CAPTURE no ejecutados
    
    • Orden de CAPTURE invertido
    
    • Área de control demasiado pequeña
  - • Ejecute CAPTURE vacío y luego CAPTURE lleno
    
    • Repita en el orden correcto
    
    • Amplíe el área de control
* - **TEST siempre VERDE (la tolva nunca se activa)**
  - • Umbral demasiado permisivo
    
    • CAPTURE lleno con demasiados componentes
    
    • Media calculada incorrectamente
  - • Repita CAPTURE lleno con el número mínimo correcto
    
    • Compruebe que AUTO recalcula correctamente
    
    • Ajuste el umbral manualmente si es necesario
* - **TEST siempre ROJO (la tolva siempre se activa)**
  - • Umbral demasiado restrictivo
    
    • CAPTURE vacío con componentes presentes
    
  - • Repita CAPTURE vacío con el área completamente limpia
    
    • Repita AUTO

* - **Tiempo de vibración no produce el efecto deseado**
  - • Valor demasiado bajo
    
    • Valor demasiado alto 
    
    • Nivel del depósito de la tolva variable
  - • Comience con 500 ms
    
    • Incremente ±100 ms para ajustar el flujo
    
    • **CRÍTICO**: Mantenga la carga constante en el depósito

* - **La tolva descarga en momentos incorrectos**
  - • Steps incorrecto

    • Hardware del controlador de tolva no configurado correctamente 

  - • Recalcule Steps

    • Compruebe las especificaciones de configuración en el [manual dedicado a la tolva]() 
```

