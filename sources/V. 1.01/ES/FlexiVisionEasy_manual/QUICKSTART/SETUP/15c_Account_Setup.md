# **Account Setup**

La página **Account Setup** permite crear y eliminar las cuentas de usuario de FlexiVision One. A cada cuenta se le asigna un **nivel de acceso**, que determina qué funciones del software puede utilizar.

```{note}
La gestión de cuentas está reservada a los usuarios de nivel **5** (**Engineer**).
```

---

(accesso-alla-configurazione-account)=
## Acceso a la configuración de cuentas

:::{list-table}
:widths: 10 90

* - **1**
  - Abra la página **Setup**.
* - **2**
  - En el menú desplegable **Name**, seleccione **Engineer**.
* - **3**
  - En el campo **Password**, introduzca `3`.
* - **4**
  - Pulse **Login** y confirme el mensaje de inicio de sesión correcto con **OK**.
* - **5**
  - Pulse el icono **Account Setup**.
:::

```{note}
El acceso solo es efectivo después de pulsar **Login**. El usuario activo y su nivel se indican en **Current User Name**.
```

---

## Visión general de la interfaz Account Setup

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Sección
  - Descripción
* - **Lista de cuentas** (izquierda)
  - Muestra las cuentas existentes. Con **Delete Account** se elimina la seleccionada.
* - **Nueva cuenta** (derecha)
  - Campos **Account Name**, **Account Password**, **Account Level** y botón **Create Account**.
:::

---

## Creación de una nueva cuenta

### *Paso 1: Introducción de los datos*

:::{list-table}
:widths: 10 90

* - **6**
  - En el campo **Account Name**, introduzca el nombre de la nueva cuenta.
* - **7**
  - En el campo **Account Password**, introduzca la contraseña de la nueva cuenta.
* - **8**
  - En el campo **Account Level**, introduzca el nivel de acceso, de `1` a `5` (véase [Niveles de acceso](#livelli-di-accesso)).
* - **9**
  - Pulse **Create Account**. La nueva cuenta aparece en la lista de la izquierda.
:::

### *Paso 2: Acceso con la nueva cuenta*

:::{list-table}
:widths: 10 90

* - **10**
  - Vuelva a la página **Setup** y seleccione la nueva cuenta en el menú desplegable **Name**.
* - **11**
  - Introduzca la contraseña y pulse **Login**.
:::

El vídeo muestra la creación de una cuenta de nivel 3, el acceso con la nueva cuenta y los mensajes que aparecen cuando el nivel no es suficiente.

:::{video} ../../../../../_shared/media/videos/new_account.mp4
     :width: 100%
     :align: center
:::

---

## Eliminación de una cuenta

Realice los pasos 1 a 5 de [Acceso a la configuración de cuentas](#accesso-alla-configurazione-account) y, a continuación, proceda como se indica.

:::{list-table}
:widths: 10 90

* - **6**
  - En la lista de la izquierda, seleccione la cuenta que desea eliminar.
* - **7**
  - Pulse **Delete Account**. La cuenta se elimina de la lista y del menú desplegable de la página **Setup**.
:::

```{warning}
La eliminación es inmediata y no se pide ninguna confirmación. Compruebe la cuenta seleccionada antes de pulsar **Delete Account**.
```

:::{video} ../../../../../_shared/media/videos/delete_account.mp4
     :width: 100%
     :align: center
:::

---

(livelli-di-accesso)=
## Niveles de acceso

FlexiVision One dispone de tres perfiles predefinidos. Una cuenta creada por el usuario recibe los permisos correspondientes al nivel asignado.

:::{list-table}
:header-rows: 1
:widths: 20 20 60

* - Nivel
  - Perfil
  - Uso
* - 1 – 3
  - **Operator**
  - Funciones básicas: consulta de la página Home, carga de recetas y copia de seguridad.
* - 4
  - **Technician**
  - Funciones de Operator, además de pruebas, gestión de recetas, configuración del sistema y licencia de software.
* - 5
  - **Engineer**
  - Funciones de Technician, además de **Protocol Setup** y **Account Setup**.
:::

### *Funciones habilitadas por perfil*

:::{list-table}
:header-rows: 1
:widths: 16 33 17 17 17

* - Página
  - Función
  - Operator (1 – 3)
  - Technician (4)
  - Engineer (5)
* - Home
  - Contact Us
  - Sí
  - Sí
  - Sí
* - Home
  - Documentation
  - Sí
  - Sí
  - Sí
* - Home
  - Quick Start
  - Sí
  - Sí
  - Sí
* - Dashboard
  - Test
  - —
  - Sí
  - Sí
* - Recipes
  - Load Recipe
  - Sí
  - Sí
  - Sí
* - Recipes
  - Backup
  - Sí
  - Sí
  - Sí
* - Recipes
  - Import Backup
  - —
  - Sí
  - Sí
* - Recipes
  - New Recipe
  - —
  - Sí
  - Sí
* - Recipes
  - Save Recipe
  - —
  - Sí
  - Sí
* - Recipes
  - Edit Recipe
  - —
  - Sí
  - Sí
* - Recipes
  - Delete Recipe
  - —
  - Sí
  - Sí
* - Setup
  - Camera Setup
  - —
  - Sí
  - Sí
* - Setup
  - FlexiBowl® Setup
  - —
  - Sí
  - Sí
* - Setup
  - Hopper Setup
  - —
  - Sí
  - Sí
* - Setup
  - Robot Setup
  - —
  - Sí
  - Sí
* - Setup
  - License Software
  - —
  - Sí
  - Sí
* - Setup
  - Protocol Setup
  - —
  - —
  - Sí
* - Setup
  - Account Setup
  - —
  - —
  - Sí
* - General
  - Cierre de la aplicación
  - —
  - Sí
  - Sí
:::

Si se intenta usar una función no habilitada, aparece el mensaje **Insufficient Access Level**, que indica el nivel requerido y el del usuario activo.

### *Cierre de sesión automático*

- **Technician**: cierre de sesión automático después de 5 minutos.
- **Engineer**: sin cierre de sesión automático.

```{tip}
Asigne a cada usuario el nivel más bajo suficiente para sus tareas, para evitar modificaciones accidentales de recetas y configuraciones.
```
