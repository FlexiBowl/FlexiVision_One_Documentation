(protocollo)=
# **Protocolo de Comunicación Robot-Visión**

FlexiVision One se comunica con el robot mediante protocolo **TCP/IP** en red Ethernet. 

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
  - CHR(13) - Carriage Return
* - Formato de datos
  - Cadena ASCII
* - Timeout
  - Configurable (predeterminado: 5000 ms)
* - Encoding
  - UTF-8
```

## Comandos disponibles

El sistema admite los siguientes comandos mediante cadenas de texto enviadas por la conexión TCP/IP:

### Gestión de recetas

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de Retorno
* - `set_Recipe=nome_ricetta`
  - Carga la receta correspondiente al "nome_ricetta" especificado
  - Ninguno
* - `get_Recipe`
  - Devuelve el nombre de la receta actualmente cargada
  - `nome_ricetta`
```

### Comandos de localización

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de Retorno
* - `start_Locator`
  - Inicia el proceso de localización de las piezas. Si no hay piezas recogibles, llama automáticamente a la rutina de movimiento del FlexiBowl.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Detiene el proceso de localización
  - Ninguno
* - `turn_Locator`
  - Si no se ha recogido ninguna pieza, hace girar el FlexiBowl y reinicia la búsqueda
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Inicia la localización sin activar el FlexiBowl (solo adquisición de imagen)
  - `Pattern_n;x;y;r`/ Ninguno
* - `state_Locator`
  - Devuelve el estado diagnóstico del localizador
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

### Comandos FlexiBowl

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Acción
  - Valor de Retorno
* - `start_Empty`
  - Inicia la secuencia de vaciado rápido (Quick-Emptying) del FlexiBowl
  - `start_Empty ended`
```


### Señales hopper opcionales

```{note}
Si el hopper debe activarse, recibiremos la cadena: `"Hopper;signalnumber;time"`

```



Para información detallada sobre la instalación física y las conexiones eléctricas, continuar con las secciones siguientes:
- [Cálculo de Distancia Óptima Cámara](05_Calcolo_distanza_ottimale.md)
- [Instalación Mecánica](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Cableado y Conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

