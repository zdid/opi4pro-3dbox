# Cahier des charges — boîtier pour Orange Pi 4 Pro

Version : 0.44 (brouillon) — 2026-10-05

## 1. Objet

Boîtier destiné à contenir une carte **Orange Pi 4 Pro (A733)** avec refroidissement actif par ventilateur, un SSD fixé à l'arrière de la carte et une antenne remplaçable par une antenne déportée.

## 2. Données de la carte (source : manuel Orange Pi 4 Pro v1.4)

| Élément | Valeur |
|---|---|
| Dimensions du circuit imprimé | **89 mm × 55,7 mm** (mesuré ; le manuel indique 89 × 56) |
| Longueur avec les prises USB et RJ45 | **91,8 mm** (les prises dépassent de la carte de 2,8 mm) |
| Fixations | 4 trous de Ø 3,0 mm. Mesuré entre les bords extérieurs des trous : **52 mm en largeur** et **61 mm en longueur**, soit des entraxes de **49 mm × 58 mm** (même gabarit que le Raspberry Pi). Distance du bord extérieur du trou au bord le plus proche de la carte : **6 mm en longueur** et **1,75 mm en largeur**, soit des centres à **7,5 mm** et **3,25 mm** de ces bords. Les 6 mm sont pris depuis le petit côté sans USB (confirmé). Côtés opposés (calculés, à vérifier) : 22 mm en longueur (89 − 6 − 61) et 1,95 mm en largeur (55,7 − 1,75 − 52). |
| SSD | Emplacement **M.2 M-Key 2280, PCIe NVMe**, sur la **face arrière** (écrou de fixation « M.2 2280 » côté opposé au connecteur) |
| Autres éléments de la face arrière | Fente **microSD**, interface eMMC, connecteur MIPI CSI 4 voies |
| Face avant | SoC Allwinner A733, mémoire LPDDR5, module Wi-Fi 6 + BT 5.4, PMU, puce Ethernet, 40 broches |
| Antenne | « Antenna pedestal » (embase) à l'angle de la carte, près du module Wi-Fi et de l'en-tête 40 broches. Type exact du connecteur non précisé par le manuel. |
| Alimentation | USB-C 5 V / 3 A (sans PD). La carte n'offre que du **5 V** et du **3,3 V** (broches 2 et 4 pour le 5 V sur le 40 broches) : le ventilateur est donc en 5 V, ou alimenté en externe s'il est d'une autre tension. |
| Connecteurs | USB 2.0 ×3, USB 3.0 ×1 et Ethernet sur un petit côté ; HDMI, USB-C, haut-parleur et jack audio sur un grand côté ; MIPI DSI, MIPI CSI 2 voies, boutons POWER, RESET et BOOT sur la face avant |
| Commande ventilateur | Broches PWM du 40 broches : 7, 29, 32, 33, 35, 36, 37, 38 (signaux en 3,3 V). Le PWM est **désactivé par défaut** sous Linux et doit être activé dans la configuration de la carte. |

### Mesures relevées sur la carte (utilisateur, 2026-10-05)

