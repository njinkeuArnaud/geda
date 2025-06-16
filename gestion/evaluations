# gestion/evaluations.py

import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime

def creer_evaluation():
    st.subheader("Créer une évaluation pour un atelier")

    fichier_ateliers = "data/ateliers.csv"
    if not os.path.exists(fichier_ateliers):
        st.warning("Aucun atelier trouvé.")
        return

    df_ateliers = pd.read_csv(fichier_ateliers)
    titres = df_ateliers["titre"].tolist()

    with st.form("form_evaluation"):
        atelier = st.selectbox("Atelier concerné", titres)
        question = st.text_area("Question")
        type_q = st.selectbox("Type de question", ["Choix unique", "Texte libre"])
        options = ""
        if type_q == "Choix unique":
            options = st.text_input("Options (séparées par des virgules)")
        submit = st.form_submit_button("Ajouter la question")

    if submit:
        evaluation = {
            "id": str(uuid.uuid4()),
            "atelier": atelier,
            "question": question,
            "type": type_q,
            "options": options,
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        fichier = "data/evaluations.csv"
        df = pd.DataFrame([evaluation])

        if os.path.exists(fichier):
            df.to_csv(fichier, mode="a", header=False, index=False)
        else:
            df.to_csv(fichier, index=False)

        st.success("Question ajoutée à l’évaluation ✅")
