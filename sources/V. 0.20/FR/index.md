# **Manuel FlexiVision One**

## **Bienvenue dans le manuel FlexiVision One!**  
test Nous sommes ravis de vous accueillir dans votre nouveau guide FlexiVision One!
Ce manuel a été créé spécialement pour être votre référence claire et fiable. Nous espérons qu'en le consultant, vous pourrez profiter pleinement de tous les avantages de notre système.
Votre avis est essentiel pour nous: n'hésitez pas à nous transmettre vos commentaires en [nous contactant](https://www.flexibowl.it/contatti)! 

*- L'Équipe Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Qu'est-ce que FlexiVision One?**  
FlexiVision One est notre solution de vision basée sur VisionController, conçue pour guider le robot et disponible comme composant additionnel pour les systèmes FlexiBowl®.
Tout en conservant toutes les puissantes fonctionnalités de la version précédente, permettant donc le déchargement, la séparation, la reconnaissance et la prise des pièces en vrac sur la surface de l'alimentateur, FlexiVision One révolutionne l'expérience utilisateur.
Grâce à un guide complet étape par étape et à des outils intuitifs, nous avons considérablement simplifié le processus, rendant la programmation et l'utilisation accessibles et utilisables par tous, quel que soit le niveau d'expérience.

## **Vue d'ensemble du système** 
Schéma d'exemple du système avec connexions jusqu'à trois FlexiBowl, trois caméras et trois hoppers.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Schéma d'exemple du système FlexiVision One
```
## **Comment lire le manuel**  
Ce manuel a été conçu pour prendre en charge à la fois la phase de conception et d'intégration du système, ainsi que la phase d'installation et de mise en service sur site. 
Pour cette raison, il est divisé en macro-sections avec des destinataires et des finalités distincts.
  
## **Quelle section recherchez-vous?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Si vous devez...
  - L'information se trouve dans...

* - Vérifier dimensions, poids, exigences électriques et protocoles de communication
  - [**RÉFÉRENCE TECHNIQUE ET SPÉCIFICATIONS**](specifiche_tecniche)

* - Installer les composants, câbler le système, configurer le réseau ou calibrer caméra/robot
  - [**INSTALLATION DU SYSTÈME**](Installazione_Meccanica) et [**QUICKSTART**](quickstart)

* - Programmer un nouveau modèle de pièce ou configurer le système d'alimentation
  - [**QUICKSTART**](quickstart)

* - Résoudre des problèmes ou demander une assistance
  - [**DÉPANNAGE**](troubleshooting) et [**SUPPORT**](support)
```
## **Groupes d'intervention et responsabilités**

La mise en œuvre correcte de FlexiVision One exige la collaboration de différentes fonctions professionnelles. Ce tableau clarifie les rôles et responsabilités:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Fonction professionnelle
  - Responsabilités principales
  - Sections de référence du manuel

* - **Intégrateur système**
  - Conception du layout, dimensionnement des composants, vérification des exigences techniques
  - Référence technique et spécifications, Options

* - **Technicien installateur**
  - Montage mécanique, câblage électrique, configuration réseau
  - Installation du système, Câblage et connexions

* - **Programmeur robot**
  - Calibration caméra-robot, intégration plugin, programmation des logiques de prise
  - Quickstart, Protocol Setup, Calibration

* - **Opérateur de ligne**
  - Création de nouveaux modèles de pièce, configuration des paramètres FlexiBowl, surveillance des performances
  - Vérification des résultats Run Time

* - **Technicien de maintenance**
  - Diagnostic des problèmes, remplacement de composants, mises à jour logicielles
  - Nouveau modèle, Configuration FlexiBowl, Dépannage, Support
```

## **Conventions et symboles utilisés**

Dans tout le manuel, des bannières informatives sont utilisées pour mettre en évidence les contenus importants:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Type
  - Signification

* - ```{warning}
    Avertissement
    ```
  - Indique une situation potentiellement dangereuse ou une procédure critique qui, si elle n'est pas exécutée correctement, pourrait provoquer des dommages à l'équipement ou de graves dysfonctionnements du système.

* - ```{important}
    Important
    ```
  - Met en évidence des informations fondamentales qui ne doivent pas être ignorées afin de garantir le bon fonctionnement du système ou la sécurité de l'opération.

* - ```{note}
    Note informative
    ```
  - Fournit des informations essentielles pour le bon déroulement de la procédure, des clarifications techniques ou des renvois à des chapitres associés.

* - ```{tip}
    Suggestion
    ```
  - Suggère une pratique optimale, une alternative ou un conseil pouvant simplifier l'installation ou améliorer les performances du système.

* - ```{error}
    Erreur
    ```
  - Indique une erreur critique ou une condition de panne nécessitant une intervention immédiate. Signale des situations qui compromettent le fonctionnement du système et exigent une action corrective.
```







```{toctree}
:hidden:
:caption: AVANT DE COMMENCER 

FlexiVisionEasy_manual/01_informazioni_preliminari.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/02_informazioni_sicurezza.md
```  
```{toctree}
:hidden:
FlexiVisionEasy_manual/03_Unboxing_Contenuto.md
```    
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27_Support.md

```
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27b_Glossario.md

```

```{toctree}
:hidden:
:caption: RÉFÉRENCE TECHNIQUE ET SPÉCIFICATIONS 

FlexiVisionEasy_manual/rif_tecnico_specifiche/04_Specifiche_FlexiVision.md
```    

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md
```   

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/06_PlugIn.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/07_Backup_management.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/08_Opzioni.md
```   
```{toctree}
:hidden:
:caption: INSTALLATION DU SYSTÈME

FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md
```     
  
```{toctree}
:hidden:
:caption: QUICKSTART

FlexiVisionEasy_manual/QUICKSTART/12_Panoramica_Interfaccia.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/SETUP/13_setup.md
``` 


```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/24_Verifica_Risultati.md
```

```{toctree}
:hidden:
:caption: APPLICATIONS MIX

FlexiVisionEasy_manual/APPLICAZIONI_MIX/28_Panoramica_Mix.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/APPLICAZIONI_MIX/29_Comandi_Mix.md
```  

```{toctree}
:hidden:
:caption: CONFIGURATIONS MULTI-DISPOSITIF

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: GARANTIE 

FlexiVisionEasy_manual/25_Garanzia.md
```

```{toctree}  
:hidden:
:caption: DÉPANNAGE

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```






