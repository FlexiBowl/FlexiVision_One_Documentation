(troubleshooting_telecamere_controllo)=
# **Caméras de contrôle**

```{important}
**Fonction Expert**

La gestion des caméras de contrôle (**Control Camera**) est une fonction **Expert** : elle requiert la connaissance de Cognex VisionPro et des scripts C#, et s'adresse aux utilisateurs expérimentés. Pour plus d'informations sur le mode Expert, consultez [Qu'est-ce que c'est et quand sert-il ?](../EXPERT/32_Expert.md).
```

```{note}
Cette page concerne la commande `start_control_` et les scripts VisionPro (disponibles à partir de la version logicielle v0.24). Pour la procédure complète, reportez-vous à [Caméras de contrôle](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) et à [Commande `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md).
```

## Réponses et messages d'erreur

Les erreurs relatives au script de contrôle commencent par `#Error_Control_`. Le cas `Not_Found` **n'est pas une erreur logicielle** : il signifie que le locator n'a détecté aucun objet. Les erreurs de la caméra peuvent être signalées séparément avec le préfixe `#Error_Camera`.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Réponse
  - Signification / action recommandée
* - `Not_Found`
  - Inspection terminée sans reconnaissance : vérifier la pièce, l'image et le modèle.
* - `#Error_Control_INVALID_CONTROL`
  - Le paramètre n'est pas géré par le script : vérifier le texte après `start_control_`.
* - `#Error_Control_TOOL_NOT_FOUND`
  - Un des outils attendus est absent ou porte un nom différent.
* - `#Error_Control_LAST_RECORD_NULL`
  - L'enregistrement de la dernière exécution de l'outil n'est pas disponible.
* - `#Error_Control_INPUT_IMAGE_RECORD_NULL`
  - Le sous-enregistrement `InputImage` n'est pas disponible.
* - `#Error_Control_RECORD_WITHOUT_IMAGE`
  - L'enregistrement sélectionné ne contient pas d'image valide.
* - `#Error_Control_VISIONPRO_JOB`
  - L'exécution de la tâche VisionPro a généré une erreur.
* - `#Error_Control_EMPTY_OUTPUT`
  - Le script n'a pas renvoyé de chaîne valide.
* - `#Error_Camera …`
  - Problème d'acquisition : vérifier la connexion et l'état de la caméra.
```

```{note}
Le script d'exemple peut également renvoyer `#Error_Control_TOOL_RUN` lorsque les résultats d'un outil ne sont pas disponibles (par exemple `#Error_Control_TOOL_RUN;Tool=2` si l'erreur concerne l'outil 2). Si au moins un outil produit une erreur d'exécution, l'erreur est écrite au début de la réponse.
```

## Vérifications rapides

- Vérifier que la commande comporte le **caractère de soulignement final** (`start_control_`) et que le paramètre ne contient pas d'espaces.
- Vérifier que les noms d'entrée et de sortie du ToolBlock sont restés `Image`, `Input_Control`, `Output_String` et `Output_Image`.
- Vérifier que la sortie `Output_Image` est configurée comme un `CogRecord` compatible.
- Exécuter **Test Tool** depuis la HMI même sans robot connecté pour isoler le problème de la communication TCP : dans ce cas, le résultat est affiché dans la HMI mais n'est pas transmis au robot.
- Après chaque modification du script, répéter le [test d'acceptation rapide](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md).
