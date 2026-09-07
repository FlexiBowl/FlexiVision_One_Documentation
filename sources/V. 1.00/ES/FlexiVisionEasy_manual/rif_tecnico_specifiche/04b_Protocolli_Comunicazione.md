(protocollo)=
# **Protocolo de comunicación Robot-Vision**

FlexiVision One se comunica con el robot mediante el protocolo **TCP/IP** a través de una red Ethernet.

## Especificaciones del protocolo

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parámetro
  - Valor
* - Protocolo
  - TCP/IP
* - Puerto
  - Configurable (predeterminado: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Carácter de terminación
  - CHR(13) - Retorno de carro
* - Formato de datos
  - Cadena ASCII
* - Timeout
  - Configurable (predeterminado: 5000 ms)
* - Codificación
  - UTF-8
```

## Comandos disponibles

El sistema admite los siguientes comandos mediante cadenas de texto enviadas a través de la conexión TCP/IP.

### *Gestión de recetas*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `set_recipe=<nombre>`
  - Carga la receta indicada e inicia la sincronización de los FlexiBowl® conectados.
  - Ninguno
* - `get_recipe`
  - Devuelve el nombre de la receta actualmente cargada.
  - `<nombre_receta>`
```

Ejemplo:

```
set_recipe=MyRecipe
```

o bien:

```
get_recipe
→ MyRecipe
```

### *Comandos de localización*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `start_Locator`
  - Inicia el proceso de localización de piezas. Si no hay piezas disponibles para recoger, se invoca automáticamente la rutina de movimiento del FlexiBowl®. Si el Locator ya está activo, el comando se ignora y el proceso no se reinicia.
    :::{important}
    Si en el momento del comando no hay ningún modelo seleccionado/habilitado, el sistema devuelve un mensaje de error y el Locator no se inicia.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Detiene el proceso de localización.
  - Ninguno
* - `turn_Locator`
  - Si no se ha recogido ninguna pieza, solicita un nuevo movimiento del FlexiBowl® y reinicia el proceso de búsqueda.
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Inicia la localización sin activar el FlexiBowl®; solo se realizan la adquisición de imagen y la búsqueda.
  - `Pattern_n;x;y;r` / Ninguno
* - `state_Locator`
  - Devuelve el estado de diagnóstico del proceso de localización.
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
* - `mix_Locator_<modelos>`
  - Selecciona dinámicamente uno o más modelos e inicia el Locator. Los modelos previamente seleccionados se deshabilitan primero. Los números disponibles van del 1 al 8 (ej. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
    :::{note}
    Si el Locator ya está en ejecución, el comando se ignora y la selección actual no se modifica.
    :::
  - Resultado normal del Locator / `#Error_mix_locator_not_valid` (si no se encuentra ningún modelo válido)
```

:::{note}
Otros separadores de cadena disponibles, además de `;`, son: `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

:::{note}
Para `start_Locator` y `mix_Locator_<modelos>`, cuando el Locator ya está en ejecución, no se envía ninguna respuesta al robot.
:::

### *Comandos FlexiBowl® – Emptying*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `start_Empty`
  - Inicia la secuencia de vaciado rápido (Quick-Emptying) del FlexiBowl®. El comando no se puede ejecutar mientras el Locator está activo.
  - `Start_Empty Started` / `Locator is Running` / `#Error_flexibowl_not_connect`
* - `stop_Empty`
  - Detiene la secuencia de vaciado del FlexiBowl®.
  - `Stop_Empty Command Sent` / `#Error_flexibowl_not_connect`
* - `state_Empty`
  - Devuelve el estado actual de la secuencia de vaciado.
  - `Emptying Running` / `Emptying Stopped` / `#Error_flexibowl_not_connect` / `#Error_invalid_emptying_state`
```

### *Señales opcionales de la tolva*

```{note}
Si es necesario activar la tolva, se recibirá la siguiente cadena: `"Hopper;signalnumber;time"`
```

## Errores generales

```{note}
**Licencia FlexiVision**: si la licencia del software no está activa, los comandos del robot se rechazan y se devuelve lo siguiente:
`#Error_License_not_active`
```

---

## Comandos Avanzados / Servicio

Los siguientes comandos están reservados al personal técnico y no forman parte de la documentación estándar para el cliente.

### *Conexión FlexiBowl®*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `connect_flb`
  - Solicita la conexión al FlexiBowl®. Si no está conectado, se inicia la tarea de conexión correspondiente.
  - `#Flb1_connected` / `#Flb1_Not_connected`
```

### *Comandos Láser*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `runlaser`
  - Inicia la tarea de adquisición/localización asociada al láser.
  - Ninguno
* - `stoplaser`
  - Solicita la detención de la tarea del láser.
  - Ninguno
```

---

Para obtener información detallada sobre la instalación física y las conexiones eléctricas, continúe con las siguientes secciones:
- [Cálculo de la Distancia Óptima de la Cámara](05_Calcolo_distanza_ottimale.md)
- [Instalación Mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Cableado y Conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
