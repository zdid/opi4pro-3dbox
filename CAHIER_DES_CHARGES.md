# Cahier des charges — boîtier pour Orange Pi 4 Pro

Version : 0.13 (brouillon) — 2026-10-05

## 1. Objet

Boîtier destiné à contenir une carte **Orange Pi 4 Pro (A733)** avec refroidissement actif par ventilateur, un SSD fixé à l'arrière de la carte et une antenne remplaçable par une antenne déportée.

## 2. Données de la carte (source : manuel Orange Pi 4 Pro v1.4)

| Élément | Valeur |
|---|---|
| Dimensions du circuit imprimé | **89 mm × 55,7 mm** (mesuré ; le manuel indique 89 × 56) |
| Longueur avec les prises USB et RJ45 | **91,8 mm** (les prises dépassent de la carte de 2,8 mm) |
| Fixations | 4 trous de Ø 3,0 mm. Mesuré entre les bords extérieurs des trous : **52 mm en largeur** et **61 mm en longueur**, soit des entraxes de **49 mm × 58 mm** (même gabarit que le Raspberry Pi). Distance du bord extérieur du trou au bord le plus proche de la carte : **6 mm en longueur** et **1,75 mm en largeur**, soit des centres à **7,5 mm** et **3,25 mm** de ces bords. Côtés opposés (calculés, à vérifier) : 22 mm en longueur (89 − 6 − 61) et 1,95 mm en largeur (55,7 − 1,75 − 52). |
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
| SSD : dépassement sous la carte | 4,5 mm (du dessous du circuit imprimé de l'Orange Pi au dessous du SSD) |
| Espace entre les deux prises USB | 4,7 mm |
| Espace entre prise USB et RJ45 | 4,6 mm |

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
| C4 | Le ventilateur est fixé sur le boîtier, pas sur la carte. |
| C5 | La fente microSD (face arrière) reste accessible sans démonter le boîtier. |

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

### 3.3 Antenne

| Réf. | Exigence |
|---|---|
| A1 | **Option 1** : l'antenne fournie reste en place, à l'intérieur ou accrochée au boîtier. |
| A2 | **Option 2** : l'antenne fournie est remplacée par une antenne fixée sur le boîtier, reliée par un câble au connecteur de la carte. |
| A3 | Les deux options sont possibles avec le même boîtier. |

### 3.4 Fabrication (à confirmer)

Boîtier imprimé en 3D, fichiers sources fournis (format à décider).

## 4. Points ouverts

À préciser avant toute conception :

1. **Cotes restantes** : position des autres connecteurs (HDMI, USB-C, audio). Les cotes USB et RJ45 sont relevées (voir plus haut). « Hauteur au-dessus de la carte » s'entend du dessus du circuit imprimé jusqu'au sommet du connecteur (confirmé).
2. **SSD** : le dépassement sous la carte est mesuré (4,5 mm). Reste à vérifier la longueur utile du SSD (2280 = 80 mm) par rapport à la longueur de la carte (89 mm).
3. **Ventilateur** : taille retenue **40 mm**, en 5 V, à 2 ou 4 fils (les deux sont prévus). Reste à préciser : épaisseur (10 mm ou 20 mm) et entraxe des trous de fixation.
4. **Dissipateurs** : hauteur mesurée, 6 mm. Reste à relever leur surface (longueur × largeur) et à confirmer si les 6 mm s'entendent au-dessus de la puce ou au-dessus du circuit imprimé.
5. **Antenne** : type de connecteur de l'embase de la carte (U.FL probable, à confirmer) et antenne de remplacement (SMA ou RP-SMA, avec câble pigtail).
6. **Matière et impression** : PLA, PETG ou ASA. La température intérieure peut dépasser la tenue du PLA.
7. **Usage** : bureau, serveur, mur ou rack. Cela détermine l'orientation et les pieds.
8. **Poussière** : un filtre sur l'entrée d'air est-il souhaité ?
9. **Accès** : boîtier ouvrable sans outil, ou vissé ?

## 5. Validation prévue

- Mesure de la température du SoC et du SSD, à vide et sous charge prolongée, dans chaque sens de ventilation.
- Retenue du sens donnant les températures les plus basses, avec le niveau de bruit acceptable.
- Vérification de l'accès aux connecteurs et du montage des deux options d'antenne.
