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
  - Configurable (por defecto: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Carácter de terminación
  - CHR(13) - Retorno de carro
* - Formato de datos
  - Cadena ASCII
* - Tiempo de espera
  - Configurable (por defecto: 5000 ms)
* - Codificación
  - UTF-8
```

## Comandos disponibles

El sistema admite los siguientes comandos mediante cadenas de texto enviadas a través de la conexión TCP/IP:

### *Gestión de recetas*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `set_Recipe=nome_ricetta`
  - Carga la receta correspondiente al "nombre_receta" especificado
  - Ninguno
* - `get_Recipe`
  - Devuelve el nombre de la receta cargada actualmente
  - `nome_ricetta`
```

### *Comandos de localización*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `start_Locator`
  - Inicia el proceso de localización de piezas. Si no hay piezas que puedan recogerse, invoca automáticamente la rutina de manipulación del FlexiBowl®.
    :::{important}
    Se al momento del comando non risulta selezionato/abilitato alcun modello, il sistema restituisce un messaggio di errore e il Locator non viene avviato.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Detiene el proceso de localización
  - Ninguno
* - `turn_Locator`
  - Si no se ha recogido ninguna pieza, hace girar el FlexiBowl® y reinicia la búsqueda
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Inicia la localización sin activar el FlexiBowl® (solo adquisición de imagen)
  - `Pattern_n;x;y;r`/ Ninguno
* - `state_Locator`
  - Devuelve el estado de diagnóstico del localizador
  - `El localizador está en ejecución` / `El localizador está en error` / `El localizador no está en ejecución`
```
:::{note}
Otros separadores de cadena disponibles, además de `;`, son: `,`, `|`, `:`, `&`, `$`, `@`, `#`. 
:::

### *Comandos FlexiBowl®*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de retorno
* - `start_Empty`
  - Inicia la secuencia de vaciado rápido del FlexiBowl®
  - `start_Empty finalizado`
```


### *Señales hopper opcional*

```{note}
Si debe activarse la tolva, recibiremos la cadena: `"Hopper;signalnumber;time"`

```



Para obtener información detallada sobre la instalación física y las conexiones eléctricas, consulte las secciones siguientes:
- [Cálculo de la distancia óptima de la cámara](05_Calcolo_distanza_ottimale.md)
- [Instalación mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Cableado y conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

