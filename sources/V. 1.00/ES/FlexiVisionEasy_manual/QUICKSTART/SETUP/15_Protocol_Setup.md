(protocol_setup)=
# **Protocol Setup**

La página **Protocol Setup** permite configurar los parámetros que rigen el flujo de comunicación y el intercambio de datos entre el sistema de visión FlexiVision One y el robot. Estos parámetros determinan cuántos objetos se envían, cómo se ordenan y cómo gestiona el sistema las estadísticas y los estados operativos.

---

## Acceso a Protocol Setup

1. Desde el menú principal, acceda a la sección dedicada al protocolo de comunicación
2. Seleccione **Protocol Setup**
3. Se abre la interfaz con los parámetros configurables


---

## Parámetros configurables

![Página Protocol Setup](../../../../../_shared/media/images/pagina_protocolsetup.png)

```{list-table}
:header-rows: 1
:widths: 35 65

* - **Parámetro**
  - **Descripción y función**
* - [**Max Object Count Return**](maxobject)
  - Indica el número **máximo** de objetos (es decir, su tríada de coordenadas) que el sistema de visión puede devolver al robot en una sola ejecución. Si la visión detecta más objetos que este límite, se envía un máximo de este número, seleccionados según el criterio de ordenación configurado (Sorting Mode).
* - [**Min Object Count Return**](minobject)
  - Indica el número **mínimo** de objetos que deben devolverse en una ejecución para que el resultado se considere válido. Si el número está por debajo de este umbral, la ejecución se considera inválida.
* - [**Sorting Mode Results**](sortingmode)
  - Define el **criterio de ordenación** con el que se ordena la lista de objetos devueltos por la visión. Este parámetro determina la prioridad de recogida y determina qué objetos se incluyen en Max Object Count Return.
    
    *Opción típica:* por puntuación decreciente.
* - [**Pickable parts by the robot detected by vision in each cycle**](pickableparts)
  - Indica el número de recogidas que realiza el robot por ciclo de visión. Por ejemplo, una recogida doble corresponde al valor 2. No representa el número de objetos detectados por la visión, sino el número de agarres del robot por ciclo. Parámetro utilizado para el cálculo de las estadísticas.

* - **Maximum processing time per part with the robot (in seconds)**
  - Define el tiempo máximo tras el cual el sistema considera finalizada la gestión/envío de coordenadas de una ejecución y suele pasar del estado RUN al estado IDLE. Parámetro utilizado para **estadísticas y gestión del flujo de trabajo**.

    :::{attention}
    **No es un timeout de error del robot**, sino una referencia temporal para el cálculo del ciclo y las métricas de productividad.
    :::
```

---

## Configuración detallada de parámetros

(maxobject)=
### *Max Object Count Return*

```{list-table}
 :class: align-top

* - **Función**: 
  - Limita el número máximo de coordenadas que se envían al robot por cada ciclo de visión.

* - **Valores típicos:**
  - 
    - **1** : Configuración más común para robots con recogida simple
    - **2** : Configuración para robots con recogida doble
    - **3** : Configuración para robots con recogida triple
    - **4-8 objetos**: Para sistemas con seguimiento circular
    - **>8 objetos**: Rara vez es necesario, puede saturar la comunicación

    :::{tip}
    **Cómo elegir el valor:**
    1. Considerar la velocidad del robot (tiempo pick&place por pieza)
    2. Considerar el tiempo de ciclo de visión + FlexiBowl®
    3. Fórmula aproximada: `Max Count = (Tiempo ciclo visión+FB) / (Tiempo pick robot)`

    **Ejemplo práctico:**
    - Ciclo visión+FlexiBowl®: 3 segundos
    - Tiempo de recogida del robot: 2 segundos/pieza
    - Recuento máximo óptimo: 3/2 = 1,5 → Redondear a 2 objetos
    :::
```

(minobject)=
### *Min Object Count Return*

```{list-table}
* - **Función**: 
  - Limita el número mínimo de coordenadas que se envían al robot por cada ciclo de visión.

* - **Valores típicos:**
  - 
    - **1**: Configuración más común - incluso una sola pieza reconocida es aceptable
    - **>2**: Sólo para aplicaciones especiales con multi-pick obligatorio

* - **Comportamiento del sistema:**
  - 
    - **Objetos detectados ≥ Min Count**: coordenada(s) enviada(s) al robot
    - **Objetos detectados < Min Count**: coordenadas no enviadas y ejecución de la secuencia del FlexiBowl®


* - **Impacto en la productividad**
  - 
    **Min Count = 1** (más permisivo):
    - ✓ Máxima flexibilidad, el robot trabaja aunque solo haya una pieza
    - ✗ Posibles ciclos con baja eficiencia (1 pieza cada N segundos)

    **Min Count = 3** (más restrictivo):
    - ✓ Garantiza una eficiencia mínima por ciclo
    - ✗ Puede provocar esperas si el llenado es variable
```

