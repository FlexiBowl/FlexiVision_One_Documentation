# V. 0.23

## **Mejoras**

### Integración con el robot

- Eliminado el servidor TCP dedicado al láser: todos los comandos y comunicaciones del láser se encaminan ahora a través del cliente TCP del Robot.

## **Problemas resueltos**

### Wizard Test Air Blow y Test Flip

- Corregido el Wizard para las pruebas **Flip** y **Blow**: añadido el control del estado del motor con habilitación automática, verificación posterior y gestión del error en caso de que no se pueda habilitar.
