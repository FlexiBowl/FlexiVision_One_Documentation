(troubleshooting_conf_tramoggia)=
# **Configuración Hopper** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles Causas
  - Soluciones

* - **Área de control no definible**
  - • Imagen no adquirida
    
    • Sección incorrecta
  - • Adquirir imagen de prueba
    
    • Acceder mediante Config Hopper X


* - **AUTO no calcula Mean y Std Dev correctamente**
  - • CAPTURE no ejecutados
    
    • Orden de CAPTURE invertido
    
    • Área de control demasiado pequeña
  - • Ejecutar CAPTURE vacío y luego CAPTURE lleno
    
    • Repetir en el orden correcto
    
    • Ampliar el área de control
* - **TEST siempre VERDE (hopper no se activa nunca)**
  - • Umbral demasiado permisivo
    
    • CAPTURE lleno con demasiados componentes
    
    • Mean calculado incorrectamente
  - • Repetir CAPTURE lleno con el número mínimo correcto
    
    • Verificar que AUTO recalcula correctamente
    
    • Ajustar manualmente el umbral si es necesario
* - **TEST siempre ROJO (hopper se activa siempre)**
  - • Umbral demasiado restrictivo
    
    • CAPTURE vacío con componentes presentes
    
  - • Repetir CAPTURE vacío con el área completamente limpia
    
    • Repetir AUTO

* - **Tiempo de vibración no produce el efecto deseado**
  - • Valor demasiado bajo
    
    • Valor demasiado alto 
    
    • Nivel variable de la cuba del hopper
  - • Empezar con 500ms
    
    • Incrementar ±100ms para regular el flujo
    
    • **CRÍTICO**: Mantener carga constante en la cuba

* - **Hopper descarga en momentos incorrectos**
  - • Steps no correcto

    • Hardware del Controlador Hopper no configurado correctamente 

  - • Recalcular Steps

    • Comprobar las especificaciones de configuración en el [manual dedicado al Hopper]() 
```

