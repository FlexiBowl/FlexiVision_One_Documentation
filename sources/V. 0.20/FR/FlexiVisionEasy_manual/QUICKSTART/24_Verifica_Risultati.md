(dashboard)=
# **Suivi de l'application : Dashboard**

Le **tableau de bord** est l'interface principale pour la surveillance en temps réel du système FlexiVision One. Cette page permet de vérifier l'efficacité du processus, d'analyser les temps de cycle, de valider la reconnaissance des composants et d'identifier les éventuels goulets d'étranglement dans le système.


---

## Aperçu de l'interface

L'interface du tableau de bord est divisée en quatre sections principales :
![Page Dashboard](../../../../_shared/media/images/pagina_dashboard.png)
1. [**Contrôle opérationnel**](controllooperativo) : Commandes et état d'exécution
2. [**Analyse de la vision**](analisivisione) : Affichage des pièces détectées et des détails
3. [**Indicateurs de performance**](indicatoriperformance) : Connectivité et temps de cycle
4. [**Analyse graphique**](analisigrafica) : Graphiques historiques de la productivité et temporels

---
(controllooperativo)=
## Contrôle opérationnel - Commandes et état d'exécution

```{list-table}
:header-rows: 1
:widths: 25 75

* - Élément
  - Description et fonction
* - **In run**
  - Indicateur d'état indiquant si le système est en cours d'exécution.  
    **Vert** 🟢 : Système actif et opérationnel.  
    **Rouge** 🔴 : Le système est arrêté ou en pause.
* - **In Run Time**
  - Affiche la durée totale de fonctionnement du système depuis le démarrage de l'application. 
* - **Sélection FlexiBowl®**
  - Menu déroulant permettant de sélectionner le FlexiBowl® spécifique à surveiller. 
* - **Test Locator**
  - Prend une photo de la zone de visualisation et lance la reconnaissance des composants présents. 
```

```{tip}
**Test Locator**
Utile pour :
- Vérifier que les composants sont bien reconnus par le système de vision 
- En cas de collision entre le robot et un composant, et si je souhaite vérifier la fiabilité des clearances
```

---
(analisivisione)=
## Analyse de la vision

Le centre du tableau de bord présente les données relatives aux composants identifiés par le système de vision.

### *Detected Vision Parts*

**Detected Vision Parts** montre les éléments suivants :
- Image acquise en temps réel par la caméra
- **Graphique historique** des détections au cours des 30 dernières secondes montrant l'évolution du nombre de pièces reconnues par acquisition.


### *Tableau des modèles détectés*

**Détail des composants reconnus**

Le tableau situé sous l'image répertorie tous les composants de la zone de prélèvement avec les paramètres suivants :

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Champ
  - Type de données
  - Description
