# V. 0.22


```{note}
Esta página corresponde a la versión **1.01** del presente manual, compatible con **FlexiVision Studio v0.21** y **v0.22**.
```

## **Nuevas funciones**

### Aplicaciones Mix

- Se ha añadido la gestión combinada de los comandos `mix_locator` para el Robot 1, el Robot 2 y el Robot 3: ahora es posible invocar varios modelos a la vez dentro de una misma cadena (por ejemplo, `mix_locator_12`, `mix_locator_248`, `mix_locator_12345678`).
- Se ha añadido una comprobación de validez para los comandos `mix_locator`: si la cadena recibida no contiene modelos válidos (del 1 al 8), el sistema devuelve un error específico.
- Se ha añadido una protección a los comandos `start_locator` y `mix_locator`: si un Locator ya se está ejecutando, el comando se ignora, lo que evita reinicios no deseados de la tarea y modificaciones imprevistas en los modelos activos.

### Clearances (Histogramas)

- Se ha añadido compatibilidad con tres tipos de regiones para las herramientas de histograma — **Rectángulo**, **Sector anular** y **Círculo** — que se pueden seleccionar a través de un menú específico en la página de recetas, para todos los modelos e histogramas disponibles.
- Se ha actualizado la página «Prueba de histograma» para mostrar correctamente los nuevos tipos de región, que se representan en verde o rojo según el resultado de la comprobación.
- Se ha añadido la visualización gráfica del índice del histograma y de las medidas principales de la región seleccionada.

### FlexiBowl®

- Se ha añadido la función **Belt Check** para comprobar el estado de desgaste y limpieza de la cinta:
  - captura de una imagen de referencia de la cinta limpia mediante el botón **Save Clean Reference**;
  - comparación automática, mediante un histograma, entre la imagen de referencia y la imagen actual de la cinta;
  - Clasificación automática de la cinta en **Light**, **Dark** o **Medium** en función de la luminosidad de la imagen de referencia;
  - Visualización del estado de la cinta con un valor porcentual, un color y una indicación textual (**Good**, **Warning**, **Poor**);
  - Visualización de la fecha de la última comprobación Belt Check para cada FlexiBowl®.
- Se ha añadido el asistente **Hopper Step Setup** para calcular el número de secuencias necesarias para llegar a la zona de la tolva, con las funciones **Reset Steps**, **Test Sequence** y **Save Hopper Step**, y la correspondiente indicación del estado de calibración.
- Se ha añadido la posibilidad de introducir manualmente desde el teclado los parámetros de los FlexiBowl®, como alternativa al ajuste mediante el control deslizante.
- Se ha añadido un mensaje de aviso no modal cuando se modifican los parámetros de un FlexiBowl® pero aún no se han sincronizado con el dispositivo real.
- Se ha añadido el **Auto Reset FlexiBowl**: si al iniciar un comando de movimiento ya existe un error, el sistema realiza automáticamente el reinicio antes de ejecutar el comando.

### Seguridad y accesos

- Se ha añadido el control del nivel de acceso en los botones comunes de la interfaz: las funciones protegidas comprueban el nivel de usuario actual antes de ejecutarse y muestran un mensaje en caso de permisos insuficientes.

## **Mejoras**

### Asistente de creación de recetas

- Se ha añadido un control sobre el desplazamiento de selección (Picking Offset) al botón **NEXT**: si el desplazamiento está habilitado, debe calcularse y ser válido antes de poder continuar en el asistente.

### Interfaz de recetas

- Se ha corregido el formato de visualización de los desplazamientos del robot de recogida en las páginas de recetas, estableciendo el punto como separador decimal en lugar de la coma.

## **Problemas resueltos**

### Gestión de copias de seguridad

- Se ha corregido un error en la creación de la copia de seguridad que se producía cuando la ruta en el ordenador contenía espacios.

### Secuencias

- Se ha solucionado un problema de visualización que podía hacer que aparecieran comandos aparentemente duplicados en la lista de secuencias.
