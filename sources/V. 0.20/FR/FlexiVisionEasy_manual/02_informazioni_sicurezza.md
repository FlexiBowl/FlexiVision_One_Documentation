# **Informations de Sécurité**

Les instructions de sécurité, précautions générales et règles relatives à la manutention et à l'environnement opérationnel suivantes doivent être scrupuleusement respectées afin de garantir la sécurité du personnel, l'intégrité du produit et le bon fonctionnement de l'installation.

```{warning}
**Responsabilité de l'utilisateur**

Le respect de toutes les règles de sécurité indiquées dans cette section est obligatoire et relève de la responsabilité de l'utilisateur final. Le non-respect peut provoquer des dommages aux personnes, aux équipements ou compromettre le fonctionnement du système.
```

---

## Sécurité opérationnelle

### Intégration avec des systèmes robotisés

#### **Exigences de sécurité de la cellule**

```{warning}
FlexiVision One fonctionne en étroite connexion avec des systèmes robotisés tiers. L'utilisateur doit garantir que la zone de travail est équipée de toutes les mesures de sécurité nécessaires imposées par les réglementations pertinentes
```
#### **Attention pendant l'exploitation**

```{warning}

Pendant le fonctionnement du système, tenir toujours compte de:

- Encombrements physiques du robot et du FlexiBowl
- Trajectoires et vitesses des mouvements robotiques
- Situations imprévues possibles (chute de pièces, erreurs de prise)
- Zones de danger pendant les phases de vibration du FlexiBowl
```

### Précautions générales avant les interventions

#### **Déconnexion des alimentations**

```{warning}
Avant d'effectuer toute intervention de maintenance, modification ou inspection sur le système, toujours s'assurer que:

- Toutes les sources d'alimentation électrique sont déconnectées (VisionController, FlexiBowl, Caméra, Illuminateur)
- L'alimentation pneumatique est déchargée et déconnectée (si présente)
- Les câbles de connexion sont physiquement débranchés
- Le robot est en mode sécurité ou complètement éteint
```
#### **Procédures de sécurité**

```{warning}

Ne pas se fier exclusivement aux interrupteurs: utiliser les procédures de lockout/tagout (LOTO) lorsqu'elles sont disponibles.
```

### Modifications et altérations

#### **Interdiction des modifications non autorisées**

```{warning}
Ne jamais modifier le produit ou ses composants sans autorisation écrite expresse d'ARS S.r.l.
```
#### **Conséquences des modifications**

```{warning}
Les modifications non autorisées peuvent:

- Provoquer des dysfonctionnements du système
- Invalider la garantie
- Créer des risques de blessures, de chocs électriques ou d'incendies
- Compromettre les certifications de sécurité du produit
```

---

## Conditions environnementales et protection

### Protection contre les liquides

#### **Risque de contact avec des liquides**

```{warning}

Ne pas utiliser le produit dans des environnements où le VisionController, la caméra ou d'autres composants électroniques peuvent entrer en contact avec:

- Gouttes d'eau ou éclaboussures
- Huiles, lubrifiants ou autres liquides industriels
- Condensation ou humidité excessive
- Poussières conductrices
```
#### **Solutions pour environnements critiques**

```{note}

Si le système doit fonctionner dans des environnements avec présence de liquides, prévoir des protections adaptées (boîtiers IP65 ou supérieurs) et consulter le service technique ARS pour des solutions personnalisées.
```

### Températures de fonctionnement

#### **Surfaces chaudes - Températures maximales**

```{warning}
Dans des conditions d'utilisation intensive ou dans des environnements chauds, certains composants du système peuvent atteindre des températures élevées:

- VisionController: jusqu'à 50°C sur les surfaces externes
- Illuminateur LED: jusqu'à 40°C sur la surface frontale
- Caméra industrielle: jusqu'à 50°C sur le corps métallique
```
#### **Responsabilité du client**

```{warning}
Il est de la responsabilité du client de:

- Documenter les risques thermiques dans sa propre évaluation des risques
- Former le personnel aux procédures permettant d'éviter les contacts accidentels
- Prévoir une signalisation d'avertissement lorsque cela est nécessaire
- Garantir une ventilation adéquate des composants
```

### Conditions environnementales pour installation et stockage

#### **Exigences environnementales - Tableau de référence**

```{note}

Pour garantir durée de vie et fiabilité, le VisionController et la caméra doivent être utilisés et conservés dans les conditions suivantes:

| Paramètre | Conditions opérationnelles | Conditions de stockage |
|-----------|---------------------|--------------------------|
| **Température** | +1°C ÷ +50°C | -20°C ÷ +65°C |
| **Humidité relative** | <90% (sans condensation) | <90% (sans condensation) |


```
#### **Précautions environnementales supplémentaires**

```{note}
Pour préserver l'intégrité des composants:

- Éviter l'exposition directe à la lumière solaire
- Protéger contre les vibrations excessives pendant le stockage
- Maintenir dans un environnement sec et exempt de poussières agressives
- La caméra est sensible aux chocs mécaniques: manipuler avec soin
```

---

## Transport et manutention

### Réception et inspection

#### **Inspection à l'arrivée**

```{note}
À la réception du produit, avant de signer le bon de livraison:

1. **Inspection externe de l'emballage**: Vérifier l'intégrité de la boîte et de l'emballage extérieur. Contrôler la présence d'éventuelles traces de chocs, d'écrasements ou d'humidité.

2. **Vérification du contenu**: Comparer le contenu avec le bon de livraison. Vérifier la présence de tous les composants commandés.
```

#### **En cas de dommages ou divergences**

```{note}
Si des problèmes sont constatés:

- NE PAS signer le reçu comme "conforme"
- Noter les dommages sur le document de transport
- Photographier les éventuels dommages visibles
- Contacter immédiatement le service d'assistance ARS: 
    [service@arsautomation.com](mailto:service@arsautomation.com) 
    [us.service@arsautomation.com](mailto:us.service@arsautomation.com) si le contact se fait depuis l'Amérique
```

### Manutention et stockage
Pour éviter les dommages pendant le transport et le stockage:

#### **Transport**

```{tip}
**Pendant le transport:**
- Toujours manutentionner l'emballage en position verticale (respecter les flèches "HAUT" sur l'emballage)
- Ne pas faire tomber ni heurter le colis
- Utiliser des chariots ou transpalettes adaptés au poids
- Éviter les variations thermiques soudaines
```
#### **Stockage**

```{tip}
**Pendant le stockage:**
- Conserver dans un lieu sec et couvert
- Ne pas superposer d'autres charges sur l'emballage
- Ne pas monter ou s'appuyer sur l'emballage
- Respecter les conditions environnementales indiquées dans le tableau précédent
```
#### **Déballage**

```{tip}
**Pendant le déballage:**
- Ouvrir avec soin afin de ne pas endommager les composants internes
- Conserver l'emballage d'origine pour d'éventuels retours ou transports futurs
- Vérifier la présence de tous les accessoires et de la documentation
```

---

## Élimination et fin de vie

### **Élimination responsable**

```{warning}

Lorsque le produit atteint la fin de son cycle de vie, il doit être éliminé conformément aux réglementations en vigueur relatives aux déchets d'équipements électriques et électroniques (RAEE/WEEE).
```
### **Composants soumis à élimination spéciale**

```{note}
**Composants soumis à élimination spéciale:**
- Cartes électroniques (VisionController): RAEE catégorie 6
- Caméra industrielle: RAEE catégorie 6
- Illuminateurs LED: RAEE catégorie 5
- Câbles et connecteurs: élimination avec les matériaux électriques
```
---