* - **Id**
  - Entier
  - Identifiant unique du composant progressif (0, 1, 2, ...).   
  Id 0 = composant ayant le score le plus élevé (la meilleure correspondance avec le modèle si l'ordre des scores est décroissant, comme recommandé).
* - **X**
  - Millimètres
  - Coordonnée X du composant.
* - **Y**
  - Millimètres
  - Coordonnée Y du composant.
* - **Rot (Rotation)**
  - Degrés
  - Angle de rotation du composant. 
* - **Score**
  - Pourcentage
  - Valeur en pourcentage (0,00-1,00 ou 0 %-100 %) exprimant le degré de fiabilité de la reconnaissance. Il représente la proximité/fidélité au modèle de référence. Score plus élevé = meilleure correspondance.
```

```{list-table} **Interprétation du Score**

* - **Score > 0.90 (90 %) :**
  - 
    - Convient parfaitement au modèle
    - Picking à haute confiance

* - **Score 0.80-0.90 (80-90 %) :**
  - 
    - Bonne correspondance
    - Picking sécurisé si l'Accept Threshold est correctement configuré

* - **Score 0.70-0.80 (70-80 %) :**
  - 
    - Correspondance acceptable
    - Vérifier la cohérence au fil du temps

* - **Score < 0.70 (< 70 %) :**
  - 
    - Mauvaise correspondance
    - En cas de problème récurrent, veuillez consulter le modèle ou l'Accept Threshold.
```

---
(indicatoriperformance)=
## Indicateurs de statut et de performance

### *Connectivité*

Indicateurs d'état des communications avec des dispositifs externes :

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indicateur
  - Description
* - **FlexiBowl®**
  - État de la connexion matérielle entre le VisionController (PC) et le FlexiBowl®.  
    **Vert** : Connecté et communicant.  
    **Rouge** : Déconnecté ou erreur de communication.
* - **Robot**
  - État de la communication avec le robot.   
    **Vert** : Connexion TCP/IP établie.  
    **Rouge** : Déconnecté ou délai de communication dépassé.
```

```{warning}
**Actions à entreprendre en cas de déconnexion**

**FlexiBowl® rouge** :
- Vérifier le câble Ethernet FlexiBowl® → VisionController
- Vérifier l'alimentation électrique du FlexiBowl®
- Vérifier l'IP du FlexiBowl® dans FlexiBowl® Setup
- Tenter une reconnexion ou un redémarrage du logiciel

**Robot rouge** :
- Vérifier le câble Ethernet Robot → VisionController
- Vérifier que le robot a une connexion TCP/IP ouverte
- Vérifier le port TCP/IP dans Robot Setup
- Vérifier le programme du robot (l'adresse IP du VisionController et le port ont été correctement introduits dans la section de configuration du robot)

En production, les deux indicateurs doivent toujours être verts.
```

### *Analyse des temps*

Le système fournit un breakdown détaillé des temps de cycle afin d'identifier les éventuels goulets d'étranglement et d'optimiser le processus.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Élément temporel
  - Description
* - **Camera Processing Time**
  - Temps nécessaire à l'acquisition de l'image à partir du capteur de la caméra. Comprend le temps d'exposition et le transfert de données. 
* - **Locator Processing Time**
  - Temps nécessaire à l'algorithme de vision pour localiser et reconnaître les composants dans l'image acquise. Il dépend du nombre de modèles actifs, de la complexité des modèles et du nombre de clearances. 
* - **Total Vision Processing**
  - Somme des temps de la caméra et du localisateur. Il représente le temps total nécessaire au système de vision pour traiter une image et envoyer les coordonnées.       
* - **Total FlexiBowl® Time**
  - Temps nécessaire au FlexiBowl® pour effectuer une séquence complète de manutention. 
* - **Total Robot Time**
  - Temps estimé ou détecté pour l'opération complète de prélèvement et de placement du robot. Il inclut : rapprochement → prise → levage → dépose → retour. 
* - **Total Processing Time**
  - Temps de cycle total (Vision + FlexiBowl® + Robot). Il représente le temps écoulé entre le début d'un cycle et le début du suivant. Détermine la productivité maximale théorique (PPM).
```

```{tip}
**Interprétation temporelle pour l'optimisation**

Le graphique temporel permet d'identifier le **goulot d'étranglement** du système :

**Si Total Vision Processing est le plus élevé** :
- Trop de modèles actifs → Désactiver les modèles inutiles
- Modèles trop complexes → Simplifier avec un Score Threshold plus élevé
- Trop de Clearances → Réduire le nombre ou la taille des clearances
- Traitement de la caméra élevé → Réduire le temps d'exposition

**Si Total FlexiBowl® Time est le plus élevé** :
- Trop de pauses → Optimiser la synchronisation Flip/Move et réduire la pause de stabilisation (Pause X ms)
- Séquence de manutention trop lente → Augmenter la vitesse dans Config FlexiBowl®
- Angle de rotation excessif → Réduire le Move Angle
- Secousses trop longues → Augmenter la vitesse SHAKE et réduire les cycles SHAKE  

**Si Total Robot Time est le plus élevé** :
- Trajectoire du robot non optimisée → Optimiser path planning robot
- Vitesse du robot trop faible → Augmenter la vitesse de déplacement (si elle est sûre)
- Distance de dépose trop longue → Rapprocher le point de dépose
- Temps de préhension trop longs → Optimiser l'ouverture/la fermeture du préhenseur

**Objectif d'optimisation** : Équilibrer les trois temps pour réduire le Total Processing Time général.
```

---
(analisigrafica)=
## Analyse graphique

Les graphiques situés en bas du tableau de bord permettent une analyse prédictive et diagnostique des performances du système au fil du temps.

### *1. Parts Per Minute (PPM)*

```{list-table}
* - **Graphique de productivité**
  - Indique la productivité moyenne du système exprimée en **composants prélevés par minute** (Parts Per Minute).

* - **Caractéristiques** :
  - 
    - Axe X : Temps 
    - Axe Y : PPM (pièces/seconde)
    - Ligne de tendance : Moyenne mobile pour identifier les tendances

* - **Utilisation** :
  - 
    - Contrôler la stabilité de la productivité dans le temps
    - Identifier les dégradations de performance
    - Calculer le débit réel par rapport au débit théorique
```

```{tip}

  :::{list-table} **Interprétation de la PPM**

    * - **PPM constant et stable** :
      - 
        ✓ Système bien configuré  
        ✓ Paramètres optimisés  
        ✓ Aucun goulet d'étranglement critique  

    * - **PPM progressivement décroissant** :
      - 
        ⚠️ Usure possible des composants (surface de préhension du FlexiBowl®)  
        ⚠️ Trémie qui se vide 
        ⚠️ Accumulation de saleté sur la caméra/l'éclairage  

    * - **PPM avec de fortes fluctuations** :
      - 
        ⚠️ Instabilité du processus  
        ⚠️ Problèmes de reconnaissance intermittents  
        ⚠️ Interférences externes (vibrations, lumière variable)  

    * - **Mesures correctives** :
      - 
        - Analyser la corrélation avec les graphiques temporels
        - Identifier le composant (Vision/FlexiBowl®/Robot) à l'origine des variations
        - Intervenir sur des paramètres spécifiques
  :::
```

### *2. Fill Hopper*

```{list-table}
* - **Graphique d'activation de la trémie**
  - Représente l'historique des impulsions de déchargement envoyées à la trémie (Hopper).

* - **Caractéristiques** :
  - 
    - Axe X : Temps
    - Axe Y : Activations de la trémie (événements)
    - Pics : Chaque pic représente une activation de déchargement

* - **Utilisation** :
  - 
    - Vérifier l'efficacité de la configuration de la trémie
    - Identifier les anomalies dans le comportement de déchargement
```

```{tip}
  
  :::{list-table} **Analyse du pattern Fill Hopper**

    * - **Activations régulières et constantes** :
      - 
        ✓ Configuration optimale de la trémie  
        ✓ Flux de pièces stable et prévisible  
        ✓ Autonomie calculée (par exemple, activation toutes les 10 minutes)  

    * - **Activations de plus en plus fréquentes** :
      - 
        ⚠️ La trémie se vide (moins de pièces = plus d'activations pour maintenir le niveau)  
        ⚠️ Temps de déchargement insuffisant en raison d'un volume réduit    
        **Action** : Recharger bientôt la trémie

    * - **Aucune activation depuis longtemps** :
      - 
        ⚠️ Robot arrêté ou ralenti (pièces non consommées)  
        ⚠️ Problème de système possible ne nécessitant pas de pièces    
        **Action** : Vérifier l'état de la production

    * - **Activations très rapprochées (rafales)** :
      - 
        ⚠️ Seuil de trémie mal configuré (trop élevé)  
        ⚠️ Étapes insuffisantes (pièces n'arrivant pas à temps)  
        **Action** : Revoir Config Hopper
  :::
```

### *3. Vision - FlexiBowl® - Robot (Graphique comparatif)*

```{list-table} 
* - **Graphique des temps superposés**
  - Un graphique comparatif à trois lignes qui superpose le déroulement des différents processus au fil du temps.

* - **Utilisation** : 
  - Identifier instantanément le processus qui influe le plus sur le temps de cycle total et comment il varie dans le temps.
```
---

## Suivi de la qualité - Indicateurs critiques à surveiller

```{list-table}
* - **Score des composants**
  - S'assurer que le **Score** des composants détectés est constamment supérieur au seuil de tolérance (Accept Threshold) défini lors de la configuration du modèle.

* - **Suivi du score** :
  - 
    - Vérifier périodiquement le tableau Modèles détectés
    - Vérifier que les scores typiques sont compris entre 0,85 et 0,95
    - Enquêter si les scores tombent régulièrement en dessous de 0,80

* - **Diminution progressive des scores** :
  - 
    ⚠️ Pièces réelles différentes de celles de training (variations de production)  
    ⚠️ Éclairage modifié (backlight plus faible, saleté)  
    ⚠️ La caméra n'est plus au point (vibrations, chocs)  
    ⚠️ La surface du FlexiBowl® est sale (motif d'interférence)  

* - **Actions correctives** :
  - 
    - Nettoyer la caméra, l'éclairage, la surface du FlexiBowl®
    - Vérifier la mise au point de la caméra
    - Envisager un nouvel apprentissage du modèle si les pièces ont changé
    - Réduire l'Accept Threshold si les résultats sont toujours fiables mais moins élevés
```
---

## Best Practices en matière de suivi de la production

### *Contrôles quotidiens*

```{list-table}
* - **Au début de la production** (5 minutes) :
  - 
    - Vérifier les indicateurs de connectivité du FlexiBowl® et du robot (verts)
    - Vérifier que les premiers cycles affichent des scores normaux (>0,85)
    - Vérifier que le PPM se stabilise à la valeur attendue

* - **Pendant la production** (vérification toutes les 1 à 2 heures) :
  - 
    - Consulter le PPM pour vérifier la stabilité
    - Vérifier la Fill Hopper pour prévoir les remplissages nécessaires
    - Vérifier l'absence d'erreurs ou d'alertes dans le journal

* - **À la fin du quart de travail** (2 minutes) :
  - 
    - Noter le PPM moyen du quart de travail
    - Vérifier le nombre d'activations de la trémie
    - Vérifier les anomalies ou les événements
    - Comparer avec les données de la veille
```
Cette routine minimale permet d'identifier rapidement les problèmes et de maintenir la traçabilité des performances.

### *Report performance*  

```{tip} **Indicateurs clés à suivre**
Pour évaluer les performances au fil du temps, il convient d'effectuer un suivi :

  :::{list-table} 

    * - **Tous les jours** :
      - 
        - PPM moyen du quart de travail
        - Nombre total de pièces collectées
        - Nombre d'activations de la trémie
        - Temps d'arrêt total (et causes)

    * - **Toutes les semaines** :
      - 
        - Tendance PPM (à la hausse/à la baisse ?)
        - Comparaison entre les valeurs théoriques et réelles en PPM
        - Score moyen des composants détectés
        - Toute modification de configuration et son impact

    * - **Tous les mois** :
      - 
        - Efficacité globale des équipements (OEE)
        - Analyse des principaux goulets d'étranglement
        - Nécessité d'une maintenance prédictive
        - ROI du système
  :::

Ces données permettent une optimisation continue et justifient l'investissement dans des améliorations.
```

---

```{raw} html
<div style="border: 2px solid #0d6efd; border-radius: 12px; padding: 2rem; margin: 1.5rem 0; background-color: #f0f6ff; display: flex; align-items: flex-start; gap: 2rem;">
  <div style="flex: 1; min-width: 0;">
    <div style="font-size: 1.2rem; font-weight: 700; color: #0d6efd; margin-bottom: 0.5rem;"> Le système est désormais opérationnel !</div>
    <div style="font-size: 0.95rem; color: #444; line-height: 1.6;">Félicitations ! Le système FlexiVision One est désormais entièrement configuré, optimisé et validé pour la production.</div>
  </div>
  <div style="flex: 1.4; background: white; border-radius: 8px; padding: 1.2rem 1.5rem; border: 1px solid #d0e4ff; font-size: 0.88rem; color: #333; line-height: 1.8;">
    <div style="font-weight: 600; margin-bottom: 0.5rem;">Récapitulatif du parcours terminé&nbsp;:</div>
    <div>✓ Configuration matérielle (FlexiBowl®, robot, caméra)</div>
    <div>✓ Calibrage complet (caméra, robot)</div>
    <div>✓ FlexiBowl® configuré pour une manutention optimale</div>
    <div>✓ Trémie configurée pour l'alimentation automatique (le cas échéant)</div>
    <div>✓ Modèles de pièces créés et optimisés</div>
    <div>✓ Système validé avec surveillance par tableau de bord</div>
    <div>✓ Performances vérifiées et stables</div>
    <div style="margin-top: 0.8rem; font-style: italic; color: #555;">Le système est prêt à fonctionner en production avec une supervision minimale.</div>
  </div>
  <div style="flex: 0.7; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.9rem;">
    <div style="color: #555; font-weight: 600;">Derniers outils utiles&nbsp;:</div>
    <a href="../TROUBLESHOOTING/26_trb_shooting_guide.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Troubleshooting</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Guide de dépannage pour les problèmes courants</div>
    <a href="../27_Support.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Support</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Contacts de l'assistance technique</div>
  </div>
</div>
```