# Boîtier Orange Pi 4 Pro — fichiers FreeCAD

Première version (v1) construite à partir de `CAHIER_DES_CHARGES.md` (v0.39).

| Fichier | Rôle |
|---|---|
| `boitier_opi4pro.FCMacro` | Macro qui construit tout. Les cotes sont des paramètres en tête de fichier. |
| `boitier_opi4pro.FCStd` | Document FreeCAD produit par la macro : socle, capot, maquette de la carte. |
| `socle.stl`, `capot.stl` | Pièces à imprimer. |

Relancer la macro (FreeCAD > Macro > Macros… > Exécuter) régénère les trois autres fichiers à côté d'elle. Testée en ligne de commande avec FreeCAD 1.1.3.

## Ce que fait la v1

- **Socle** : la carte s'encastre dedans (jeu 0,5 mm) et se visse sur 4 plots. Les plots laissent 3 mm d'air sous le SSD. Ouvertures pour les prises, la microSD avec un creux pour la saisir, et le micro. Un poussoir à languette souple pour le bouton POWER. Un double fond avec un trou de serrure pour accrocher le boîtier à une vis.
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

## Cotes supposées, à mesurer

| Paramètre | Valeur supposée | Quoi mesurer |
|---|---|---|
| `USB_Y0` | 2,25 mm | Distance entre le bord 40 broches de la carte et le bord extérieur de la première prise USB |
| `PWR_Z` | 1 mm au-dessus de la carte | Hauteur du centre du bouton POWER |
| `TROUS` | centres à 7,5 mm du petit côté sans USB | Confirmer que les 6 mm « dans la longueur » partent bien du petit côté sans USB |
| SSD (maquette) | x 2-82, y 20-42 | Emplacement réel du SSD (sert seulement au contrôle d'encombrement) |
