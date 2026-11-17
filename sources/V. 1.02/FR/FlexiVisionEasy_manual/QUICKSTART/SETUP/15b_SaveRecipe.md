(ricettabase)=
# **Sauvegarder la recette**

Une fois toutes les configurations des composants terminées, la dernière étape avant de passer à la création du modèle consiste à sauvegarder la recette.

````{list-table}
:header-rows: 0
:widths: 10 90

* - **1**
  - Accéder à la section <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon" > à partir du bouton du haut

* - **2**
  - Saisir le nom de la recette.

    Utiliser un nom descriptif (par ex : «&nbsp;Recette_Base&nbsp;»).

    Éviter les caractères spéciaux ou les espaces (utiliser les underscores `_` à la place des espaces).

* - **3**
  - Renommer la recette dupliquée   
    **Conventions recommandées :**
    - Noms qui identifient clairement la pièce ou l'application
    - Pas d'espaces (utiliser `_` ou `-`)
    - Inclure des informations pertinentes (type de pièce, taille, application)
    
    :::{tip}
    **Éviter les noms génériques**

    ❌ Noms à éviter :
    - `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

    ✓ Noms recommandés :
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    **Format suggéré** : `[LINEA]_[PRODOTTO]_[VARIANTE]_[GG_MM_AAAA]`

    Un nom clair facilite la gestion lorsque vous avez plusieurs recettes différentes.
    :::

* - **4**
  - Cliquer sur **Save Recipe** pour enregistrer la recette
````

```{warning}
**Sauvegarde des recettes**

Après avoir créé et configuré une recette :
- Utiliser la fonction de sauvegarde du logiciel ([Backup Management](backup))
- Exporter périodiquement les recettes sur un support externe
- Documenter les paramètres critiques sur papier/support numérique

Une recette bien configurée représente des heures de travail. Une protection adéquate permet d'éviter la perte de données.
```