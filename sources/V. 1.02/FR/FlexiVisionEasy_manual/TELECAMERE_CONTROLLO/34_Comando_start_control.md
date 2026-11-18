(start_control)=
# **Commande `start_control_`**

```{important}
**Fonction Expert**

La gestion des caméras de contrôle (**Control Camera**) est une fonction **Expert** : elle requiert la connaissance de Cognex VisionPro et des scripts C#, et s'adresse aux utilisateurs expérimentés. Pour plus d'informations sur le mode Expert, consultez [Qu'est-ce que c'est et quand sert-il ?](../EXPERT/32_Expert.md).
```

```{note}
**Prérequis**

La commande `start_control_` nécessite une caméra de contrôle configurée et un script VisionPro chargé. Consultez [Caméras de contrôle](33_Telecamere_Controllo.md). Disponible à partir de la version logicielle v0.24.
```

La commande `start_control_` permet au robot de demander une inspection visuelle avec une caméra de contrôle. Le robot peut ajouter un paramètre textuel, que FlexiVision transmet au [script VisionPro](35_Script_VisionPro.md).

## Format de la commande

```
start_control_<paramètre>
```

Le **caractère de soulignement final** du préfixe est **obligatoire**. Le paramètre peut être vide ou contenir des chiffres, des lettres et d'autres caractères de soulignement.

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Commande envoyée par le robot
  - Texte reçu par VisionPro
  - Comportement du script d'exemple
* - `start_control_`
  - `""` (vide)
  - Exécute les deux PMRedLine
* - `start_control_1`
  - `"1"`
  - Exécute uniquement PMRedLine 1
* - `start_control_2`
  - `"2"`
  - Exécute uniquement PMRedLine 2
* - `start_control_ABC_123`
  - `"ABC_123"`
  - Paramètre personnalisé : nécessite une logique dédiée dans le script
```

```{important}
Le paramètre est traité comme du **texte**. FlexiVision n'attribue aucune signification à des valeurs telles que `ABC_123` : c'est le script VisionPro du client qui doit les interpréter.
```

```{note}
`start_control_ 1` est également lu comme paramètre `"1"` : les espaces au début et à la fin sont supprimés. Pour éviter toute ambiguïté, il est recommandé d'envoyer `start_control_1`, sans espaces.

Le préfixe `start_control_` n'est pas transmis au script : seule la partie qui suit est reçue (par exemple `"2"` pour `start_control_2`).
```

La commande peut également être exécutée **sans robot connecté** depuis la HMI via **Test Tool** ; dans ce cas, le résultat est affiché dans la HMI mais n'est pas transmis via TCP.

## Réponse au robot

La réponse est la chaîne `Output_String` produite par le script VisionPro. Le format présenté ci-dessous est celui du **script d'exemple** et peut être adapté au protocole requis par le robot.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Situation
  - Exemple d'Output_String
* - Objet trouvé
  - `X=125.450;Y=78.320;Rz=45.000`
* - Aucun objet trouvé
  - `Not_Found`
* - Les deux outils exécutés
  - `1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found`
* - Paramètre non prévu
  - `#Error_Control_INVALID_CONTROL`
* - Erreur sur l'outil 2
  - `#Error_Control_TOOL_RUN;Tool=2`
```

Pour chaque outil exécuté, seul le **premier objet** reconnu est utilisé. Si les deux outils sont exécutés, les réponses sont précédées des préfixes `1:` et `2:` et séparées par `|`.

```{note}
- `X` et `Y` sont exprimés dans le système de coordonnées configuré dans l'outil VisionPro (pixels ou unités calibrées) : ils ne sont pas automatiquement en millimètres.
- `Rz` est exprimé en degrés.
- Trois décimales ; le point est toujours utilisé comme séparateur décimal, quelle que soit la langue de Windows.
```

### Not_Found et erreurs

`Not_Found` **n'est pas une erreur** : il indique que l'outil a été exécuté mais n'a trouvé aucun objet. Les **erreurs des scripts de contrôle** commencent toujours par le préfixe `#Error_Control_` ; les erreurs de la caméra peuvent être signalées séparément avec le préfixe `#Error_Camera`. Si au moins un outil produit une erreur d'exécution, le script écrit l'erreur au début de la réponse (dans l'exemple, l'outil 1 est prioritaire).

La liste complète des messages et des actions recommandées est disponible dans [Dépannage – Caméras de contrôle](../TROUBLESHOOTING/26j_Telecamere_Controllo.md).

## Exemples d'échange

**Cas A – Locator 2 uniquement**

Commande envoyée par le robot : `start_control_2`. VisionPro reçoit `Input_Control = "2"`, exécute `CogPMRedLineTool2`, lit X, Y et Rz du premier résultat et produit la réponse textuelle. L'affichage montre l'enregistrement de l'outil 2.

**Cas B – deux Locators**

Commande envoyée : `start_control_`. VisionPro reçoit une chaîne vide et exécute les deux outils. La réponse contient deux sections, une pour chaque locator. L'enregistrement de l'image provient de l'outil 1, sauf choix différent dans le script.

**Cas C – paramètre applicatif**

Commande envoyée : `start_control_ABC_123`. Le paramètre parvient à VisionPro sans être interprété par FlexiVision. Le script d'exemple répond `#Error_Control_INVALID_CONTROL` ; pour l'utiliser comme commande réelle, il faut ajouter la logique correspondante dans le script C#.

```{tip}
Pour la liste complète des commandes robot, consultez [Protocole de communication Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