(sortingmode)=
### *Sorting Mode Results*


```{list-table}
:header-rows: 1
:widths: 30 70

* - Modalidad de ordenación
  - Descripción y cuándo usar
* - **Por puntuación (descendente)**
  - Ordenar por puntuación de mayor a menor. Los objetos que coinciden mejor con el modelo se envían primero.   
    **Más común y recomendable**: Garantiza siempre la recogida de piezas con un reconocimiento más fiable.
* - **Por puntuación (ascendente)**
  - Ordenar por puntuación de menor a mayor. Los objetos con peor coincidencia con el modelo se envían primero.     
    **NO RECOMENDADO**: NO garantiza siempre la recogida de piezas con un reconocimiento más fiable.
* - **By X Coordinate (Ascending)**
  - Ordenar por coordenada X creciente. Útil si el robot tiene preferencia de recogida secuencial a lo largo de un eje.
* - **By X Coordinate (Descending)**
  - Ordenar por coordenada X decreciente.
* - **By Y Coordinate (Ascending)**
  - Ordenar por coordenada Y creciente.
* - **By Y Coordinate (Descending)**
  - Ordenar por coordenada Y decreciente.
* - **X Alternating**
  - El sistema alterna la selección del componente entre el primero y el último detectado en el eje X. Como los dos componentes seleccionados están distantes entre sí, se reduce el riesgo de que una recogida anterior haya desplazado piezas cercanas, lo que garantiza una recogida más segura y fiable.
* - **Y Alternating**
  - El sistema alterna la selección del componente entre el primero y el último detectado en el eje Y. Mismo principio que X Alternating: la distancia entre los dos puntos de recogida minimiza las interferencias causadas por el movimiento accidental de piezas adyacentes.
```

```{tip}
**Elección del Sorting Mode óptimo**

**Recomendado en la mayoría de los casos: Por puntuación (descendente)**

**Ventajas**:
- Máxima fiabilidad: el robot siempre recoge las piezas mejor reconocidas
- Reduce el riesgo de recogidas erróneas
- Independiente de la posición física
```

```{note}
La modalidad de ordenación interactúa con Max Object Count. Se envían los primeros 15 objetos (según el criterio).
```
(pickableparts)=
### *Pickable parts by the robot*

**Función**

Parámetro estadístico que indica cuántas piezas **recoge realmente** el robot por cada ciclo de visión.

**Valores típicos**

- **1**: robot con pinza simple, recoge 1 pieza cada vez
- **2**: robot con pinza doble o ventosa doble
- **>2**: robot con pinza o ventosa multi-pick

```{important}
Este valor representa las **recogidas físicas**, no los objetos detectados por la visión.
```

**Ejemplo clarificador**

Escenario: pinza doble, la visión detecta 5 objetos.

- Si quiero enviar al robot un máximo de 2 objetos, configuro `Max Object Count = 2`.
- Si quiero que el robot recoja al menos 2 objetos a la vez, configuro `Min Object Count = 2`.
- En este caso configuro `Pickable Parts by the robot = 2`.
- Si, por el contrario, también quiero permitir la recogida de un solo objeto, configuro `Max Object Count = 2`, `Min Object Count = 1` y `Pickable Parts by the robot = 2`.

**Impacto en las estadísticas del Dashboard**

Este parámetro es crucial para el cálculo preciso de los **Parts Per Minute (PPM)**.

- Fórmula: `PPM = (Pickable parts x 60) / Tiempo ciclo total en segundos`
- Si se ajusta incorrectamente, el PPM visualizado no se corresponde con la realidad



---

## Guardar configuración

```{warning}
**Guardado obligatorio**

Después de configurar los parámetros de Protocol Setup:

1. Comprobar que todos los valores están ajustados correctamente  
2. Hacer clic en Recipes > Save Recipe
3. Los parámetros se guardan en la configuración del sistema
```

---

## Próximos pasos

Una vez completada la configuración del protocolo, el sistema está totalmente configurado para funcionar:

- [Guardar la receta](ricettabase)





