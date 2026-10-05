# Vérification du modèle, à lancer après la macro :
#   freecadcmd freecad/outils/verifier.py
# Contrôle que le socle et le capot sont des solides valides et qu'ils ne
# touchent pas la maquette de la carte (prises, SSD, ventilateur, micro, microSD).
import os
import FreeCAD as App

ici = os.path.dirname(os.path.abspath(__file__))
doc = App.openDocument(os.path.join(ici, "..", "boitier_opi4pro.FCStd"))
maquette = doc.getObject("Maquette_carte").Shape
ok = True
for nom in ("Socle", "Capot"):
    sh = doc.getObject(nom).Shape
    collision = sh.common(maquette).Volume
    bb = sh.BoundBox
    print("%s : valide=%s, collision avec la maquette=%.3f mm3, %.1f x %.1f x %.1f mm"
          % (nom, sh.isValid(), collision, bb.XLength, bb.YLength, bb.ZLength))
    ok = ok and sh.isValid() and collision < 1e-3
print("RESULTAT :", "OK" if ok else "ECHEC")
