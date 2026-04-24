(backup)=
# **BackUp Management**

## **Vista general**

El backup de FlexiVision One consiste en copiar la carpeta `Recipes` presente en el VisionController. Esta carpeta contiene todas las recetas configuradas en el sistema — incluidos modelos, parámetros de reconocimiento y ajustes asociados — y representa el único dato de usuario que debe conservarse.

Como no se requiere ninguna herramienta dedicada, el proceso de backup se reduce a una simple operación de copiar y pegar mediante el Explorador de archivos.
```{important}
Se recomienda realizar un backup cada vez que se cree o modifique una receta, y en cualquier caso antes de cualquier actualización de software o intervención de mantenimiento en el VisionController.
```

---

## **Contenido del Backup**

Dentro de la carpeta de instalación de FlexiVision One se encuentra la siguiente estructura:
```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← unica cartella da includere nel backup
├── Flexivision_Smart_018
└── Package.dat
```

La única carpeta que contiene datos de usuario es `Recipes\`. Las demás carpetas y archivos presentes pertenecen a la instalación del software y no deben incluirse en el backup.
```{note}
La ruta exacta de la carpeta de instalación puede variar según la configuración del sistema. En caso de duda, verificar la ruta en los ajustes del software.
```

---

## **Procedimiento de Backup**
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Paso**
  - **Acción**
* - 1
  - Asegurarse de que el software FlexiVision One esté **cerrado**.
* - 2
  - Abrir el Explorador de archivos en el VisionController y navegar hasta `C:\FlexiVision One\`.
* - 3
  - Hacer clic con el botón derecho en la carpeta `Recipes` y seleccionar **Copiar**.
* - 4
  - Navegar hasta el destino de backup deseado (memoria USB, carpeta de red, NAS, etc.).
* - 5
  - Pegar la carpeta en el destino. Se recomienda renombrarla incluyendo la fecha, por ejemplo: `Recipes_backup_2025-06-01`.
```
```{warning}
No realizar el backup mientras el software FlexiVision One está en ejecución. La copia de archivos abiertos podría resultar incompleta o corrupta.
```

---

## **Procedimiento de Restauración (Restore)**

En caso de pérdida de datos o sustitución del VisionController, es posible restaurar las recetas anteriores siguiendo estos pasos:
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Paso**
  - **Acción**
* - 1
  - Asegurarse de que FlexiVision One esté instalado en el VisionController y **cerrado**.
* - 2
  - Abrir el Explorador de archivos y navegar hasta `C:\FlexiVision One\`.
* - 3
  - Renombrar la carpeta `Recipes` existente (p. ej. `Recipes_old`) como medida de precaución.
* - 4
  - Copiar la carpeta de backup en la ubicación `C:\FlexiVision One\` y renombrarla `Recipes`.
* - 5
  - Iniciar FlexiVision One: todas las recetas guardadas anteriormente volverán a estar disponibles.
```
```{important}
La versión del software instalada en el VisionController debe ser compatible con la utilizada en el momento del backup. En caso de actualización de software, contactar con el soporte técnico antes de proceder con la restauración.
```

---

## **Recomendaciones**

- Conservar al menos **dos copias del backup** en ubicaciones físicas distintas (p. ej. una memoria USB local y una carpeta de red remota).
- Etiquetar siempre los backups con **fecha y versión de software** para facilitar su identificación con el tiempo.
- No modificar manualmente el contenido de la carpeta `Recipes`: las recetas deben gestionarse exclusivamente mediante la interfaz de FlexiVision One.
```{tip}
Para entornos con varios VisionController, se recomienda centralizar los backups en una carpeta de red compartida, organizada por nombre de máquina y fecha.
```
