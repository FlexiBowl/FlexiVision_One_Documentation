(troubleshooting_fb_wizard)=
# **FlexiBowl Wizard**

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes Possibles
  - Solutions
* - **Wizard ne démarre pas**
  - • Recette non chargée
    
    • FlexiBowl non connecté
    
    • Setup initial non terminé
  - • Charger ou créer d'abord une recette
    
    • Vérifier connexion FlexiBowl
    
    • Compléter configuration de base système

* - **Sens de rotation configuré ne correspond pas**
  - • Erreur de sélection CW/CCW
    
  - • Vérifier visuellement le sens de rotation réel
    
    • Corriger la sélection dans le Wizard
    
* - **Test Air-blow ne fonctionne pas**
  - • Air comprimé non connecté
    
    • Pression insuffisante
    
    • Module non présent physiquement
  - • Vérifier connexion air comprimé
    
    • Augmenter pression à 5-6 bar
    
    • Sélectionner "FlexiBowl NOT equipped" si le module est absent
* - **Test Flip non perceptible**
  - • Air comprimé non connecté/insuffisant
    
    • Régulateur de pression fermé
    
    • Fuites circuit pneumatique
  - • Vérifier air comprimé connecté
    
    • Ouvrir régulateur sur panneau de contrôle
    
    • Vérifier pression 5-6 bar
    
    • Inspecter les raccords pour fuites
* - **Paramètres calculés non optimaux**
  - • Caractérisation composant erronée
    
    • Wizard utilise valeurs génériques
  - • Revoir géométrie et comportement sélectionnés
    
    • Accepter paramètres Wizard comme point de départ
    
    • Affiner manuellement dans dashboard récapitulatif

* - **Composants bougent pendant acquisition**
  - • Vitesse/accélération trop élevées
    
    • Pauses stabilisation absentes
    
    • Surface grip non adaptée
  - • Diminuer Speed et Accel
    
    • Insérer pauses 200-500ms
    
    • Remplacer surface grip par une plus adhérente
* - **Soufflage non efficace**
  - • Pression air insuffisante/excessive
    
    • Buses obstruées
  - • Vérifier pression 5-6 bar
    
    • Nettoyer buses air-blow

* - **Modifications paramètres ne s'appliquent pas**
  - • "Synchronize Parameters" non appuyé
    
    • Recette non enregistrée
  - • **TOUJOURS** cliquer sur Synchronize Parameters après modifications
    
    • Enregistrer recette pour rendre les modifications permanentes
* - **Turn FLB ne fonctionne pas pendant setup**
  - • FlexiBowl non connecté
    
    • Commande non configurée
    
    • FlexiBowl en erreur
  - • Vérifier connexion FlexiBowl
    
    • Contrôler configuration FlexiBowl Setup
    
    • Vérifier LED READY FlexiBowl
```
