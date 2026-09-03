# **Información de seguridad**

Las siguientes instrucciones de seguridad, precauciones generales y normas relativas a la manipulación y el entorno operativo deben respetarse escrupulosamente para garantizar la seguridad del personal, la integridad del producto y el correcto funcionamiento del sistema.

```{warning}
**Responsabilidad del usuario**

El cumplimiento de todas las normas de seguridad de esta sección es obligatorio y responsabilidad del usuario final. De lo contrario, pueden producirse daños personales y materiales o afectar al funcionamiento del sistema.
```

---

## Seguridad operativa

### *Integración con sistemas robotizados*


```{warning} **Requisitos de seguridad de las células**  

FlexiVision One funciona en estrecha conexión con sistemas robóticos de terceros. El usuario debe asegurarse de que la zona de trabajo está equipada con todas las medidas de seguridad necesarias impuestas por la normativa pertinente.
```


```{warning} **Precaución durante el funcionamiento**    

Al utilizar el sistema, tenga siempre en cuenta:

- Dimensiones físicas del robot y del FlexiBowl®
- Trayectorias y velocidad de los movimientos del robot
- Posibles situaciones imprevistas (caída de piezas, errores de recogida)
- Zonas de peligro durante las fases de manipulación del FlexiBowl®
```

### *Precauciones generales antes de las intervenciones*


```{warning} **Desconexión de la alimentación**  

Antes de realizar cualquier trabajo de mantenimiento, modificación o inspección en el sistema, asegúrese siempre de que:

- Todas las fuentes de energía están desconectadas (VisionController, FlexiBowl®, Cámara, Iluminador)
- La energía neumática está descargada y desconectada (si está presente)
- Los cables de conexión están físicamente desconectados
- El robot está en modo de seguridad o completamente apagado
```


```{warning} **Procedimientos de seguridad**    

No confíe únicamente en los interruptores: utilice procedimientos de bloqueo/etiquetado (LOTO) cuando estén disponibles.
```

### *Modificaciones y manipulaciones*


```{warning} **Prohibición de modificaciones no autorizadas**    

No modifique nunca el producto o sus componentes sin la autorización expresa y por escrito de ARS S.r.l.
```

```{warning} **Consecuencias de los cambios**    

Las modificaciones no autorizadas pueden:

- Provocar fallos de funcionamiento del sistema
- Invalidar la garantía
- Crear riesgos de lesiones, descargas eléctricas o incendios
- Comprometer las certificaciones de seguridad del producto
```

---

## Predisposiciones a cargo del cliente

Sin perjuicio de cualquier acuerdo contractual en contrario, las siguientes disposiciones son **normalmente responsabilidad del Cliente**:

````{list-table}
:header-rows: 1
:widths: 25 75

* - Categoría
  - Descripción
* - **Locales**
  - Obras de albañilería, cimientos, canalizaciones e iluminación eventualmente requeridas.
* - **Instalaciones eléctricas**
  - Hasta los puntos de alimentación de la máquina, de conformidad con las normas vigentes en el país de instalación. Las especificaciones técnicas se incluyen en el contrato de venta. El fabricante no asume ninguna responsabilidad si el cliente no las garantiza.
* - **Alimentación eléctrica**
  - Incluido el conductor de puesta a tierra, de acuerdo con las características y tolerancias especificadas en este manual.
* - **Servicios auxiliares**
  - Adecuados a las necesidades de la máquina.
* - **Utensilios y materiales de consumo**
  - Necesarios para el montaje y la instalación.
* - **Lubricantes**
  - Necesarios para la puesta en marcha de la máquina.
* - **Alimentación neumática**
  - Adecuada según se especifica en la sección "Datos técnicos".
* - **Manipulación**
  - Medios de elevación y manipulación adecuados.
````

---

## Condiciones ambientales admisibles

El sistema está diseñado para uso **exclusivo en interiores**, protegido de la intemperie y los agentes agresivos. El entorno no debe estar clasificado ATEX.

````{list-table}
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Límite admitido
* - **Temperatura ambiente**
  - 5 ÷ 40 °C
* - **Humedad relativa**
  - 5 – 90% (sin condensación), variación máx. 0,005 p.u./h
* - **Iluminación ambiente**
  - Luz de neón
* - **Polvo**
  - Ausencia de polvo excesivo, abrasivo o combustible
* - **Vapores y gases**
  - Ausencia de humos corrosivos, vapores oleosos, mezclas explosivas
* - **Vibraciones y golpes**
  - Ausencia de vibraciones, golpes o sacudidas anormales
* - **Variaciones térmicas**
  - Máximo 5K/h
* - **Otras exclusiones**
  - Aire salobre, intemperie, radiación nuclear, condiciones inusuales de almacenamiento
````

````{warning}
Las condiciones ambientales distintas de las especificadas pueden causar graves daños en la máquina y anular la garantía.
````

````{important}
La superficie de trabajo debe estar suficientemente iluminada. En presencia de zonas de sombra o desniveles, corresponde al usuario disponer dispositivos de iluminación adecuados.
````

La máquina está diseñada y fabricada para funcionar con seguridad en las siguientes condiciones ambientales:

| Condiciones ambientales admisibles | |
|---|---|
| **Temperatura ambiente** | 5 ÷ 40 °C |
| **Rango de humedad** | 5 - 90 % (sin condensación) |
| **Iluminación ambiental** | Luz de neón |

```{warning}
Las condiciones ambientales distintas de las especificadas pueden causar graves daños en la máquina. La instalación de la máquina en entornos que no correspondan a lo indicado anula la garantía de los componentes a sustituir.
```

```{important}
La superficie de trabajo debe estar suficientemente iluminada. Si en el puesto de trabajo se detectan zonas de sombra o desniveles, corresponderá al usuario disponer dispositivos de iluminación adecuados.
```

---

## Condiciones ambientales y protección

### *Protección contra líquidos*


```{warning} **Riesgo de contacto con líquidos**    

No utilice el producto en entornos en los que el VisionController, la cámara u otros componentes electrónicos puedan entrar en contacto:

- Gotas o salpicaduras de agua
- Aceites, lubricantes u otros líquidos industriales
- Condensación o humedad excesiva
- Polvos conductores
```

```{note} **Soluciones para entornos críticos**    

Si el sistema va a funcionar en entornos con presencia de líquidos, proporcione una protección adecuada (envolventes IP65 o superior) y consulte al Servicio Técnico de ARS para obtener soluciones personalizadas.
```

### *Temperaturas de funcionamiento*


```{warning} **Superficies calientes - Temperaturas máximas**    

En condiciones de uso intensivo o ambientes calurosos, algunos componentes del sistema pueden alcanzar altas temperaturas:

- VisionController: hasta 50°C en superficies exteriores
- Iluminador LED: hasta 40°C en superficie frontal
- Cámara industrial: hasta 50°C en carcasa metálica
```


```{warning} **Responsabilidad del cliente**    

Es responsabilidad del cliente:

- Documente los riesgos térmicos en su evaluación de riesgos
- Forme al personal en los procedimientos para evitar el contacto accidental
- Coloque señales de advertencia cuando sea necesario
- Garantice una ventilación adecuada de los componentes
```

### *Condiciones ambientales para la instalación y el almacenamiento*

```{note} **Requisitos medioambientales - Tabla de referencia**    

Para garantizar la durabilidad y fiabilidad, el VisionController y la cámara deben utilizarse y almacenarse en las siguientes condiciones:

| Parámetro | Condiciones de funcionamiento | Condiciones de almacenamiento |
|-----------|---------------------|--------------------------|
| **Temperatura** | +5°C ÷ +40°C | +5°C ÷ +40°C |
| **Humedad relativa** | <90% (sin condensación) | <90% (sin condensación) |
```

```{note} **Precauciones adicionales para el medio ambiente**    

Para preservar la integridad de los componentes:

- Evite la exposición directa a la luz solar
- Protéjala de vibraciones excesivas durante el almacenamiento
- Consérvela en un entorno seco y sin polvo
- La cámara es sensible a los golpes mecánicos: manipúlela con cuidado
```

---

## Transporte y manipulación

### *Recepción e inspección*

```{note} **Inspección a la llegada**    

Al recibir el producto, antes de firmar el albarán de entrega:

1. **Inspección externa de los envases**: Compruebe la integridad de la caja y del embalaje exterior. Compruebe si hay signos de impacto, aplastamiento o humedecimiento.
2. **Verificación del contenido**: Compare el contenido con el albarán de entrega. Compruebe que están presentes todos los componentes solicitados.
```

```{note} **En caso de daños o discrepancias**    

Si surgen problemas:

- NO firme el recibo como "conforme"
- Anote los daños en el documento de transporte
- Fotografíe cualquier daño evidente
- Póngase en contacto con el servicio ARS inmediatamente:
  [service@arsautomation.com](mailto:service@arsautomation.com)
  [us.service@arsautomation.com](mailto:us.service@arsautomation.com) si contacta desde América
```

### *Manipulación y almacenamiento*

Para evitar daños durante el transporte y el almacenamiento:

```{tip}
**Durante el transporte:**
- Mover siempre el embalaje en posición vertical (respetar las flechas "ARRIBA" en el embalaje)
- No dejar caer ni golpear el paquete
- Utilizar carros o transpaletas adecuados al peso
- Evitar cambios bruscos de temperatura
```

```{tip}
**Durante el almacenamiento:**
- Conservar en lugar seco y cubierto
- No apilar otras cargas sobre el embalaje
- No subir ni apoyarse en el embalaje
- Respetar las condiciones ambientales indicadas en la tabla anterior
```

```{tip}
**Durante el desembalaje:**
- Abrir con cuidado para no dañar los componentes internos
- Conservar el embalaje original para posibles devoluciones o transportes futuros
- Comprobar la presencia de todos los accesorios y la documentación
```

---

## Eliminación y fin de vida útil

```{warning}
Cuando el producto llegue al final de su ciclo de vida, debe eliminarse de conformidad con la normativa vigente relativa a los residuos de aparatos eléctricos y electrónicos (RAEE/WEEE).
```

