# **Cableado y conexiones**
(troubleshooting_alimentazione)=
## Problemas de alimentación FlexiBowl®

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **El LED READY no se enciende**
  - • La fuente de alimentación no está conectada correctamente
    
    • Interruptor CA en posición "O" en lugar de "I"
    
    • Cable de alimentación dañado
    
    • Fusibles fundidos dentro del panel frontal 
  - • Compruebe la conexión eléctrica según el manual del FlexiBowl®
    
    • Ponga el interruptor en posición "I" (ON)
    
    • Inspeccione el cable en busca de daños y sustitúyalo si es necesario
    
    • Póngase en contacto con el servicio técnico para sustituir el fusible
* - **El FlexiBowl® se apaga aleatoriamente**
  - • Conexión eléctrica defectuosa
    
    • Interferencias eléctricas
    
  - • Apriete las conexiones eléctricas
    
    • Conecte a una línea dedicada con filtro EMI

```
(troubleshooting_ethernet)=
## Problemas de conexión Ethernet

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **FlexiBowl® no comunica con VisionController**
  - • FlexiBowl® no encendido (LED READY apagado)  
    • Cable Ethernet no conectado correctamente al FlexiBowl® y/o al VisionController  
    • Cable Ethernet dañado    
    • Dirección IP errónea  
    • FlexiBowl® y VisionController en subredes distintas  
    • Firewall bloquea la comunicación  
    • Puerto Ethernet del VisionController averiado  
  - • Compruebe que el LED READY está encendido en el FlexiBowl®  
    • Compruebe la conexión física del cable Ethernet en ambos lados  
    • Pruebe el cable con un comprobador de cables o sustitúyalo  
    • Compruebe la configuración IP en [FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md)  
    • Configure FlexiBowl® y VisionController en la misma red (p. ej.: 192.168.1.x)  
    • Deshabilite temporalmente el firewall para pruebas  
    • Pruebe otro puerto Ethernet del VisionController  
* - **Conexión intermitente**  
  - • Cable demasiado largo (> 100 m)  
    • Conector RJ45 dañado o mal crimpado  
    • Interferencias electromagnéticas  
  - • Reduzca la longitud del cable por debajo de 100 m o utilice un switch intermedio  
    • Sustituya los conectores o el cable completo  
    • Utilice cable apantallado (STP) lejos de fuentes de EMI  
```
(troubleshooting_pneumatica)=
## Problemas neumáticos (aire comprimido)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **El flip no funciona o el impulso es muy débil**
  - • Aire comprimido no conectado  
    • Manguera neumática dañada u obstruida  
    • Regulador de presión cerrado o al mínimo  
    
    • Presión insuficiente (< 5 bar)
    
    
    
    • Fugas en el circuito neumático
    
    
  - • Conecte el aire comprimido a la conexión FlexiBowl® (consulte el manual)  

    • Compruebe que la manguera no esté doblada ni obstruida; sustitúyala si es necesario  
    • Abra el regulador de presión del panel de control  
    
    • Aumente la presión a 5-6 bar
    
    
    
    • Inspeccione los racores con agua jabonosa; apriételos o sustitúyalos
    
    
* - **Air-blow no funciona**
  - • FlexiBowl® no configurado con la opción Air-Blow  

    • Desviadores de aire sin alimentación externa   

    • Reguladores de caudal cerrados   

    • Presión de aire insuficiente  
  
    
    • Electroválvula defectuosa
  - • Compruebe que el FlexiBowl® solicitado tiene la opción Option Blow Test en True en la hoja de producción   

    • Compruebe que hay alimentación neumática externa (manguera suministrada)     

    • Si hay varios desviadores de aire, compruebe que el regulador de caudal situado en el lateral del FlexiBowl® está ajustado por encima de cero     

    • Compruebe la presión del aire (5-6 bar)    

    
    • Siga [Instrucciones]()
