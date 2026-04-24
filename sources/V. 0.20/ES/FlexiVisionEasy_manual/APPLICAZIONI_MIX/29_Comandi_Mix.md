# **Comandos Aplicación Mix**
```{note}
**Requisitos previos**

Antes de continuar con esta sección, asegurarse de haber comprendido el funcionamiento de la Aplicación Mix y de haber configurado correctamente la receta con los modelos de los distintos componentes. Consultar [Vista General Aplicación Mix](28_Panoramica_Mix.md).
```

---

## Diferencias lado robot

En una Aplicación Mix, los comandos TCP/IP enviados por el robot al sistema de visión cambian respecto a los de una aplicación Estándar.

La principal diferencia se refiere a la **familia de comandos de localización**: los comandos que en la aplicación Estándar tienen prefijo `start_` se sustituyen por la familia equivalente con prefijo `mix_`.

Esta variación permite al sistema de visión activar la lógica de reconocimiento **multicomponente**, devolviendo al robot no solo las coordenadas de la pieza localizada, sino también el **identificador del modelo** reconocido, de modo que el programa robot pueda seleccionar la estrategia de recogida correcta para cada tipología de pieza.
```{important}
El valor de retorno de los comandos Mix incluye siempre el identificador del pattern reconocido (`Pattern_n`). El programa robot debe estar preparado para gestionar las distintas tipologías de respuesta y adoptar la lógica de recogida apropiada según el modelo identificado.
```

---

## Comandos disponibles en modo Mix

### Gestión de recetas

| Comando | Acción | Valor de Retorno |
|---|---|---|
| `set_Recipe=nome_ricetta` | Carga la receta Mix especificada | Ninguno |
| `get_Recipe` | Devuelve el nombre de la receta actualmente cargada | `nome_ricetta` |
```{note}
Los comandos de gestión receta son idénticos entre modo Estándar y Mix.
```

### Comandos de localización Mix

Los comandos de localización Mix permiten al robot solicitar las coordenadas de un modelo específico dentro de la receta. Cada comando está dedicado a un único modelo y gestiona de forma autónoma el ciclo de búsqueda, incluida la movimentación del FlexiBowl® y la activación del hopper si es necesario.

El comportamiento de `mix_Locator_n` es el siguiente:

1. El sistema adquiere una imagen y busca el Modelo `n`.
2. Si el modelo no se encuentra en la primera adquisición, el FlexiBowl® se acciona automáticamente y la búsqueda se reanuda.
3. El ciclo continúa hasta que el Modelo `n` se localiza o se envía el comando `stop_Locator`.
4. Durante toda la fase de búsqueda, el hopper se activa automáticamente si es necesario.
```{important}
Cada comando `mix_Locator_n` busca **exclusivamente** el modelo correspondiente al número `n`.   
Esto significa que, para solicitar las coordenadas de un modelo diferente, es necesario utilizar el comando específico para ese modelo (p. ej. `mix_Locator_2` para el Modelo 2, `mix_Locator_3` para el Modelo 3, y así sucesivamente).
```

| Comando | Acción | Valor de Retorno |
|---|---|---|
| `mix_Locator_1` | Inicia la búsqueda del **Modelo 1**. Si no se encuentra, acciona el FlexiBowl® y repite la búsqueda automáticamente hasta el hallazgo o hasta `stop_Locator`. Activa el hopper si es necesario. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Como arriba, para el **Modelo 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Como arriba, para el **Modelo 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Como arriba, para el **Modelo 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Si no se ha recogido ninguna pieza, hace girar el FlexiBowl® y reinicia la búsqueda multicomponente | `Pattern_n;x;y;r` |
| `test_Locator` | Inicia la localización multicomponente sin activar el FlexiBowl® (solo adquisición de imagen) | `Pattern_n;x;y;r` / Ninguno |
| `stop_Locator` | Interrumpe cualquier búsqueda en curso | Ninguno |
| `state_Locator` | Devuelve el estado diagnóstico del localizador | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
El número máximo de modelos gestionables dentro de una única receta Mix es **8**, correspondientes a los comandos `mix_Locator_1` … `mix_Locator_8`. El programa robot puede solicitar los modelos en cualquier orden y combinación, según la lógica aplicativa.
```

### Comandos FlexiBowl®

| Comando | Acción | Valor de Retorno |
|---|---|---|
| `start_Empty` | Inicia la secuencia de vaciado rápido del FlexiBowl® | `start_Empty ended` |

### Señales hopper opcionales
```{note}
Si el hopper debe activarse, recibiremos la cadena: `"Hopper;signalnumber;time"`
```

---

## Formato del valor de retorno

En modo Mix, el valor de retorno de los comandos de localización tiene el siguiente formato:
```
Pattern_n;x;y;r
```

| Campo | Descripción |
|---|---|
| `Pattern_n` | Identificador del modelo reconocido (p. ej. `Pattern_1`, `Pattern_2`, …). Corresponde al número del modelo solicitado con el comando `mix_Locator_n`. |
| `x` | Coordenada X de la pieza en el área de trabajo (en mm, en el sistema de referencia del robot) |
| `y` | Coordenada Y de la pieza en el área de trabajo (en mm, en el sistema de referencia del robot) |
| `r` | Ángulo de rotación de la pieza (en grados) |
```{tip}
El campo `Pattern_n` es el parámetro clave para las aplicaciones Mix: el programa robot debe utilizarlo para seleccionar la rutina de recogida correcta (posición de aproximación, apertura pinza, fuerza de agarre, etc.) según la tipología de pieza identificada.
```

---


Para información sobre el protocolo de comunicación y los parámetros de conexión TCP/IP, consultar:

**→ [Protocolo de Comunicación Robot-Visión](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
