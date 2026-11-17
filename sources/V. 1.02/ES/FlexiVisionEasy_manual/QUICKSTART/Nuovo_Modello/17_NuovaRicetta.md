(nuovaricetta)=
# **Crear una nueva receta**

Esta sección describe cómo crear una nueva receta de aplicación en FlexiVision One. Una receta es el contenedor principal que incluye todos los modelos de piezas, las configuraciones de FlexiBowl®/Hopper y los parámetros del robot necesarios para una aplicación de picking completa.
```{note}
**Crear una nueva receta cuando:**

- Trabaja con un **tipo de pieza completamente diferente**
- Cambia de **aplicación**

**NO es necesario crear una nueva receta cuando:**
- Añade una cara de la misma pieza (crea un nuevo modelo en la misma receta para la misma pieza en diferentes posiciones)
- Realiza pequeños ajustes en los parámetros existentes (exposición de la cámara)
- Sólo cambia el umbral de aceptación, el umbral de puntuación, etc.
```

---

## Vista general de la interfaz

Antes de proceder al entrenamiento del modelo, familiarícese con la interfaz [Recipes](recipes).

![Recetas](../../../../../_shared/media/images/pagina_recipesNEW.png)

## Guardar receta básica

Antes de continuar, asegúrese de haber guardado la receta básica creada durante la configuración inicial:
:::{list-table}
  * - **1**
    - Desde la página principal, haga clic en <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
  * - **2**
    - Compruebe que la receta actual es la receta básica (p. ej.: "Receta_Base" creada durante la configuración)
  * - **3**
    - Haga clic en <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon">
  * - **4**
    - Mantenga el mismo nombre en el campo guardar (está sobrescribiendo la receta con las configuraciones actualizadas)
  * - **5**
    - Confirme guardar
:::
```{important}

**¿Por qué guardar la receta básica?**

La receta básica contiene todas las configuraciones de hardware realizadas durante la instalación:
- Conexión FlexiBowl® (IP, parámetros)
- Conexión tolva
- Conexión robot (puerto TCP/IP)
- Calibración cámara

Disponer de una receta básica ya hecha permite reutilizar todas estas configuraciones sin tener que repetirlas.
```

---
## Paso 1: Duplicar la receta básica

Para empezar con la creación del primer modelo y, por tanto, con la configuración de una nueva aplicación, siempre es aconsejable duplicar la receta básica que acaba de guardar.
Esto es útil porque le permite guardar por separado todas las configuraciones nuevas. Y esto es ventajoso por dos razones:
- Para iniciar una nueva aplicación con el mismo sistema, no tiene que repetir todos los pasos que ha realizado hasta ahora
- Si sólo cambia un elemento de la configuración, puede mantener las configuraciones de todos los demás componentes
```{list-table}
* - **6**
  - Desde la página principal del software FlexiVision One, haga clic en <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
* - **7**
  - Se abre la página de gestión de recetas con una lista de todas las recetas existentes
* - **8**
  - Seleccione la Receta Básica
* - **9**
  - Duplique la Receta Básica
* - **10**
  - Haga clic en Load Recipe
* - **11**
  - Compruebe en la barra superior que el nombre que aparece es el de la nueva receta
    :::{warning}
    **Trabaje siempre sobre la receta correcta**

    Con varias recetas presentes, compruebe siempre que se ha seleccionado la correcta antes de iniciar las modificaciones. Los cambios aplicados a una receta equivocada obligan a rehacer el trabajo.
    :::
```
## Paso 2: Poner nombre a la receta

Antes de hacer clic en "Guardar receta", elija un nombre descriptivo.
```{list-table}
* - **12**
  - Renombrar receta duplicada
    **Convenciones recomendadas:**
    - Nombres que identifiquen claramente la pieza o la aplicación
    - Sin espacios (utilice `_` o `-`)
    - Incluya la información pertinente (tipo de pieza, tamaño, aplicación)
    
    :::{tip}
    **Evitar nombres genéricos**

    ❌ Nombres a evitar:
    - `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

    ✓ Nombres recomendados:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    **Formato sugerido**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[GG_MM_AAAA]`

    Un nombre claro facilita la gestión cuando se tienen muchas recetas diferentes.
    :::
```
```{warning}
**Recetas de reserva**

Después de crear y configurar una receta:
- Utilice la función de copia de seguridad del software ([Gestión de copias de seguridad](backup))
- Exporte periódicamente las recetas a soportes externos
- Documente los parámetros críticos en papel o soporte digital

Una receta bien configurada representa horas de trabajo. Protegerla adecuadamente evita la pérdida de datos.
```

---

## Próximos pasos

- **[Creación de un modelo](18_NuovoModello.md)**
- **[Definición del ROI](roitest)**
- **[Configuración de Clearances](istogrammi)**
- **[Calibración del robot](robotpick)**

```{tip}
**Qué se necesita para el siguiente paso**

- Piezas físicas a reconocer (al menos 10-15 piezas)
- FlexiBowl® vacío y limpio
- Si la herramienta robótica que vamos a utilizar es una pinza, necesitaremos también dos objetos distintos de las piezas a modelar para utilizarlos como simuladores de la huella de la herramienta.
- Hoja para anotar las coordenadas del robot (X, Y, RZ)
```