```
(troubleshooting_connessione_camera)=
## Problemas de conexión de la cámara

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **La cámara no es detectada por el VisionController**
  - • Cable Ethernet de la cámara no conectado
    
    • Cámara conectada a un puerto no POE del VisionController
    

    
    • Dirección IP de la cámara en conflicto con la de otros dispositivos en la misma subred  
    • Puerto POE del VisionController averiado
  - • Compruebe la conexión física del cable de la cámara  
    • Conecte la cámara SOLO al puerto POE del VisionController  
    • Restablezca la IP de la cámara o configure una IP estática única    
    • Pruebe otro puerto POE del VisionController  
* - **Imagen de la cámara negra o ausente**
  - • Iluminador apagado   
    • Exposición de la cámara demasiado baja  
    • Objetivo con tapa protectora no retirada    
    • Objetivo no instalado    
    • Cámara no alimentada (POE no activo)  
    
     
    • Cámara defectuosa  
  - • Compruebe que el iluminador está encendido   
    • Aumente la exposición en [Configuración de la cámara](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
    • Retire la tapa protectora del objetivo   
    • Instale el objetivo con la distancia focal correcta  
    • Compruebe que el LED de la cámara está encendido (indicador POE activo)  
    • Sustituya la cámara  

* - **La cámara se desconecta aleatoriamente**
  - • Alimentación POE insuficiente (potencia < demanda de la cámara)
    
    • Cable dañado
    
    • Sobrecalentamiento de la cámara
    
    • Puerto POE dañado
  - • Compruebe la alimentación POE disponible   
    • Sustituya el cable Ethernet  
    
    • Mejore la ventilación del área de la cámara  
    
    • Sustituya el switch POE o el puerto del VisionController  
```
(troubleshooting_connessione_toplight)=
## Problemas de conexión del Toplight 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **El Toplight no se enciende**
  - • Alimentación 24 V CC no conectada
    
    • Cable de alimentación dañado
    
    • Tensión incorrecta (≠ 24 V)
    
    • Toplight defectuoso
    
    • Fusible/protección disparado
  - • Compruebe la conexión de alimentación 24 V CC
    
    • Inspeccione el cable; sustitúyalo si está dañado
    
    • Mida la tensión con multímetro; debe ser 24 V CC (±10 %)
    
    • Sustituya el Toplight
    
    • Compruebe las protecciones del armario eléctrico
* - **Luminosidad del Toplight variable**
  - • Alimentación inestable
    
    • Conexiones sueltas
    
    • Fuente de alimentación subdimensionada
    
    • Toplight al final de su vida útil
  - • Compruebe la estabilidad de la tensión de alimentación
    
    • Apriete todas las conexiones eléctricas
    
    • Compruebe el consumo de corriente frente a la capacidad de la fuente de alimentación
    
    • Sustituya el Toplight
* - **El Toplight se sobrecalienta**
  - • Ventilación insuficiente
    
    • Corriente excesiva
    
    • Ciclo de trabajo continuo al 100 %
  - • Mejore la circulación del aire alrededor del Toplight
    
    • Compruebe que el consumo de corriente no supere las especificaciones
    
    • Implemente un ciclo de trabajo intermitente si es posible
```
(troubleshooting_multi)=
## Problemas de configuraciones multidispositivo
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Posibles causas
  - Soluciones
* - **Sistema con 2-3 FlexiBowl®: solo uno comunica**
  - • FlexiBowl® apagados  
    • Direcciones IP duplicadas  
    • Cables cruzados  
  - • Compruebe que el FlexiBowl® está encendido  
    • Asigne IPs únicas a cada FlexiBowl® (p. ej.: 192.168.1.10, .11, .12)  
    • Compruebe el cableado en estrella correcto (sin daisy-chain)  
* - **Sistema con 2-3 cámaras: solo una adquiere**  
  - • Alimentación insuficiente   
    • Direcciones IP de las cámaras en conflicto  
  - • Compruebe que la alimentación está comprendida entre 6 y 26 V  
    • Configure una IP estática única para cada cámara  
    • Habilite todas las cámaras en [Configuración de la cámara](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
* - **Sistema con 2-3 tolvas: control incorrecto**  
  - • Tolvas no habilitadas individualmente en el software  
    • Alimentación incorrecta   
    • Contacto con el robot incorrecto   
  - • Habilite cada tolva en [Hopper Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md)  
    • Compruebe la alimentación  
    • Compruebe el contacto con el robot   
```



