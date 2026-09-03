# **Manuale FlexiVision One**

## **Bienvenue dans le manuel du FlexiVision One !**  
Nous sommes heureux de vous accueillir dans votre nouveau guide FlexiVision One !
Ce manuel a été spécialement conçu pour être une référence claire et fiable. Nous espérons qu'en le consultant, vous bénéficierez de tous les avantages de notre système.
Votre avis est essentiel pour nous : n'hésitez pas à nous faire part de vos commentaires [contattandoci](https://www.flexibowl.it/contatti) ! 

*- L'équipe d'ARS Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Qu'est-ce que FlexiVision One ?**  
FlexiVision One est notre solution de vision basée sur VisionController, conçue pour le guidage des robots et disponible en tant qu'extension pour les systèmes FlexiBowl®.
Tout en conservant toutes les puissantes fonctionnalités de la version précédente, permettant ainsi le déchargement, la séparation, la reconnaissance et le prélèvement de pièces en vrac sur la surface d'alimentation, FlexiVision One révolutionne l'expérience de l'utilisateur.
Grâce à des conseils détaillés étape par étape et à des outils intuitifs, nous avons grandement simplifié le processus, rendant la programmation et le fonctionnement accessibles et utilisables par tous, quel que soit leur niveau d'expérience.

## **Aperçu du système** 

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Exemple de schéma du système FlexiVision One
```
## **Comment lire le manuel**  
Ce manuel est conçu pour aider à la fois la phase de conception et d'intégration du système et la phase d'installation et de mise en service sur le terrain. 
Pour cette raison, il est divisé en macro-sections ayant des destinataires et des objectifs distincts.
  
## **Quelle section recherchez-vous ?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Si vous devez...
  - L'information se trouve dans...

* - Vérifier les dimensions, le poids, les exigences électriques et les protocoles de communication
  - [**RÉFÉRENCE TECHNIQUE ET SPÉCIFICATIONS**](specifiche_tecniche)

* - Installer les composants, câbler le système, configurer le réseau ou calibrer la caméra/le robot
  - [**INSTALLATION DU SYSTÈME**](Installazione_Meccanica) et [**QUICKSTART**](setupcomponenti)

* - Programmer un nouveau modèle de pièce ou configurer le système d'alimentation
  - [**QUICKSTART**](setupcomponenti)

* - Résoudre des problèmes ou demander de l'assistance
  - [**DÉPANNAGE**](troubleshooting) et [**SUPPORT**](support)
```
## **Groupes d'intervention et responsabilités**

La mise en œuvre réussie de FlexiVision One nécessite la collaboration de plusieurs professionnels. Ce tableau clarifie les rôles et les responsabilités :

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Profil professionnel
  - Principales responsabilités
  - Sections du manuel de référence

* - **Intégrateur de système**
  - Conception de l'agencement, dimensionnement des composants, vérification des exigences techniques
  - Référence technique et spécifications, options

* - **Technicien d'installation**
  - Assemblage mécanique, câblage électrique, configuration du réseau
  - Installation du système, câblage et connexions

* - **Programmateur de robot**
  - Calibrage caméra-robot, intégration de plugins, programmation de la logique de prise
  - Démarrage rapide, configuration du protocole, calibrage

* - **Opérateur de ligne**
  - Création de nouveaux modèles de pièce, configuration des paramètres FlexiBowl®, contrôle des performances
  - Vérification des résultats du temps d'exécution

* - **Technicien de maintenance**
  - Dépannage, remplacement de composants, mise à jour du logiciel
  - Nouveau modèle, configuration FlexiBowl®, dépannage, assistance
```

## **Conventions et symboles utilisés**

Tout au long du manuel, des bannières d'information sont utilisées pour mettre en évidence le contenu important :

```{list-table}
:header-rows: 1

* - Type
  - Signification

* - ```{warning}
    Mise en garde
    ```
  - Indique une situation potentiellement dangereuse ou une procédure critique qui, si elle n'est pas exécutée correctement, peut entraîner des dommages à l'équipement ou un dysfonctionnement grave du système.

* - ```{important}
    Important
    ```
  - Met en évidence les informations vitales à ne pas ignorer pour assurer le bon fonctionnement du système ou la sécurité de l'opération.

* - ```{note}
    Note d'information
    ```
  - Fournit des informations essentielles au bon déroulement de la procédure, des clarifications techniques ou des références à des chapitres connexes.

* - ```{tip}
    Conseil
    ```
  - Suggère une meilleure pratique, une alternative ou un conseil qui peut simplifier l'installation ou améliorer les performances du système.

* - ```{error}
    Erreur
    ```
  - Indique une erreur critique ou une condition de défaut nécessitant une action immédiate. Signale les situations qui compromettent le fonctionnement du système et nécessitent une action corrective.
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
:caption: INSTALLAZIONE DEL SISTEMA

FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md
```     
  
```{toctree}
:hidden:
:caption: PANORAMICA DELL'INTERFACCIA

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12a_Home.md
```  
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12c_Dashboard.md
```    
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12b_Recipes.md
```    
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12d_Setup.md
```    

```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12e_TastiInfo.md
```    

```{toctree}
:hidden:
:caption: QUICKSTART
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
:caption: EXPERT

FlexiVisionEasy_manual/EXPERT/32_Expert.md
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
:caption: CONFIGURATIONS MULTI-APPAREILS

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

```{toctree}  
:hidden:
:caption: APPENDICI

FlexiVisionEasy_manual/APPENDICI/Release_Notes.md
```





