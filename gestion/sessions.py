# gestion/sessions.py

import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime
from gestion.utils import generer_qr_code  # Assure-toi que utils.py est créé

FICHIER_SESSIONS = "data/sessions.csv"
FICHIER_ATELIERS = "data/ateliers.csv"

# ✅ Création d'une nouvelle session de formation
def creer_session(email_utilisateur):
    st.subheader("➕ Créer une session de formation")

    if not os.path.exists(FICHIER_ATELIERS):
        st.warning("Aucun atelier disponible. Veuillez contacter l’administrateur.")
        return

    df_ateliers = pd.read_csv(FICHIER_ATELIERS)
    titres = df_ateliers["titre"].tolist()

    with st.form("form_session"):
        atelier_choisi = st.selectbox("Atelier concerné", titres)
        date_session = st.date_input("Date de la session")
        lieu = st.text_input("Lieu de la session")
        submit = st.form_submit_button("Créer la session")

    if submit:
        id_session = str(uuid.uuid4())
        session = {
            "id_session": id_session,
            "atelier": atelier_choisi,
            "date": date_session.strftime("%Y-%m-%d"),
            "lieu": lieu,
            "cree_par": email_utilisateur
        }

        df = pd.DataFrame([session])

        fichier_existe = os.path.exists(FICHIER_SESSIONS)
        df.to_csv(FICHIER_SESSIONS, mode="a", header=not fichier_existe, index=False)

        st.success("Session créée avec succès ✅")

        # Générer QR code pour inscription
        lien_qr = f"https://tonapp.streamlit.app/inscription?id={id_session}"  # à personnaliser
        chemin_qr = generer_qr_code(lien_qr, f"{id_session}.png")
        st.image(chemin_qr, caption="QR Code pour inscription", width=200)

# ✅ Affiche les sessions créées par un utilisateur donné
def afficher_sessions(email_utilisateur):
    st.subheader("📅 Mes sessions de formation")

    if os.path.exists(FICHIER_SESSIONS):
        df = pd.read_csv(FICHIER_SESSIONS)
        df_user = df[df["cree_par"] == email_utilisateur]

        if not df_user.empty:
            st.dataframe(df_user, use_container_width=True)
        else:
            st.info("Vous n'avez encore créé aucune session.")
    else:
        st.info("Aucune session enregistrée.")
