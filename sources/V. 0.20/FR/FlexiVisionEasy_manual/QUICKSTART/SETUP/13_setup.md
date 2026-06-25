(setupcomponenti)=
# **Configuration initiale du système**

Cette section guide l'utilisateur dans la configuration complète des composants matériels et logiciels du système FlexiVision One. Il est essentiel de suivre les étapes dans l'ordre indiqué pour assurer le bon fonctionnement du système.

```{note}
**Pré-requis**

Avant de commencer la configuration du logiciel, s’assurer que :
- L'installation mécanique de tous les composants est terminée ([Installation mécanique](Installazione_Meccanica))
- Tous les câbles sont correctement connectés ([Câblage et connexions](cablaggio)) 
```
![WorkFlow](../../../../../_shared/media/images/workflow.png)
---

## Aperçu de la procédure de configuration

La procédure de configuration initiale comprend sept étapes principales :

0. **Saisie de la clé de licence** fournie dans le kit
1. **Login** - Accès au logiciel avec les identifiants de l'utilisateur
2. si le dispositif d’éclairage est présent : **Configuration de l'adresse IP du FlexiBowl®** et **allumage du rétroéclairage**
3. **Camera Setup** - Configuration de la caméra
4. **FlexiBowl Setup** - Connexion et configuration du FlexiBowl®
5. **Hopper Setup** - Configuration de la trémie
6. **Robot Setup** - Configuration de la communication avec le robot
7. **Protocol Setup** - Configuration des paramètres de protocole
8. **Renommer et enregistrer la recette de base** - Configuration du profil d'application



```{warning}
**Ordre des étapes**

L'ordre des configurations est important ! Ne pas sauter d'étapes et ne pas modifier l'ordre, car certaines configurations dépendent des précédentes.
```

---

## Opérations préliminaires

:::{important}
La première étape avant de démarrer le logiciel FlexiVision One consiste à insérer la clé de licence fournie avec le kit.
:::

### *Connexion au système*

Au démarrage du logiciel FlexiVision One, la page d'accueil s'affiche.
```{list-table} 
   :widths: 10 90
   :header-rows: 0
   * - **0**
     - Cliquer sur Setup
   * - **1**
     - **Sélectionner l'utilisateur ENGINEER** dans le menu déroulant en haut à droite.
   * - **2**
     - **Entrer le mot de passe** « 3&nbsp;».
   * - **3**
     - Cliquer sur le bouton **LOGIN** pour accéder à l'interface.
```

```{tip}
**Gestion des utilisateurs**

FlexiVision One supporte plusieurs profils d'utilisateurs avec différents niveaux d'autorisation :
- **ARS**
- **Engineer**
- **Technician**
- **Operator**
```

---

### *Allumer le rétro-éclairage s'il est présent*

Après la première connexion, s’il faut activer la licence FlexiVision One, suivre les étapes suivantes :

```{list-table}
* - **4** 
  - Depuis la page principale du logiciel, cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **5**
  - Sur la page SETUP, identifier et cliquer sur l'icône **FlexiBowl® Setup**
    ```{dropdown} Page Setup 
       ![Page Setup](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **6**
  - L'écran de configuration du FlexiBowl® s'ouvre
* - **7**
  - Saisir l'adresse IP du FlexiBowl® (par défaut&nbsp;: `192.168.1.10` )
* - **8**
  Après avoir saisi l'adresse IP, cliquer sur le bouton **Connection** **Test**
* - **9**
  Le système effectue un test de communication (ping) avec le FlexiBowl®.
* - **10**
  - Observer l'indicateur de **Statut** :
    - 🟢 **Vert** : Connexion établie avec succès
    - 🔴 **Rouge :** Échec de la connexion (vérifier l'adresse IP et le câblage)
* - **11** 
  - Cliquer sur le bouton <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **12**
  - Une fenêtre s'ouvre avec les paramètres configurables du FlexiBowl®
* - **13**
  - Activer le rétro-éclairage en cochant la case «&nbsp;Light ON ».
```

---

## Configuration matérielle

Une fois les étapes préliminaires terminées, procéder à la configuration des composants matériels dans l'ordre suivant.

Toutes les configurations matérielles sont accessibles à partir de la page centrale **SETUP** du logiciel.


```{list-table} 
* - **14** 
  - Depuis le menu principal, cliquer sur <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **15** 
  - Les icônes des différents composants à configurer sont affichées.
* - **16**
  - Cliquer sur l'icône du composant souhaité pour accéder à sa configuration spécifique.
```

---

```{toctree}
:hidden:
13d_Camera_Setup.md
14_calibrazione_camera.md
13a_FB_Setup.md
13b_Hopper_Setup.md
13c_Robot_Setup.md
15_Protocol_Setup.md
15b_SaveRecipe.md
```

