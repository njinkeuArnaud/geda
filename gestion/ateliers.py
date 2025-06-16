# gestion/ateliers.py

import streamlit as st
import pandas as pd
import csv
import uuid
import os
from datetime import datetime

def creer_atelier():
    st.subheader("Créer un nouvel atelier")
    with st.form("form_ajout_atelier"):
        titre = st.text_input("Titre de l'atelier")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Créer l'atelier")

    if submitted:
        if titre.strip() == "":
            st.warning("Le titre est obligatoire.")
        else:
            atelier = {
                "id_atelier": str(uuid.uuid4()),
                "titre": titre,
                "description": description,
                "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

            fichier = "data/ateliers.csv"
            fichier_existe = os.path.exists(fichier)

            with open(fichier, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=atelier.keys())
                if not fichier_existe:
                    writer.writeheader()
                writer.writerow(atelier)

            st.success(f"L’atelier **{titre}** a été créé avec succès ✅")

def afficher_ateliers():
    st.subheader("Liste des ateliers existants")
    fichier = "data/ateliers.csv"
    if os.path.exists(fichier):
        df = pd.read_csv(fichier)
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Aucun atelier enregistré.")
    else:
        st.info("Le fichier ateliers.csv n’existe pas encore.")