| Élément | Valeur |
|---|---|
| Longueur de la carte avec le dépassement des prises USB et RJ45 | 91,8 mm (circuit imprimé : 89 mm) |
| Connecteurs USB : hauteur au-dessus de la carte | 15,7 mm |
| Connecteurs USB : rebord courbé | dépasse de 0,8 mm sur le dessus et sur les côtés |
| Connecteurs USB : largeur du corps de la prise | 13,1 mm (14,7 mm avec les rebords de 0,8 mm de chaque côté) |
| Prise RJ45 : hauteur au-dessus de la carte | 13,8 mm |
| Prise RJ45 : largeur | 15,9 mm |
| Prise RJ45 : rebord | aucun |
| Distance extérieur de la prise USB à extérieur de la prise RJ45 | **51,2 mm** (mesure de référence, la plus sûre) |
| Distance du grand côté du 40 broches à l'extérieur de la 1re prise USB | 2,5 mm |
| SSD : dépassement sous la carte | 4,5 mm (du dessous du circuit imprimé de l'Orange Pi au dessous du SSD) |
| SSD : dimensions | 22 mm de large, 84 mm de long avec son connecteur |
| SSD : position en largeur (décentré) | bord le plus éloigné à 35,2 mm du grand côté HDMI, soit de 13,2 à 35,2 mm de ce côté |
| SSD : support de vis (écrou M.2) | support à épaulement : le SSD repose sur l'épaulement à 3,9 mm sous la carte, le téton (Ø 3,1 environ) passe dans l'encoche du SSD et dépasse dessous ; point le plus éloigné du support à **87,6 mm** du petit côté sans USB et à **33,4 mm** du grand côté du 40 broches |
| Espace entre les deux prises USB | 4,7 mm |
| Espace entre prise USB et RJ45 | 4,6 mm |
| Prise HDMI : largeur / hauteur carte incluse | 14,8 mm / 7,3 mm |
| Prise USB-C (alimentation) : largeur / hauteur carte incluse | 8,8 mm / 5 mm |
| Prise audio (jack 3,5 mm) : largeur / hauteur carte incluse | 6 mm / 6,5 mm |

Épaisseur du circuit imprimé : **1,3 mm** (mesurée). Les hauteurs HDMI, USB-C et audio ci-dessus incluent cette épaisseur ; ramenées au-dessus de la carte : HDMI **6,0 mm**, audio **5,2 mm**, USB-C **3,7 mm**.

Position des prises du grand côté (HDMI, USB-C, audio), mesurée depuis le **petit côté sans USB** jusqu'au point le plus éloigné de chaque prise ; le début se déduit de la largeur :

| Prise | De | À | Largeur |
|---|---|---|---|
| USB-C | 11,7 mm | 20,5 mm | 8,8 mm |
| HDMI | 27,8 mm | 42,6 mm | 14,8 mm |
| Audio | 54,2 mm | 60,2 mm | 6 mm |

Dépassement du bord de la carte (mesuré) : USB-C **1,4 mm**, HDMI **2,6 mm**, audio **2,8 mm**.

Fente microSD : sous la carte, sur le **petit côté sans USB**. Mesurée depuis le grand côté du 40 broches : de **7,8 mm** à **18,9 mm** (largeur du support **11,1 mm**). La carte microSD insérée **dépasse de 3 mm** du bord de la carte. Hauteur du support : **2,8 mm carte incluse**, soit **1,5 mm sous la carte** (épaisseur de carte 1,3 mm).

Microphone : rond, **Ø 5,1 mm**, posé à plat sur le dessus de la carte, à l'angle formé par le **petit côté sans USB** et le **grand côté des prises USB-C, HDMI et audio**, il **dépasse de 0,3 mm** des deux bords de la carte (grand côté et petit côté, confirmé) (largeur mesurée carte + micro : 56 mm, contre 55,7 mm pour la carte seule).

Bouton POWER : sur le **petit côté sans USB**, juste à côté du microphone. Point extérieur le plus éloigné : **48,8 mm depuis le grand côté du 40 broches** (confirmé), soit 6,9 mm du grand côté des prises HDMI/USB-C. Bouton **rond, Ø 2,1 à 2,2 mm**, dépassant de **0,2 mm** du bord de la carte ; son sommet est à **4,8 mm** du dessous de la carte (centre à 3,7 mm).

Échancrure dans le bord de la carte, **sous le bouton POWER** (petit côté sans USB, près du micro) : **1,6 mm** de profondeur, **6 mm** de large, de **4,5 à 10,5 mm du grand côté des prises HDMI/USB-C** (confirmé). Le socle la laisse libre (pas de paroi qui remplisse l'échancrure ni gêne le bouton).

Empilement vertical (depuis le dessous du SSD) :

| Niveau | Cote |
|---|---|
| Dessous du SSD | 0 |
| Dessous de la carte | 4,5 mm |
| Dessus de la carte | 5,8 mm |
| Sommet des prises USB avec rebord (16,5 mm au-dessus de la carte) | 22,3 mm |
| Dessus du ventilateur de 10 mm posé au ras des prises USB | 32,3 mm |

Hauteur intérieure minimale, sans jeu ni parois : **32,3 mm**.

Hauteur maximale avec rebord : 15,7 + 0,8 = **16,5 mm** au-dessus de la carte, pour les USB.
Contrôle : 13,1 + 4,7 + 13,1 + 4,6 + 15,9 = 51,4 mm, soit 0,2 mm de plus que la mesure de référence (écart d'arrondi ou de mesure). Les découpes du boîtier se calent sur 51,2 mm, avec une tolérance d'impression.

Les dissipateurs collés ont une hauteur de **6 mm** (mesurée) et ne dépassent pas la hauteur des prises USB : le volume intérieur est dimensionné sur les prises (16,5 mm), pas sur les dissipateurs.

## 3. Exigences

### 3.1 Contenu à loger

| Réf. | Exigence |
|---|---|
| C1 | La carte Orange Pi 4 Pro est contenue entièrement dans le boîtier, avec accès à tous ses connecteurs (E/S, alimentation, GPIO si utilisés). |
| C2 | Des dissipateurs statiques sont collés sur les puces de la carte, sans dépasser la hauteur des prises USB : le ventilateur placé au-dessus se trouve au-delà de 16,5 mm. |
| C3 | Un SSD M.2 2280 NVMe est enfiché à l'arrière de la carte, sans radiateur et à quelques millimètres seulement du circuit imprimé : le boîtier ménage l'espace et le flux d'air nécessaires. |
| C4 | Le ventilateur est fixé **à l'intérieur du capot** (sous le dessus du capot), pas sur la carte. |
| C5 | La fente microSD (face arrière) reste accessible sans démonter le boîtier : ouverture dans la paroi du socle, de 7,8 à 18,9 mm depuis le grand côté du 40 broches, avec de quoi saisir la carte qui dépasse de 3 mm. |
| C6 | Les prises HDMI, USB-C et audio ne dépassent du bord de la carte que de 1,4 à 2,8 mm. Autour de chaque ouverture, la paroi est **amincie localement** (lamage côté extérieur) pour que la fiche du câble s'enfonce complètement sans buter contre la paroi. Les lamages acceptent les fiches **les plus courantes du commerce** (dimensions à fixer à la conception, avec marge). |
| C7 | Le bouton **POWER** (rond, Ø 2,1 mm) reste actionnable de l'extérieur par un **poussoir intégré au boîtier** : une languette souple imprimée dans la paroi, avec un téton qui dépasse légèrement de la carcasse et vient appuyer sur le bouton. |

### 3.1 bis Socle

| Réf. | Exigence |
|---|---|
| S1 | Le boîtier comporte un **socle** dans lequel la carte **s'encastre** (bac épousant le contour de la carte, SSD compris). |
| S2 | Le dessous des prises de la carte (USB, RJ45, HDMI, USB-C, audio) **s'encastre dans le socle** : les ouvertures des prises sont en partie taillées dans les parois du socle. |
| S3 | Le socle laisse un dégagement au niveau du **microphone** (Ø 5,1 mm), qui dépasse de 0,3 mm des bords de la carte à l'angle petit côté sans USB / grand côté des prises USB-C, HDMI et audio. |
| S4 | La carte est **vissée sur le socle** par ses 4 trous (Ø 3,0 mm, entraxes 49 × 58 mm) avec des **vis M2,5** (le M3 passe tout juste dans un trou de 3,0 mm), sur des plots assez hauts pour loger le SSD (4,5 mm sous la carte) et laisser passer l'air dessous. |
| S5 | Le **capot est vissé au socle** par des **vis M3** (solution préférée). Un assemblage par encastrement est acceptable en complément, pas en remplacement des vis. |
| S6 | Un **plot du socle cale le bout du SSD** par dessous, à l'endroit du support de vis M.2, pour le maintenir quand il n'est pas vissé. **Ø 5 mm au contact**, creusée au centre pour loger le téton du support (Ø 3,1 + jeu), son bord s'arrêtant à 87,6 mm du petit côté sans USB et à 33,4 mm du grand côté du 40 broches. |

### 3.1 ter Fixation murale

| Réf. | Exigence |
|---|---|
| M1 | **Option 1 — accroche sur une vis** : le dessous du socle comporte un trou en forme de serrure (trou de passage de la tête, puis fente) pour pendre le boîtier à une vis du mur. Il accepte des vis de **Ø 3,5 ou 4 mm** avec une tête jusqu'à **8 mm**. |
| M2 | Le socle a un **double fond** : la tête de la vis reste dans un logement fermé et ne peut toucher ni la carte, ni le SSD, ni aucun composant. |
| M3 | **Option 2 — pattes latérales** : des bras de fixation de chaque côté du socle, percés pour des vis murales. |
| M4 | Les deux options sont possibles (pattes ajoutées ou non au socle, ou deux variantes de socle). |
| M5 | Monté au mur, le dessous du socle est plaqué contre le mur : les entrées et sorties d'air ne sont **pas** placées sur la face arrière, mais sur les côtés et le capot. |

### 3.2 Refroidissement

| Réf. | Exigence |
|---|---|
| R1 | L'air circule dans tout le volume intérieur et refroidit à la fois la carte (puces avec dissipateurs) et le SSD, qui n'a pas de radiateur. |
| R2 | Le flux d'air balaie les deux faces de l'ensemble carte + SSD, pas seulement la face supérieure de la carte. |
| R3 | Les ouvertures d'entrée et de sortie sont placées pour éviter qu'une zone reste sans circulation d'air. |
| R4 | Le SSD, à quelques millimètres du circuit imprimé, n'est guère atteint par un flux venant d'au-dessus des dissipateurs : le boîtier est en deux parties (haut et bas) séparées par des ouvertures latérales le long de la carte, qui laissent passer l'air sur les deux faces. |
| R5 | Ces ouvertures sont placées en tenant compte des connecteurs : aucune fente ne gêne une fiche. |
| R6 | Le sens du flux (aspiration ou soufflage) est tranché par essai (§5). Le boîtier permet de monter le ventilateur dans les deux sens. |

### 3.2 bis Raccordement du ventilateur

Le ventilateur 40 mm, en 5 V, se branche sur le 40 broches (numérotation : broches impaires 1, 3, 5… d'un côté, paires 2, 4, 6… de l'autre) :

| Fil du ventilateur | Broche de la carte |
|---|---|
| Rouge (+5 V) | **broche 4** (5 V ; la broche 2 est aussi du 5 V) |
| Noir (masse) | **broche 6** (GND) |
| Commande de vitesse (PWM) — ventilateurs à 4 fils seulement | **broche 7** (PWM, signal 3,3 V) |
| Mesure de vitesse (tachymètre, jaune) — facultatif | non raccordé |

**Attention 3,3 V / 5 V** : les broches 1 et 17 sont en **3,3 V** ; les broches 2 et 4 sont en **5 V**. Le +5 V du ventilateur va sur la broche 4 (ou 2), jamais sur la broche 1 voisine. Le signal PWM de la broche 7 est en 3,3 V, il ne faut pas lui appliquer de 5 V.

Un ventilateur à 2 fils (rouge et noir) tourne toujours à pleine vitesse ; le PWM n'est utile que s'il a un fil de commande.

| Réf. | Exigence |
|---|---|
| F1 | Le ventilateur est alimenté par le 40 broches (broches 4 et 6). La commande par la broche 7 est facultative : elle n'est utilisée que si le ventilateur est à 4 fils. |
| F2 | Le boîtier accepte **deux types de ventilateur 40 mm en 5 V** : à 2 fils (marche permanente, broches 4 et 6) ou à 4 fils (broches 4 et 6, plus la commande PWM broche 7). Les deux ont la même fixation et le même passage de câble. |
| F3 | Le ventilateur à 4 fils n'est réglable qu'après activation du PWM dans la configuration de la carte et ajout d'un script de réglage selon la température (hors boîtier, à traiter plus tard). |
| F4 | Le câble du ventilateur arrive jusqu'au 40 broches sans gêner les autres connecteurs ni le flux d'air. |
| F5 | Fixation au standard des ventilateurs 40 × 40 × 10 mm du commerce : **entraxe 32 × 32 mm**, vis M3 (trous de passage Ø 3,4 mm). Vérifié : Noctua NF-A4x10 5V PWM (fiche technique). Non vérifié sur la fiche produit : modèles 2 fils (Fechtner, WINSINN 4010), annoncés à 32 mm dans leur titre ou un résumé de recherche. **L'entraxe est à contrôler sur le ventilateur acheté** ; les trous du boîtier sont légèrement oblongs (± 0,5 mm) pour absorber un petit écart. |
| F6 | L'emplacement du ventilateur tolère les patins anti-vibration fournis avec certains modèles (épaisseur totale jusqu'à 12 mm). |

### 3.3 Antenne (reportée)

L'antenne est mise de côté pour l'instant : les exigences ci-dessous restent valables mais ne seront traitées que plus tard.

| Réf. | Exigence |
|---|---|
| A1 | **Option 1** : l'antenne fournie reste en place, à l'intérieur ou accrochée au boîtier. |
| A2 | **Option 2** : l'antenne fournie est remplacée par une antenne fixée sur le boîtier, reliée par un câble au connecteur de la carte. |
| A3 | Les deux options sont possibles avec le même boîtier. |

### 3.4 Fabrication

Boîtier imprimé en 3D en **PLA** (seule matière disponible). Fichiers sources au format **FreeCAD** (logiciel de l'utilisateur), avec export STL pour l'impression. Le PLA ramollit vers 55-60 °C : la conception évite tout contact entre le boîtier et les dissipateurs ou le SSD, et la température intérieure est mesurée lors des essais (§5).

## 4. Points ouverts

À préciser avant toute conception :

1. **Cotes restantes** : position exacte du microphone le long des bords (diamètre relevé : 5,1 mm). Les cotes USB et RJ45 sont relevées (voir plus haut). « Hauteur au-dessus de la carte » s'entend du dessus du circuit imprimé jusqu'au sommet du connecteur (confirmé).
2. **SSD** : le dépassement sous la carte est mesuré (4,5 mm). Reste à vérifier la longueur utile du SSD (2280 = 80 mm) par rapport à la longueur de la carte (89 mm).
3. **Ventilateur** : taille retenue **40 mm**, en 5 V, à 2 ou 4 fils (les deux sont prévus). Épaisseur : **10 mm**. Entraxe de fixation : 32 × 32 mm (standard du commerce, voir F5), à contrôler sur le modèle acheté.
4. **Dissipateurs** : hauteur mesurée, 6 mm. Reste à relever leur surface (longueur × largeur) et à confirmer si les 6 mm s'entendent au-dessus de la puce ou au-dessus du circuit imprimé.
5. **Antenne (reportée)** : type de connecteur de l'embase de la carte (U.FL probable, à confirmer) et antenne de remplacement (SMA ou RP-SMA, avec câble pigtail).
6. **Matière** : PLA (seule matière disponible). Aucun contact entre le boîtier et les parties chaudes (dissipateurs, SSD).
7. **Usage** : posé ou fixé au mur (voir 3.1 ter). Vis murales : Ø 3,5 ou 4 mm, tête jusqu'à 8 mm (les deux acceptées).
8. **Poussière** : un filtre sur l'entrée d'air est-il souhaité ?
9. **Accès** : capot vissé (décidé). Vis : M2,5 pour la carte, M3 pour le capot (l'utilisateur dispose des deux).

## 5. Validation prévue

- Mesure de la température du SoC et du SSD, à vide et sous charge prolongée, dans chaque sens de ventilation.
- Retenue du sens donnant les températures les plus basses, avec le niveau de bruit acceptable.
- Vérification de l'accès aux connecteurs et du montage des deux options d'antenne.
