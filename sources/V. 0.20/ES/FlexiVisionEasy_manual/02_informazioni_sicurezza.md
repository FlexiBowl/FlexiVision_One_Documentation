# **Información de Seguridad**

Las siguientes instrucciones de seguridad, precauciones generales y normas relativas a la manipulación y al entorno operativo deben respetarse escrupulosamente para garantizar la seguridad del personal, la integridad del producto y el correcto funcionamiento de la instalación.

```{warning}
**Responsabilidad del usuario**

El cumplimiento de todas las normas de seguridad indicadas en esta sección es obligatorio y responsabilidad del usuario final. El incumplimiento puede causar daños a personas, equipos o comprometer el funcionamiento del sistema.
```

---

## Seguridad operativa

### Integración con sistemas robotizados

#### **Requisitos de seguridad de la celda**

```{warning}
FlexiVision One opera en estrecha conexión con sistemas robotizados de terceros. El usuario debe garantizar que el área de trabajo esté equipada con todas las medidas de seguridad necesarias exigidas por la normativa pertinente
```
#### **Atención durante la operación**

```{warning}

Durante el funcionamiento del sistema, tener siempre en cuenta:

- Dimensiones físicas del robot y del FlexiBowl
- Trayectorias y velocidades de los movimientos robóticos
- Posibles situaciones imprevistas (caída de piezas, errores de recogida)
- Zonas de peligro durante las fases de vibración del FlexiBowl
```

### Precauciones generales antes de las intervenciones

#### **Desconexión de alimentaciones**

```{warning}
Antes de realizar cualquier intervención de mantenimiento, modificación o inspección en el sistema, asegurarse siempre de que:

- Todas las fuentes de alimentación eléctrica estén desconectadas (VisionController, FlexiBowl, Cámara, Iluminador)
- La alimentación neumática esté descargada y desconectada (si está presente)
- Los cables de conexión estén físicamente desconectados
- El robot esté en modo de seguridad o completamente apagado
```
#### **Procedimientos de seguridad**

```{warning}

No confiar exclusivamente en los interruptores: utilizar procedimientos de lockout/tagout (LOTO) cuando estén disponibles.
```

### Modificaciones y manipulaciones

#### **Prohibición de modificaciones no autorizadas**

```{warning}
No modificar nunca el producto ni sus componentes sin autorización escrita expresa de ARS S.r.l.
```
#### **Consecuencias de las modificaciones**

```{warning}
Las modificaciones no autorizadas pueden:

- Causar fallos de funcionamiento del sistema
- Invalidar la garantía
- Crear riesgos de lesiones, descargas eléctricas o incendios
- Comprometer las certificaciones de seguridad del producto
```

---

## Condiciones ambientales y protección

### Protección contra líquidos

#### **Riesgo de contacto con líquidos**

```{warning}

No utilizar el producto en entornos donde el VisionController, la cámara u otros componentes electrónicos puedan entrar en contacto con:

- Gotas de agua o salpicaduras
- Aceites, lubricantes u otros líquidos industriales
- Condensación o humedad excesiva
- Polvos conductivos
```
#### **Soluciones para entornos críticos**

```{note}

Si el sistema debe operar en entornos con presencia de líquidos, prever protecciones adecuadas (envolventes IP65 o superiores) y consultar al servicio técnico ARS para soluciones personalizadas.
```

### Temperaturas operativas

#### **Superficies calientes - Temperaturas máximas**

```{warning}
En condiciones de uso intenso o en entornos cálidos, algunos componentes del sistema pueden alcanzar temperaturas elevadas:

- VisionController: hasta 50°C en las superficies externas
- Iluminador LED: hasta 40°C en la superficie frontal
- Cámara industrial: hasta 50°C en el cuerpo metálico
```
#### **Responsabilidad del cliente**

```{warning}
Es responsabilidad del cliente:

- Documentar los riesgos térmicos en su propia evaluación de riesgos
- Instruir al personal sobre los procedimientos para evitar contactos accidentales
- Prever señalización de advertencia donde sea necesario
- Garantizar una ventilación adecuada de los componentes
```

### Condiciones ambientales para instalación y almacenamiento

#### **Requisitos ambientales - Tabla de referencia**

```{note}

Para garantizar duración y fiabilidad, el VisionController y la cámara deben utilizarse y conservarse en las siguientes condiciones:

| Parámetro | Condiciones operativas | Condiciones de almacenamiento |
|-----------|---------------------|--------------------------|
| **Temperatura** | +1°C ÷ +50°C | -20°C ÷ +65°C |
| **Humedad relativa** | <90% (sin condensación) | <90% (sin condensación) |


```
#### **Precauciones ambientales adicionales**

```{note}
Para preservar la integridad de los componentes:

- Evitar la exposición directa a la luz solar
- Proteger contra vibraciones excesivas durante el almacenamiento
- Mantener en un entorno seco y libre de polvos agresivos
- La cámara es sensible a los choques mecánicos: manipular con cuidado
```

---

## Transporte y manipulación

### Recepción e inspección

#### **Inspección a la llegada**

```{note}
Al recibir el producto, antes de firmar el albarán de entrega:

1. **Inspección externa del embalaje**: Verificar la integridad de la caja y del embalaje exterior. Comprobar la presencia de posibles señales de golpes, aplastamientos o humedad.

2. **Verificación del contenido**: Comparar el contenido con la nota de entrega. Verificar la presencia de todos los componentes pedidos.
```

#### **En caso de daños o discrepancias**

```{note}
Si se detectan problemas:

- NO firmar el recibo como "conforme"
- Anotar los daños en el documento de transporte
- Fotografiar cualquier daño evidente
- Contactar inmediatamente con el servicio de asistencia ARS: 
    [service@arsautomation.com](mailto:service@arsautomation.com) 
    [us.service@arsautomation.com](mailto:us.service@arsautomation.com) si se contacta desde América
```

### Manipulación y almacenamiento
Para prevenir daños durante el transporte y el almacenamiento:

#### **Transporte**

```{tip}
**Durante el transporte:**
- Manipular siempre el embalaje en posición vertical (respetar las flechas "ARRIBA" del embalaje)
- No dejar caer ni golpear el paquete
- Utilizar carros o transpaletas adecuados al peso
- Evitar cambios bruscos de temperatura
```
#### **Almacenamiento**

```{tip}
**Durante el almacenamiento:**
- Conservar en un lugar seco y cubierto
- No superponer otras cargas sobre el embalaje
- No subirse ni apoyarse sobre el embalaje
- Respetar las condiciones ambientales indicadas en la tabla anterior
```
#### **Desembalaje**

```{tip}
**Durante el desembalaje:**
- Abrir con cuidado para no dañar los componentes internos
- Conservar el embalaje original para posibles devoluciones o transportes futuros
- Verificar la presencia de todos los accesorios y de la documentación
```

---

## Eliminación y fin de vida

### **Eliminación responsable**

```{warning}

Cuando el producto alcance el final de su ciclo de vida, debe eliminarse de conformidad con las normativas vigentes relativas a los residuos de aparatos eléctricos y electrónicos (RAEE/WEEE).
```
### **Componentes sujetos a eliminación especial**

```{note}
**Componentes sujetos a eliminación especial:**
- Tarjetas electrónicas (VisionController): RAEE categoría 6
- Cámara industrial: RAEE categoría 6
- Iluminadores LED: RAEE categoría 5
- Cables y conectores: eliminación con materiales eléctricos
```
---


