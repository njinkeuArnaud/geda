import qrcode
import os

def generer_qr_code(data: str, fichier_sortie: str):
    img = qrcode.make(data)
    os.makedirs("data/qrcodes", exist_ok=True)
    chemin = os.path.join("data/qrcodes", fichier_sortie)
    img.save(chemin)
    return chemin
