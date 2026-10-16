# Boîtier Orange Pi 4 Pro — fichiers FreeCAD

Première version (v1) construite à partir de `CAHIER_DES_CHARGES.md` (v0.47).

| Fichier | Rôle |
|---|---|
| `boitier_opi4pro.FCMacro` | Macro qui construit tout. Les cotes sont des paramètres en tête de fichier. |
| `boitier_opi4pro.FCStd` | Document FreeCAD produit par la macro : socle, capot, maquette de la carte. |
| `socle.stl`, `capot.stl` | Pièces à imprimer. |
| `outils/verifier.py` | Contrôle après la macro : solides valides, aucune collision avec la maquette (`freecadcmd outils/verifier.py`). |

Relancer la macro (FreeCAD > Macro > Macros… > Exécuter) régénère les trois autres fichiers à côté d'elle. Testée en ligne de commande avec FreeCAD 1.1.3.

## Ce que fait la v1

- **Vis du SSD** : le SSD est vissé sur le support de la carte ; la vis dépasse de 9 mm sous la carte, plus bas que le plancher du socle (7,5 mm). Un logement de Ø 8 mm, 10 mm sous la carte, est creusé dans le fond à cet endroit (`SSD_VIS_*`).
- **Socle** : la carte s'encastre dedans (jeu 0,5 mm) et se visse sur 4 plots. Les plots laissent 3 mm d'air sous le SSD. Ouvertures pour les prises, la microSD avec un creux pour la saisir, et le micro. Un poussoir à languette souple pour le bouton POWER. Un double fond avec un trou de serrure pour accrocher le boîtier à une vis.
- **Côté HDMI** : ouvertures à la forme des prises : USB-C oblongue (bouts arrondis), HDMI rectangle aux coins du bas coupés, jack audio rond ; lamages autour pour les fiches.
- **Côté USB / RJ45** : une fenêtre par prise, séparées par des pattes (2,5 mm entre les deux USB, 3 mm entre USB et RJ45).
- **Capot** : ventilateur 40 × 10 mm vissé sous le dessus (entraxe 32 mm, trous légèrement oblongs), grille d'entrée d'air au-dessus, ouvertures des prises.
- **Circulation d'air** : le ventilateur souffle vers l'intérieur, sur les dissipateurs. Un couloir de 3 mm le long du côté 40 broches fait descendre l'air sous la carte. L'air passe sur le SSD et sort par des fentes basses côté HDMI et côté USB.
- **Options** (en tête de macro) : `OREILLES = True` ajoute les pattes de fixation murale, et `FENTES_HAUTES = True` ajoute des sorties d'air au-dessus de la carte, pour comparer pendant les essais.

Dimensions hors tout : 105 × 74 × 45 mm, bossages d'angle compris.

## Visserie

| Usage | Vis |
|---|---|
| Carte sur le socle | 4 × M2,5 × 8, auto-taraudeuses dans le PETG |
| Capot sur le socle, vissé par dessous | 4 × M3 × 25 |
| Ventilateur sous le capot | 4 × M3 (longueur selon le ventilateur) + écrous |
| Mur | 1 vis Ø 3,5 à 4 mm, tête de 8 mm maximum |

## Impression (PETG)

