(telecamere_controllo)=
# **Caméras de contrôle**

```{important}
**Fonction Expert**

La gestion des caméras de contrôle (**Control Camera**) est une fonction **Expert** : elle requiert la connaissance de Cognex VisionPro et des scripts C#, et s'adresse aux utilisateurs expérimentés. Pour plus d'informations sur le mode Expert, consultez [Qu'est-ce que c'est et quand sert-il ?](../EXPERT/32_Expert.md).
```

```{note}
**Disponible à partir de la version logicielle v0.24**

Les fonctions décrites dans cette section ont été introduites avec FlexiVision One v0.24. Consultez les [Notes de version – V. 0.24](../APPENDICI/V.0.24.md).
```

Outre la caméra de vision utilisée pour la préhension, FlexiVision One gère **3 caméras de contrôle indépendantes**, associées respectivement à **FLB1**, **FLB2** et **FLB3**. Les caméras de contrôle permettent d'effectuer une **inspection visuelle** à la demande du robot, par exemple la vérification d'une pièce prélevée, et de renvoyer au robot le résultat du contrôle.

## À quoi ça sert

La commande `start_control_` permet au robot de demander à FlexiVision une inspection avec une caméra de contrôle. Le robot peut ajouter un **paramètre textuel** après le caractère de soulignement (`_`) : FlexiVision transmet le paramètre au **script VisionPro**, qui décide quels outils exécuter et quels résultats renvoyer.

```{important}
**Principe de fonctionnement**

La configuration HMI reste inchangée : le client peut adapter les règles d'inspection et le format des résultats en modifiant son propre **script VisionPro**, sans intervenir sur l'interface de FlexiVision One.
```

## Séquence de fonctionnement

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - #
  - Acteur
  - Action
* - 1
  - **Robot**
  - Envoie `start_control_` ou `start_control_<paramètre>`.
* - 2
  - **FlexiVision**
  - Acquiert l'image avec la caméra de contrôle associée et lance le script VisionPro.
* - 3
  - **VisionPro**
  - Exécute les outils sélectionnés et prépare une réponse textuelle et un enregistrement graphique.
* - 4
  - **FlexiVision**
  - Affiche l'image et la chaîne dans la HMI ; envoie la chaîne au robot **uniquement s'il est connecté**.
```

Pour chaque contrôle, FlexiVision gère une **Main Task** dédiée à la caméra de contrôle, avec gestion des erreurs, journalisation et envoi des résultats au robot.

## Utilisation depuis la HMI

Les pages HMI des caméras de contrôle sont **partagées** entre les dispositifs : depuis la section **Control FlexiBowl®**, sélectionnez le dispositif concerné.

```{list-table}
:header-rows: 1
:widths: 25 75

* - Page
  - Fonction
* - **Setup Camera Ctrl**
  - Configuration de la caméra de contrôle.
* - **Setup Tool Ctrl**
  - Configuration de VisionPro : permet d'intervenir sur les outils et sur le script VisionPro (voir [Script VisionPro](35_Script_VisionPro.md)).
* - **View Runtime**
  - Affichage de l'image et du résultat du contrôle.
* - **Test Tool**
  - Lance un contrôle local, même sans robot connecté.
```

```{note}
Avec la commande **Test Tool**, le contrôle est exécuté même **sans robot connecté** : dans ce cas, le résultat est affiché dans la HMI mais **n'est pas transmis via TCP**.
```

## Test d'acceptation rapide

Après avoir installé ou modifié le script VisionPro, effectuez les vérifications suivantes :

- ☐ Envoyer `start_control_1` et vérifier le résultat textuel et l'image du PMRedLine 1.
- ☐ Envoyer `start_control_2` et vérifier le résultat textuel et l'image du PMRedLine 2.
- ☐ Envoyer `start_control_` et vérifier que la chaîne contient les deux résultats.
- ☐ Envoyer `start_control_ABC` et vérifier l'erreur `INVALID_CONTROL` du script d'exemple.
- ☐ Exécuter **Test Tool** avec le robot déconnecté et vérifier que la HMI et VisionPro restent opérationnels.

## Pour aller plus loin

- [Commande `start_control_`](34_Comando_start_control.md) : format de la commande, paramètres, réponses et exemples d'échange.
- [Script VisionPro](35_Script_VisionPro.md) : interface du script, personnalisation et code d'exemple complet.
- [Dépannage – Caméras de contrôle](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) : messages d'erreur et actions recommandées.
- [Protocole de communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) : liste complète des commandes robot.
