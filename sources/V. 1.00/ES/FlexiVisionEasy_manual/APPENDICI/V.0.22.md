# V. 0.22


## **Nuevas funcionalidades**

### Aplicaciones Mix

- Añadida la gestión combinada de los comandos `mix_Locator` para Robot 1, Robot 2 y Robot 3: ahora es posible llamar varios modelos simultáneamente dentro de una única cadena (p. ej. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
- Añadido un control de validez en los comandos `mix_Locator`: si la cadena recibida no contiene modelos válidos (del 1 al 8), el sistema devuelve un error específico.
- Añadida una protección en los comandos `start_Locator` y `mix_Locator`: si un Locator ya está en ejecución, el comando se ignora, evitando reinicios no deseados de la tarea y modificaciones imprevistas de los modelos activos.

### Clearances (Histogramas)

- Añadido el soporte para tres tipos de región para las herramientas Histogram — **Rectángulo**, **Sector anular** y **Círculo** — seleccionables mediante un menú específico en la página de la receta, para todos los modelos e histogramas disponibles.
- Actualizada la página Test Histogram para mostrar correctamente los nuevos tipos de región, dibujados en verde o rojo según el resultado del control.
- Añadida la visualización gráfica del índice Histogram y de las medidas principales de la región seleccionada.

### FlexiBowl®

- Añadida la función **Belt Check** para controlar el estado de desgaste y limpieza de la cinta:
  - adquisición de una imagen de referencia de la cinta limpia mediante el botón **Save Clean Reference**;
  - comparación automática, mediante Histogram, entre la imagen de referencia y la imagen actual de la cinta;
  - clasificación automática de la cinta en **Light**, **Dark** o **Medium** según el brillo de la referencia;
  - visualización del estado de la cinta con valor porcentual, color e indicación textual (**Good**, **Warning**, **Poor**);
  - visualización de la fecha del último Belt Check de cada FlexiBowl®.
- Añadido el procedimiento guiado **Hopper Step Setup** para calcular el número de secuencias necesarias para alcanzar la zona de la tolva, con las funciones **Reset Steps**, **Test Sequence** y **Save Hopper Step**, y la correspondiente indicación del estado de calibración.
- Añadida la posibilidad de introducir manualmente desde el teclado los parámetros de los FlexiBowl®, como alternativa al ajuste mediante slider.
- Añadido un mensaje de aviso no modal cuando los parámetros de un FlexiBowl® se modifican pero aún no están sincronizados con el dispositivo real.
- Añadido el **Auto Reset FlexiBowl**: si al iniciar un comando de movimiento ya hay un error, el sistema realiza automáticamente el reset antes de iniciar el comando.

### Seguridad y accesos

- Añadido el control del nivel de acceso en los botones comunes de la interfaz: las funciones protegidas verifican el nivel de usuario actual antes de ejecutarse y muestran un mensaje en caso de permisos insuficientes.

## **Mejoras**

### Asistente de creación de recetas

- Añadido un control sobre el Picking Offset en el botón **NEXT**: si el offset está habilitado, debe estar calculado y ser válido antes de poder continuar en el asistente.

### Interfaz de la receta

- Corregido el formato de visualización de los offsets Robot Pick en las páginas de la receta, forzando el punto como separador decimal en lugar de la coma.

## **Problemas resueltos**

### Gestión de copias de seguridad (BackUp)

- Corregido un error en la creación de la copia de seguridad que se producía cuando la ruta en el PC contenía espacios.

### Secuencias

- Resuelto un problema de visualización que podía mostrar comandos aparentemente duplicados en la lista de secuencias.
