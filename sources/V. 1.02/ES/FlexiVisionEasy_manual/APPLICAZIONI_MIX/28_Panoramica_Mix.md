# **Visión general Aplicación Mix**
Esta sección introduce el concepto de **Aplicación Mix** en FlexiVision One, explicando en qué se diferencia de una aplicación estándar y cómo configurarla correctamente a nivel de receta y modelos.

---

## ¿Qué es una aplicación Mix?

Una **aplicación Mix** es una configuración aplicativa en la que coexisten modelos relativos a **componentes completamente diferentes entre sí dentro de la misma receta**.

En una aplicación Mix, el robot es capaz de reconocer y recoger **varios tipos diferentes de piezas** presentes simultáneamente en el área de trabajo, sin tener que cambiar de receta ni interrumpir el ciclo. La visión identifica cada pieza presente en el FlexiBowl® y devuelve al robot las coordenadas de la pieza recogible más adecuada, independientemente de su tipología.

![Aplicación Mix](../../../../_shared/media/videos/video_applicazionemix.gif)  
*Ejemplo de Aplicación Mix*

```{tip}
**Ejemplo típico:** en el FlexiBowl® pueden encontrarse simultáneamente tornillos, tuercas y arandelas. El robot recoge cualquier pieza reconocida, optimizando el rendimiento sin interrupciones.
```

---

## Aplicación estándar frente a aplicación Mix

| Característica | Aplicación estándar | Aplicación Mix |
|---|---|---|
| **Tipos de piezas** | Solo un tipo de pieza  | Varios tipos de piezas completamente diferentes entre sí |
| **Modelos en la receta** | Todos los modelos se refieren al mismo componente | Los modelos también pueden referirse a componentes distintos |
| **Comportamiento del robot** | Recoge siempre la misma pieza incluso en posiciones diferentes (creando múltiples modelos)| Recoge cualquier pieza reconocida, independientemente de la tipología |
| **Configuración del software** | No hay diferencia respecto al modo Mix | No hay diferencia respecto al modo estándar |
| **Selección del modo** | No es necesaria: depende de los modelos incluidos en la receta | No es necesaria: depende de los modelos incluidos en la receta |
| **Comandos robot** | Familia `start_..` | Familia `mix_..` |

```{note}
A nivel de software no existe una elección explícita entre el modo estándar y el modo Mix: la distinción viene determinada exclusivamente por el **contenido de la receta**. Si todos los modelos presentes se refieren a la misma pieza (o a sus distintas caras), se trata de una aplicación estándar. Si los modelos se refieren a piezas diferentes, se trata automáticamente de una aplicación Mix.
```

---

## ¿Cómo se crea una receta Mix?

El proceso de creación de una receta Mix es **idéntico** al de una receta estándar. No es necesario seleccionar ninguna opción previa. A continuación, puede seguir el procedimiento de [Creación de recetas y modelos - Visión general](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

La diferencia se manifiesta **en la fase de creación de los modelos**:

- En una aplicación **estándar**, todos los modelos incluidos en la receta representan el mismo componente (por ejemplo: cara A, cara B, cara C de la misma pieza).
- En una aplicación **Mix**, los modelos incluidos representan **componentes completamente diferentes** (por ejemplo: Pieza A, Pieza B, Pieza C — tres componentes distintos con geometrías diferentes).
```{important}
Cada modelo dentro de una receta Mix debe entrenarse por separado con su propia pieza física de referencia, siguiendo el procedimiento estándar descrito en [Creación de un nuevo modelo](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Las clearances y las coordenadas robot pick deben calibrarse individualmente para cada componente.
```

---

## Próximos pasos

Una vez comprendido el concepto de Aplicación Mix y configurada la receta con los modelos de los distintos componentes, el siguiente paso consiste en adaptar los **comandos robot** necesarios para operar en modo Mix:

**→ [Comandos Aplicación Mix](29_Comandi_Mix.md)**

