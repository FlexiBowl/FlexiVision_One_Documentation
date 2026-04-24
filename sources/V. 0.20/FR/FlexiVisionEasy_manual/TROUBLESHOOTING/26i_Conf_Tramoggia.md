(troubleshooting_conf_tramoggia)=
# **Configuration Hopper** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes Possibles
  - Solutions

* - **Zone de contrôle non définissable**
  - • Image non acquise
    
    • Section incorrecte
  - • Acquérir une image de test
    
    • Accéder via Config Hopper X


* - **AUTO ne calcule pas correctement Mean et Std Dev**
  - • CAPTURE non exécutés
    
    • Ordre CAPTURE inversé
    
    • Zone de contrôle trop petite
  - • Exécuter CAPTURE vide puis CAPTURE plein
    
    • Répéter dans l'ordre correct
    
    • Agrandir la zone de contrôle
* - **TEST toujours VERT (hopper ne s'active jamais)**
  - • Seuil trop permissif
    
    • CAPTURE plein avec trop de composants
    
    • Mean calculé incorrect
  - • Répéter CAPTURE plein avec le nombre minimal correct
    
    • Vérifier qu'AUTO recalcule correctement
    
    • Régler manuellement le seuil si nécessaire
* - **TEST toujours ROUGE (hopper s'active toujours)**
  - • Seuil trop restrictif
    
    • CAPTURE vide avec composants présents
    
  - • Répéter CAPTURE vide avec une zone complètement propre
    
    • Répéter AUTO

* - **Temps de vibration ne produit pas l'effet souhaité**
  - • Valeur trop basse
    
    • Valeur trop élevée 
    
    • Niveau de cuve hopper variable
  - • Commencer avec 500ms
    
    • Augmenter de ±100ms pour régler le flux
    
    • **CRITIQUE**: Maintenir une charge constante dans la cuve

* - **Hopper décharge aux mauvais moments**
  - • Steps non correct

    • Matériel du Contrôleur Hopper non configuré correctement 

  - • Recalculer Steps

    • Contrôler les spécifications de configuration dans le [manuel dédié au Hopper]() 
```

