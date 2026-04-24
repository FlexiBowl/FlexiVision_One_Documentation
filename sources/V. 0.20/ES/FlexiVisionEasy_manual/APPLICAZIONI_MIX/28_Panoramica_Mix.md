# **Vista General Aplicación Mix**
Esta sección introduce el concepto de **Aplicación Mix** en FlexiVision One, explicando en qué se diferencia de una aplicación estándar y cómo configurarla correctamente a nivel de receta y modelos.

---

## ¿Qué es una Aplicación Mix?

Una **Aplicación Mix** es una configuración aplicativa en la que, dentro de la misma receta, coexisten modelos relativos a **componentes completamente diferentes entre sí**.

En una aplicación Mix, el robot puede reconocer y recoger **varias tipologías de piezas diferentes** presentes simultáneamente en el área de trabajo, sin tener que cambiar de receta ni interrumpir el ciclo. La visión identifica cada pieza presente en el FlexiBowl® y devuelve al robot las coordenadas de la pieza recogible más adecuada, independientemente de su tipología.
```{tip}
**Ejemplo típico:** en el FlexiBowl® pueden encontrarse simultáneamente tornillos, tuercas y arandelas. El robot recoge cualquier pieza reconocida, optimizando el throughput sin interrupciones.
```

---

## Aplicación Estándar vs Aplicación Mix

| Característica | Aplicación Estándar | Aplicación Mix |
|---|---|---|
| **Tipologías de piezas** | Un solo tipo de pieza  | Varias tipologías de piezas completamente diferentes entre sí |
| **Modelos en la receta** | Todos los modelos se refieren al mismo componente | Los modelos también pueden referirse a componentes distintos |
| **Comportamiento del robot** | Recoge siempre la misma pieza incluso en posiciones diferentes (creando varios modelos)| Recoge cualquier pieza reconocida, independientemente de la tipología |
| **Configuración software** | Ninguna diferencia respecto al modo Mix | Ninguna diferencia respecto al modo Estándar |
| **Selección del modo** | No requerida: depende de los modelos introducidos en la receta | No requerida: depende de los modelos introducidos en la receta |
| **Comandos robot** | Familia `start_..` | Familia `mix_..` |

```{note}
A nivel software no existe una elección explícita entre modo Estándar y Mix: la distinción está determinada exclusivamente por el **contenido de la receta**. Si todos los modelos presentes se refieren a la misma pieza (o a sus distintas caras), se trata de una aplicación Estándar. Si los modelos se refieren a piezas diferentes, se trata automáticamente de una aplicación Mix.
```

---

## ¿Cómo se crea una receta Mix?

El proceso de creación de una receta Mix es **idéntico** al de una receta Estándar. No es necesario seleccionar ninguna opción preliminar. Por tanto, se puede seguir el procedimiento de [Creación Recetas y Modelos - Vista General](../QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md)

La diferencia se manifiesta **en la fase de creación de los modelos**:

- En una aplicación **Estándar**, todos los modelos introducidos en la receta representan el mismo componente (por ejemplo: cara A, cara B, cara C de la misma pieza).
- En una aplicación **Mix**, los modelos introducidos representan **componentes completamente diferentes** (por ejemplo: Pieza A, Pieza B, Pieza C — tres componentes distintos con geometrías diferentes).
```{important}
Cada modelo dentro de una receta Mix debe entrenarse por separado con su propia pieza física de referencia, siguiendo el procedimiento estándar descrito en [Crear un Nuevo Modelo](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md). Las clearances y las coordenadas robot pick deben calibrarse individualmente para cada componente.
```

---

## Próximos pasos

Una vez comprendido el concepto de Aplicación Mix y configurada la receta con los modelos de los distintos componentes, el paso siguiente se refiere a la adaptación de los **comandos robot** necesarios para operar en modo Mix:

**→ [Comandos Aplicación Mix](29_Comandi_Mix.md)**

