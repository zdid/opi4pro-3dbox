# Boîtier Orange Pi 4 Pro — fichiers FreeCAD

Première version (v1) construite à partir de `CAHIER_DES_CHARGES.md` (v0.47).

| Fichier | Rôle |
|---|---|
| `boitier_opi4pro.FCMacro` | Macro qui construit tout. Les cotes sont des paramètres en tête de fichier. |
| `boitier_opi4pro.FCStd` | Document FreeCAD produit par la macro : socle, capot, maquette de la carte. |
| `socle.stl`, `capot.stl` | Pièces à imprimer. |

Relancer la macro (FreeCAD > Macro > Macros… > Exécuter) régénère les trois autres fichiers à côté d'elle. Testée en ligne de commande avec FreeCAD 1.1.3.

## Ce que fait la v1

- **Cale du SSD** : un plot conique (Ø 8 à la base, Ø 6 au contact, surface de la tête de vis) sous le bout du SSD, au droit du support de vis M.2 (bord du contact à 87,6 mm du petit côté sans USB et à 33,4 mm du côté 40 broches), le maintient quand il n'est pas vissé (`SSD_CALE`). Elle a un léger creux (0,5 mm) au droit du téton du support (Ø 3,1), qui arrive au ras du SSD. `SSD_CALE_DECALAGE` permet de la déplacer vers l'intérieur du SSD en cale pleine.
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
| Carte sur le socle | 4 × M2,5 × 8, auto-taraudeuses dans le PLA |
| Capot sur le socle, vissé par dessous | 4 × M3 × 25 |
| Ventilateur sous le capot | 4 × M3 (longueur selon le ventilateur) + écrous |
| Mur | 1 vis Ø 3,5 à 4 mm, tête de 8 mm maximum |

## Impression (PLA)

- Socle à plat, fond sur le plateau. Capot retourné, dessus sur le plateau. Aucun support n'est nécessaire.
- La languette du bouton POWER fait 1,2 mm d'épaisseur. Si elle est trop raide ou cassante, réduire son épaisseur dans la macro.

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
| `SSD_CALE` | `True` | Plot qui cale le bout du SSD quand il n'est pas vissé |
| `SSD_EP_PCB` | 0,8 | Hauteur de la cale : augmenter si elle serre trop, diminuer si elle ne touche pas |
| `SSD_CALE_DECALAGE` | 0 | Déplace la cale vers l'intérieur du SSD ; à partir de 4,5 elle devient pleine, sans logement |
| `SSD_TETON_PROF` | 0,5 | Profondeur du creux au droit du téton du support |
| `JEU` | 0,5 | Jeu entre la carte et les parois (augmenter si la carte force) |
| `PAROI` | 2,0 | Épaisseur des parois |
| `PLOT_AVANT_TROU` | 2,2 | Avant-trou des vis M2,5 de la carte |
| `VIS_M3_AVANT_TROU` | 2,6 | Avant-trou des vis M3 du capot |
| `FAN_X`, `FAN_Y` | 50 ; 27,85 | Position du ventilateur au-dessus de la carte |
| `FAN_JEU_USB` | 1,0 | Jeu entre le sommet des prises USB et le ventilateur |
| `JEU_AIR`, `COULOIR_X` | 3 ; 12-62 | Largeur et longueur du couloir d'air qui descend vers le SSD |
| `AIR_SOUS_SSD` | 3,0 | Espace d'air sous le SSD |
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
| `SSD_EP_PCB` | 0,8 mm (non mesurable, valeur courante) | Si la cale serre trop ou ne touche pas le SSD, ajuster cette valeur |
