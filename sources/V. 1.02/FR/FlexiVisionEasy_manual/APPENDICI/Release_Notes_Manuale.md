# Manuel FlexiVision One

Cette page rassemble l'historique des révisions du présent manuel et indique avec quelles versions du logiciel FlexiVision One chaque révision est compatible.

```{important}
Consultez toujours la version du manuel compatible avec la version du logiciel installée afin d'accéder aux informations les plus à jour sur les fonctionnalités, la sécurité et les procédures.
```

## Compatibilité

| Version du manuel | Versions compatibles du logiciel FlexiVision One |
|---|---|
| **1.02** (actuelle) | v0.23, v0.24 |
| **1.01** | v0.21, v0.22 |
| **1.00** | v0.20, v0.21, v0.22 |

## Historique des révisions

### Version 1.02

Date de publication: 17/11/2026

**Pages ajoutées**

- Nouvelle section **Caméras de contrôle**, avec les pages :
  - [Caméras de contrôle](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) : présentation, séquence de fonctionnement, utilisation depuis la HMI (Setup Camera Ctrl, Setup Tool Ctrl, View Runtime, Test Tool) et test d'acceptation rapide.
  - [Commande `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md) : format de la commande, paramètres, réponses au robot et exemples d'échange.
  - [Script VisionPro](../TELECAMERE_CONTROLLO/35_Script_VisionPro.md) : interface du ToolBlock, personnalisation du script et Annexe A avec le script C# complet.
- Ajout de la page [Dépannage – Caméras de contrôle](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) avec les messages `#Error_Control_…` et `#Error_Camera…` et les actions recommandées.
- Toutes les pages de la section Caméras de contrôle affichent en haut un bandeau indiquant que la **Control Camera** est une fonction **Expert**.

**Pages mises à jour**

- [Protocole de communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) : ajout de la sous-section « Commandes des caméras de contrôle » avec la commande `start_control_<paramètre>`.
- [Dépannage](../TROUBLESHOOTING/26_trb_shooting_guide.md) : ajout de la fiche « Caméras de contrôle ».
- [Glossaire](../27b_Glossario.md) : ajout des termes CogRecord, PMRedLine, Caméra de contrôle, ToolBlock et VisionPro.
- Notes de version – Logiciel : ajout des versions [V. 0.23](V.0.23.md) et [V. 0.24](V.0.24.md) et mise à jour de la page [Logiciel FlexiVision One](Release_Notes_Software.md).
- Mise à jour du tableau de compatibilité avec les versions logicielles v0.23 et v0.24.

### Version 1.01

Date de publication : 04/09/2026

- Ajout de la page **Check Belt** (Surveillance de la bande) dans le Quickstart et de l'entrée correspondante dans la page Setup de la Vue d'ensemble de l'interface.
- Mise à jour de la section Hopper Setup avec les procédures guidées **Wizard Steps** et **Wizard Time**.
- Mise à jour de la section Histogrammes avec le choix du type de région pour les Clearances (Rectangle, Annulus Section, Circle).
- Mise à jour de la section Applications Mix avec les commandes multi-modèles `mix_Locator_<modèles>` et la protection pour les commandes déjà en cours d'exécution.
- Ajout au Protocole de communication Robot-Vision de la sous-section « Comment utiliser correctement les commandes Start et Mix ».
- Mise à jour de la section FlexiBowl® Setup : saisie manuelle des paramètres au clavier et avertissement en cas de paramètres non synchronisés.
- Mise à jour de la section Robot Pick : format des offsets avec le point comme séparateur décimal et contrôle du Picking Offset avant de poursuivre avec **Next**.
- Ajout à la section Setup de l'indication relative au contrôle du niveau d'accès de l'utilisateur.
- Réorganisation de la section Notes de version, avec séparation des notes du logiciel FlexiVision One et de celles du manuel.

### Version 1.00

Date de publication : 01/08/2026

- Première édition du manuel.