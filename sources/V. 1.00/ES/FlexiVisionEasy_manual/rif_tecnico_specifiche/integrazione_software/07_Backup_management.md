(backup)=
# **Gestión de copias de seguridad**

## Resumen

Toda la configuración de FlexiVision One — configuración de hardware, calibraciones, modelos de piezas y parámetros de protocolo — está contenida en los archivos de receta. Por esta razón, las copias de seguridad son esenciales para mantener todos los datos a salvo.

```{important}
Se recomienda realizar una copia de seguridad después de cada creación o modificación significativa de una receta, antes de actualizar el software FlexiVision y antes de cualquier intervención de hardware en el sistema.

**Regla mínima:** al menos una vez a la semana durante el funcionamiento normal.
```

---

## Procedimiento de copia de seguridad

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Paso**
  - **Acción**
* - Haga clic en Copia de seguridad
  - En el menú Recetas, haga clic en el botón Copia de seguridad.
* - Elija la carpeta FlexiVision
  - Localice la carpeta runtime de FlexiVision One en el VisionController.
* - Elija la carpeta de destino
  - Seleccione la carpeta de destino de la copia de seguridad.
* - Nomenclatura con fecha
  - Asigne siempre un nombre que incluya la fecha, la versión del software y el identificador del sistema u otra información útil, como el nombre del cliente. Ejemplos:
    
    - `FV_Recipes_LineA_20260402_SW1.2.xml`
    - `Backup_FlexiVision_ClientABC_Plant3_20260402.xml`
    - `Recipes_FB500_Commissioning_20260315_v1.zip`
    
    Incluya la versión del software (visible en la página de inicio) en el nombre o en un archivo de texto adjunto.
```

---

## Importar copia de seguridad

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Paso**
  - **Acción**
* - Haga clic en Importar copia de seguridad
  - En la sección Recetas, haga clic en Importar copia de seguridad.
* - Seleccione la carpeta runtime de FlexiVision
  - **Seleccione la carpeta que contiene la instalación de FlexiVision.**
* - Seleccionar ruta de copia de seguridad
  - Establezca la ruta del archivo de copia de seguridad. FlexiVision se reiniciará durante este proceso.
* - Comprobaciones posteriores a la recuperación
  - Tras la recuperación, realice las siguientes comprobaciones antes de reiniciar la producción:

    1. Compruebe que todas las recetas previstas aparecen en la página Recetas.
    2. Confirme que la receta principal puede cargarse sin errores.
    3. Compruebe que las pruebas de conexión del FlexiBowl® y de la cámara son positivas (verde) en Configuración de la cámara.
    4. Confirme que el panel de control muestra correctamente los dispositivos conectados.

    **Ejecute un ciclo de prueba con la receta de funcionamiento principal para verificar el funcionamiento correcto.**
```

---

## Gestión correcta de las recetas

```{list-table}
:header-rows: 1
:widths: 25 37 38

* - **Acción**
  - **Método correcto**
  - **Método a evitar**
* - Renombrar una receta
  - Página de recetas → función Renombrar en el software.
  - Cambie el nombre del archivo XML a través del Explorador de archivos.
* - Eliminar una receta
  - Página de recetas → botón **Borrar receta**.
  - Elimine el archivo XML manualmente.
* - Copiar una receta en otro sistema
  - Página de recetas → Backup → Import Backup en el otro sistema.
  - Copie y pegue los archivos XML entre dos carpetas Recipes.
* - Modificar un parámetro de receta
  - Abra la receta en modo **Edición** en el software.
  - Edite el archivo XML con un editor de texto.
```
