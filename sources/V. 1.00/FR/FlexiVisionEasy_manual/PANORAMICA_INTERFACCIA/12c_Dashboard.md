# **Page DashBoard**
L'interface du FlexiVision One est structurée en sections fonctionnelles qui guident l'utilisateur depuis la configuration initiale jusqu'à la gestion opérationnelle du système.
Chaque page fournit des informations en temps réel sur l'état de la machine, les connexions, les performances et les paramètres du processus, avec un accès direct aux fonctions clés.
La navigation est conçue pour garantir la simplicité d'utilisation, le contrôle immédiat des opérations et la surveillance continue des performances de vision, d'alimentation et de robot.


<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Description de la page Dashboard
:header-rows: 1
:widths: 10 90

* - **#**
  - **Description**

* - 1
  - **Zone de vision et de détection**
    * **Detected vision parts avec graphique** : nombre de composants détectés dans l'image actuelle et tendance dans le temps (30s).
    

* - 2
  - **État de fonctionnement**
    * **In run** : voyant indiquant si le système est en cours de fonctionnement ou arrêté.
    * **In run time** : chronomètre indiquant la durée totale de fonctionnement du système.

* - 3
  - **Contrôles et sélection**
    * **Menu déroulant FlexiBowl®** : permet de sélectionner le dispositif FlexiBowl® sur lequel vous souhaitez opérer.
    * **Test Locator** : déclenche des mouvements cycliques du FlexiBowl® et de la trémie tant qu'il y a des composants dans la zone de visualisation.

* - 4
  - **État des connexions**
    * **FlexiBowl®** : indique l'état de la connexion en temps réel avec le FlexiBowl®.
    * **Robot** : indique l'état de la connexion en temps réel avec le robot.

* - 5
  - **Analyse des temps de cycle (Timings)**
    * **Camera/Locator processing time** : temps de prise de vue de chaque image et reconnaissance des composants.
    * **Total vision processing Time** : somme des temps de la caméra et du localisateur.
    * **Total FlexiBowl® / Robot time** : temps pour une séquence de mouvement FB et un seul pick & place du robot.
    * **Total processing time** : temps de traitement total (Vision + FB + Robot).
    * **Fill hopper** : historique des déchargements de la trémie sur le disque du FlexiBowl®.
    * **Vision - FlexiBowl® - Robot** : graphique comparatif des trois fonctions pour comprendre l'impact de chaque processus sur le temps total.
* - 6
  - **Graphiques des performances et historique**
    * **Liste des modèles détectés** : tableau avec les coordonnées (**X**, **Y**), la rotation (**Rot**) du composant et le **Score** (degré de similarité de l'objet détecté avec le modèle de référence).
    * **Parts per minute** : graphique de la moyenne des pièces prélevées par minute.
```