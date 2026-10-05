# CLAUDE.md

Boîtier imprimé en 3D (PLA) pour une carte **Orange Pi 4 Pro** avec SSD M.2 au dos et ventilateur 40 × 10 mm dans le capot.

## Fichiers de référence

- `CAHIER_DES_CHARGES.md` : exigences et **toutes les cotes mesurées sur la carte**. C'est la source de vérité. Toute nouvelle mesure ou décision y est ajoutée, et sa version (en-tête) est incrémentée.
- `freecad/boitier_opi4pro.FCMacro` : macro FreeCAD (Python, module `Part`) qui construit le socle, le capot et une maquette de la carte. Toutes les cotes sont des paramètres commentés en tête de fichier.
- `freecad/LISEZMOI.md` : mode d'emploi, visserie, impression, **liste des variables d'ajustement**. À tenir à jour à chaque nouveau paramètre.
- `freecad/boitier_opi4pro.FCStd`, `freecad/socle.stl`, `freecad/capot.stl` : produits par la macro. Les régénérer et les commiter après chaque modification de la macro.

## Repère de la macro (mm)

- X : longueur de la carte. 0 = petit côté **sans USB**, 89 = côté USB/RJ45.
- Y : largeur. 0 = grand côté du **40 broches**, 55,7 = grand côté HDMI / USB-C / audio.
- Z : 0 = **dessous** du circuit imprimé (épaisseur 1,3 mm).

Attention aux références des mesures de l'utilisateur : certaines hauteurs sont prises « carte incluse » (depuis le dessous de la carte), d'autres « au-dessus de la carte ». Le cahier des charges précise chaque fois laquelle.

## Utilisateur

- Échanges en **français**. Il utilise **FreeCAD 1.1.1** et **Cura**, imprime en **PLA uniquement**.
- Il mesure lui-même les cotes sur la carte : quand une mesure est ambiguë (référence, côté), demander plutôt que supposer. Une valeur supposée est marquée « A MESURER » dans la macro et listée dans `LISEZMOI.md`.
- Ne pas affirmer une donnée externe (fiche technique, entraxe…) sans l'avoir vérifiée ; dire ce qui est vérifié et ce qui ne l'est pas.

## Git

- **Une seule branche : `main`.** L'utilisateur ne veut pas d'autres branches ni de pull request pour l'instant. Commits atomiques, messages en français.
- La session cloud ne peut pas supprimer de branche sur GitHub (refus 403) : ne pas en créer.

## Tester la macro dans une session cloud

FreeCAD n'est pas dans les paquets apt et GitHub (AppImage) est bloqué par le proxy ; conda-forge est accessible :

```bash
mkdir -p /opt/mm && cd /opt/mm
curl -sSL https://conda.anaconda.org/conda-forge/linux-64/micromamba-2.9.0-0.tar.bz2 | tar -xj bin/micromamba
MAMBA_ROOT_PREFIX=/opt/mm/root ./bin/micromamba create -y -q -p /opt/mm/fc -c conda-forge "freecad=1.1"
```

(environ 5 Go, plusieurs minutes, à lancer en arrière-plan). Puis, depuis la racine du dépôt :

```bash
cd freecad && /opt/mm/fc/bin/freecadcmd boitier_opi4pro.FCMacro   # régénère FCStd + STL
/opt/mm/fc/bin/freecadcmd outils/verifier.py                        # doit afficher RESULTAT : OK
```

`verifier.py` contrôle que les pièces sont des solides valides et ne touchent pas la maquette de la carte. Quand un élément de la carte est ajouté ou modifié, le reporter aussi dans `construire_maquette()` pour que le contrôle reste significatif.
