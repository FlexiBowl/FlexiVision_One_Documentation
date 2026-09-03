(camerasetup)=
# **Camera Setup**

Cette section décrit la procédure de configuration et de test de la caméra industrielle du système FlexiVision One. La configuration correcte de la caméra est cruciale pour garantir l'acquisition d'images de qualité.

```{note}
**Pré-requis**

Avant de poursuivre, s’assurer que :
- La caméra a été installée mécaniquement à la bonne distance
- Le câble Ethernet de la caméra est connecté au VisionController
- La caméra est alimentée (via PoE ou alimentation externe)
- FlexiBowl® est configuré et le rétroéclairage fonctionne (pour le test d’acquisition)
```

---

## Accès à la configuration de la caméra

```{list-table}

* - **1** 
  - Depuis la page principale du logiciel, cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Sur la page SETUP, identifier et cliquer sur l'icône **Camera Setup**
    ```{dropdown} Page Setup 
       ![Page Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - La page de configuration de la caméra s'ouvre
```

---

## Aperçu de l'interface Camera Setup

La page Camera Setup présente trois boîtes d'information principales et un espace de configuration :
![Page Camera Setup](../../../../../_shared/media/images/pagina_camsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Selected Camera**
  - Affiche l'identification de la caméra actuellement sélectionnée. Elle s'affiche automatiquement au démarrage de FlexiVision One.
* - **Camera Serial Number**
  - Affiche le numéro de série unique de la caméra connectée
* - **Status**
  - Indique l'état de la connexion
* - **Calibration Result**
  - Affiche le résultat de l'étalonnage de la caméra
* - **Config Camera**
  - Bouton permettant d'ouvrir la page de configuration détaillée
```

---


:::{note}
Pour plus de commodité et d'homogénéité, nous recommandons d'associer le numéro de la caméra au FlexiBowl® correspondant&nbsp;:
 - ✅ Caméra installée au-dessus du FlexiBowl® 1&nbsp;: CAM-CIC-5000-20G-12345 > Sélectionner la Caméra 1 FlexiBowl® 1
:::

:::{warning}
Si la caméra n'est pas visible lors de la première ouverture de FlexiVision, consulter la section [Troubleshooting pour la section Camera Setup](scelta_camera)
:::


---
## Étapes suivantes

Une fois la configuration de la caméra terminée, passer à :

- [Étalonnage de la Caméra](calibrazione)
- [FlexiBowl® Setup](fbsetup)
- [Hopper Setup](13b_Hopper_Setup.md)
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Sauvegarder la recette](ricettabase)

