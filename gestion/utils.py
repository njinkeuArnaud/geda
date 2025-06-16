# gestion/utils.py

import qrcode
import os

def generer_qr_code(data: str, fichier_sortie: str):
    img = qrcode.make(data)
    dossier = "data/qrcodes"
    os.makedirs(dossier, exist_ok=True)
    chemin = os.path.join(dossier, fichier_sortie)
    img.save(chemin)
    return chemin
