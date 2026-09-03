(troubleshooting_conf_tramoggia)=
# **Configuration de la trémie** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes possibles
  - Solutions

* - **Zone de contrôle non définissable**
  - • Image non acquise
    
    • Mauvaise section
  - • Acquérir l'image test
    
    • Accès via Config Hopper X


* - **AUTO ne calcule pas correctement Mean et Std Dev**
  - • CAPTURE pas exécutée
    
    • Ordre CAPTURE inversé
    
    • Zone de contrôle trop petite
  - • Exécuter CAPTURE vide puis CAPTURE plein
    
    • Répéter dans le bon ordre
    
    • Agrandir la zone de contrôle
* - **TEST toujours VERT (la trémie ne s'active jamais)**
  - • Seuil trop permissif
    
    • CAPTURE pleine avec trop de composants
    
    • Moyenne calculée erronée
  - • Répéter la CAPTURE complète avec le nombre minimum correct
    
    • Vérifier qu'AUTO recalcule correctement
    
    • Ajuster le seuil manuellement si nécessaire
* - **TEST toujours ROUGE (trémie toujours activée)**
  - • Seuil trop restrictif
    
    • CAPTURE vide avec composants présents
    
  - • Répéter l'opération CAPTURE vide avec une zone complètement propre
    
    • Répéter AUTO

* - **Time vibration ne produit pas l'effet désiré**
  - • Valeur trop faible
    
    • Valeur trop élevée 
    
    • Niveau variable de la cuve de la trémie
  - • Démarrer avec 500 ms
    
    • Augmenter ±100 ms pour ajuster le débit
    
    • **CRITIQUE** : Maintenir une charge constante dans la cuve

* - **Trémie déchargée au mauvais moment**
  - • Paramètre « Steps » incorrect

    • Matériel du contrôleur de trémie mal configuré 

  - • Recalculer les Steps

    • Vérifier les spécifications de configuration dans le [manuel de la trémie]() 
```

