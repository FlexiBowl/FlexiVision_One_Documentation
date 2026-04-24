(cablaggio)=
# **Cableado y Conexiones**
imagen general de conexiones eléctricas 
tipo:  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **De**
  - **A**
  - **Conexión**

* - Red eléctrica
  - FlexiBowl
  - Alimentación 110/220 Vdc

* - Red eléctrica
  - Robot
  - Alimentación según las especificaciones del robot en posesión

* - Red eléctrica
  - Cámara
  - Alimentación 24 Vdc

* - Red eléctrica
  - Iluminador (luz)
  - Alimentación 24 Vdc

* - Red eléctrica
  - Controlador Hopper
  - Alimentación 110/220 Vdc

* - Controlador Hopper
  - Hopper
  - Alimentación y señal

* - Robot
  - Controlador Hopper
  - I/O Digitales

* - VisionController
  - Cámara
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```

## Procedimiento guiado de cableado

```{list-table} 
:header-rows: 1

* - **Paso**
  - **Acción**
* - 1
  - Conectar la alimentación del FlexiBowl®.  
    [🔗 Consultar el manual para las especificaciones de alimentación](http://link-al-manuale.com)
* - 2
  - Conectar el [cable de alimentación Hirose 24V](cavo) a la Cámara.
* - 3
  - Conectar el FlexiBowl® al VisionController con cable Ethernet.
* - 4
  - Conectar la Cámara al VisionController (PC) con cable Ethernet.
* - 5
  - Conectar el Robot al VisionController con cable Ethernet.
* - 6
  - Conectar el aire comprimido al FlexiBowl®.  
    [🔗 Consultar el manual para las especificaciones neumáticas](http://link-al-manuale.com)
* - 7
  - Si está presente, conectar el hopper a su controlador
* - 8
  - Si está presente, conectar el robot al controlador del hopper (I/O Digitales)
* - 9 
  - Si está presente, alimentar el controlador del hopper (110/220 V según la opción elegida al comprar la base vibrante del hopper)
* - 10
  - Encender el interruptor AC del FlexiBowl® (posición "I"). El led READY está **ON**.
* - 11
  - Encender todos los demás dispositivos
```
(cablaggio_illuminatore)=
## Cableado iluminador

![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parámetro
  - Requisito / Acción
* - **Tensión**
  - 24V DC (±10%). Tensión mínima de funcionamiento: 20V DC en la entrada luz.
* - **Conector**
  - M12 Male. 
    :::{note}
      Para conectar el toplight, también es posible adquirir su [cable de alimentación](cavoalimtoplight). 
    :::
* - **Pinout conector**
  - Pin 1: +24V (marrón) — Pin 3: GND (azul) — Pin 4: STROBE PNP (negro)
* - **Modo STROBE (PNP)**
  - De 5V a 24V para encendido al 100%. De 0V a 1V para apagado al 100%.
* - **Modo CONTINUO**
  - Pin 1 (+24V) y Pin 3 (GND) conectados; Pin 4 (PNP) conectado a Pin 1.
* - **Caída de tensión (cable M12, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Apantallamiento**
  - Utilizar cables apantallados para reducir las interferencias electromagnéticas (EMI).
```
```{warning}
**Seguridad eléctrica**

- Respetar las tensiones de alimentación y los bornes de conexión indicados.
- No modificar ni desmontar el producto.
- No conectar ni limpiar el equipo cuando está bajo tensión.
- No mirar directamente la fuente luminosa.
```



