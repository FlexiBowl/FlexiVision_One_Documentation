(troubleshooting_calib_cam)=
# **Calibration Caméra**

## **Pattern non détecté**

```{warning}
**Erreur: "Unable to detect calibration pattern"**

Cause: Le logiciel ne parvient pas à identifier le pattern de la grille.

**Solutions**:
- Augmenter le contraste (régler exposition ou éclairage)
- Vérifier que toute la grille est visible dans l'image
- Améliorer la mise au point
- Nettoyer la surface de la grille (poussière ou empreintes peuvent interférer)
- Vérifier que la grille est la bonne (carrés, pas cercles ou autres patterns)
```

## **Calibration toujours "Bad" ou "Acceptable"**

```{warning}
**Qualité de calibration insuffisante**

Si, malgré les réglages, la calibration reste sous "Excellent":

1. Vérifier la distance de travail caméra-FlexiBowl (elle doit être celle calculée)
2. Contrôler que la caméra est parallèle par rapport au plan du FlexiBowl (elle doit être parfaitement horizontale)
3. S'assurer que la caméra est stable (aucune vibration pendant l'acquisition)
4. Vérifier que l'objectif est complètement vissé 

Si le problème persiste, il peut y avoir un problème mécanique dans le montage. Consulter [Installation Mécanique]009_Installazione_Meccanica.md) pour révision.
```

## **Erreurs après changement d'éclairage**

```{tip}
**Re-calibration après changement backlight/toplight**

Si l'on passe de backlight à toplight (ou inversement):

1. La calibration géométrique reste valide (il n'est pas nécessaire de la refaire)
2. Il suffit de régler l'exposition de la caméra pour le nouveau type d'éclairage
3. Acquérir une image de test pour vérifier que le pattern reste bien visible

En général, il est conseillé de décider dès le début du type d'éclairage à utiliser et de conserver cette configuration.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problème
  - Causes Possibles
  - Solutions
* - **Calibration échoue (erreur logiciel)**
  - • Grille de calibration non détectée correctement
    
    • Éclairage insuffisant/excessif
    
    • Grille calibration endommagée ou sale
    
  - • Positionner le target plat et bien visible
    
    • Régler l'exposition caméra pour bien visualiser le target
    
    • Utiliser une grille calibration propre et intacte
    
* - **Erreur de calibration trop élevée**
  - • Caméra non parfaitement orthogonale à la surface
    
    • Grille calibration non plane
    
    • Distorsion optique excessive
    
  - • Vérifier l'orthogonalité caméra avec un niveau (tolérance ±1°)
    
    • Positionner le target sur une surface rigide et plane
    
    • Vérifier la qualité optique de l'objectif, nettoyer ou remplacer
    
* - **Coordonnées réelles ne correspondent pas à celles mesurées**
  - • Facteur d'échelle erroné (Tile Size erroné)
    
    • Caméra déplacée après calibration
    
  - • Répéter la calibration complète
    
    • Fixer fermement la caméra pour éviter les déplacements
    
    • Vérifier les dimensions du target de calibration selon la documentation
* - **Calibration valide uniquement au centre image**
  - • Distorsion optique périphérique
    
    • Calibration avec trop peu de points
  - • Utiliser un objectif de qualité supérieure à faible distorsion
    
    • Vérifier que la distance de travail est correcte
```