- Socle à plat, fond sur le plateau. Capot retourné, dessus sur le plateau. Aucun support n'est nécessaire.
- Le PETG fait moins bien les ponts que le PLA : le plus long (≈ 14 mm, au-dessus de l'ouverture microSD) peut légèrement s'affaisser sans gêner.
- La languette du bouton POWER fait 1,2 mm d'épaisseur (`LANGUETTE_EP`). Si elle est trop raide, la réduire ; si elle casse, l'augmenter.

### Réglages Cura de départ (Ender 5, PETG)

Valeurs courantes à ajuster : les plages indiquées sur la bobine font foi. Faire d'abord un petit essai (cube de 20 mm ou tour de température). Partir du profil « Generic PETG » de Cura.

**Avant d'imprimer**
- Sécher le filament s'il file, crépite ou fait des bulles : 4 à 6 h à 65 °C.
- Imprimante sous tente : le PETG n'a pas besoin d'enceinte chaude. Laisser la tente entrouverte pour rester sous 35-40 °C, sinon la tête d'origine de l'Ender 5 risque de se boucher (« heat creep »).

| Réglage | Valeur |
|---|---|
| Buse | 235 °C (230-245) ; 240 °C pour la 1re couche. Tête d'origine à tube PTFE : ne pas dépasser 240 °C |
| Plateau | 80 °C (75-85) |
| 1re couche | ne pas l'écraser : offset Z remonté de 0,05 à 0,1 mm par rapport au PLA |
| Adhérence | verre ou PEI lisse : fine couche de colle en bâton (anti-adhérent, le PETG peut arracher le verre) ; PEI texturé : rien. Pas de bordure nécessaire |
| Vitesse | 40-50 mm/s ; 1re couche 20 mm/s |
| Ventilateur de pièce | 0 % sur les 2-3 premières couches, puis 30-50 % ; ponts 100 % |
| Temps minimal par couche | 10 s |
| Rétraction (extrudeur déporté, Bowden) | 5-6 mm à 30-40 mm/s ; extrudeur direct (Ender 5 S1) : 0,8-1,5 mm |
| Z-hop | désactivé (augmente les fils) |
| Combing | « Pas dans la surface extérieure » |
| Hauteur de couche | 0,2 mm |
| Parois | 3 (1,2 mm), pour la tenue des vis |
| Dessus / dessous | 5 couches |
| Remplissage | 20-25 %, gyroïde |
| Supports | aucun |
| Débit | 95-100 % |

**Si ça file** : baisser la buse de 5 °C, augmenter la rétraction de 0,5 mm, vérifier que le filament est sec.

## Variables d'ajustement

Toutes les variables sont **en tête du fichier `boitier_opi4pro.FCMacro`**, chacune avec son commentaire. Ce n'est pas un fichier FreeCAD « paramétrique » : le `.FCStd` et les STL ne contiennent que les formes, les paramètres sont uniquement dans la macro.

Pour les modifier :
- dans FreeCAD : Macro > Macros…, sélectionner `boitier_opi4pro.FCMacro`, bouton **Éditer** ; modifier, enregistrer, puis **Exécuter** ;
- ou avec n'importe quel éditeur de texte, puis relancer la macro.

### Réglages d'essai (les plus utiles)

| Variable | Valeur | Effet |
|---|---|---|
| `FENTES_BASSES` | `True` | Sorties d'air sous la carte (côtés HDMI et USB) : l'air passe sur le SSD |
| `FENTES_HAUTES` | `False` | Sorties d'air au-dessus de la carte (petit côté sans USB), à comparer aux essais |
| `TROU_SERRURE` | `True` | Accroche murale sur une vis (double fond) |
| `OREILLES` | `False` | Pattes de fixation murale de chaque côté |
| `JEU` | 0,5 | Jeu entre la carte et les parois (augmenter si la carte force) |
| `PAROI` | 2,0 | Épaisseur des parois |
| `PLOT_AVANT_TROU` | 2,2 | Avant-trou des vis M2,5 de la carte |
| `LANGUETTE_EP` | 1,2 | Épaisseur de la languette du bouton POWER (plus fine = plus souple) |
| `VIS_M3_AVANT_TROU` | 2,6 | Avant-trou des vis M3 du capot |
| `FAN_X`, `FAN_Y` | 50 ; 27,85 | Position du ventilateur au-dessus de la carte |
| `FAN_JEU_USB` | 1,0 | Jeu entre le sommet des prises USB et le ventilateur |
| `JEU_AIR`, `COULOIR_X` | 3 ; 12-62 | Largeur et longueur du couloir d'air qui descend vers le SSD |
| `AIR_SOUS_SSD` | 3,0 | Espace d'air sous le SSD |
| `SSD_VIS_SOUS`, `SSD_VIS_TETE_D`, `SSD_VIS_JEU` | 9 ; 6 ; 1 | Dépassement de la vis du SSD sous la carte, diamètre de sa tête, jeu du logement creusé dans le fond |
| `MINI_PAROI` | 0,8 | Épaisseur minimale laissée par les lamages des fiches |
| `JEU_OUVERTURE` | 0,3 | Jeu autour des prises USB-C, HDMI et audio |
| `HDMI_CHANFREIN` | 1,5 | Taille des coins coupés de l'ouverture HDMI |
| `HDMI_CHANFREIN_EN_BAS` | `True` | Coins coupés côté carte ; `False` pour les mettre en haut si la prise est montée dans l'autre sens |
| `PRISES_Y` (dernier champ) | `oblong`, `chanfrein`, `rond` | Forme de chaque ouverture ; `rect` pour revenir au rectangle |
| `JEU_PRISE` | 0,3 | Jeu autour de chaque prise USB / RJ45 dans sa fenêtre (pattes entre les prises) |

### Cotes de la carte (mesurées)

`CARTE_*`, `TROUS`, `SSD_*`, `USB_*`, `PRISES_Y` (positions, hauteurs, dépassements et taille des fiches pour les lamages), `SD_*`, `PWR_*`, `MIC_*`. Elles reprennent le cahier des charges et ne devraient changer qu'après une nouvelle mesure.

### Boîtier et visserie

`FOND_EXT`, `FOND_CAVITE`, `FOND_INT` (double fond), `SPLIT` (plan de joint socle/capot), `PLAFOND`, `PLOT_D`, `BOSSAGE_D`, `VIS_M3_*`, `SERRURE_*`, `OREILLE_TROU`, `FAN*`.

## Cotes supposées, à mesurer

| Paramètre | Valeur supposée | Quoi mesurer |
|---|---|---|
| `SSD_VIS_TETE_D` | 6 mm | Diamètre de la tête de la vis du SSD (le logement fait ce diamètre + 2 mm) |
| `SSD_SUPPORT_R` | 2,5 mm | Rayon du support de vis sur la carte : sert à placer le centre de la vis à partir des cotes du point le plus éloigné |
