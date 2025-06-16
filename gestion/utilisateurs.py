# gestion/utilisateurs.py

import streamlit as st
import pandas as pd
import os
import csv
import uuid

FICHIER_UTILISATEURS = "data/utilisateurs.csv"

# ✅ Vérifie email + mot de passe, retourne le rôle (admin ou utilisateur)
def verifier_identifiants(email, mdp):
    if os.path.exists(FICHIER_UTILISATEURS):
        df = pd.read_csv(FICHIER_UTILISATEURS)
        utilisateur = df[(df["email"] == email) & (df["mot_de_passe"] == mdp)]
        if not utilisateur.empty:
            return utilisateur.iloc[0]["role"]
    return None

# ✅ Affiche tous les utilisateurs (admin uniquement)
def gestion_utilisateurs():
    st.subheader("📋 Liste des utilisateurs enregistrés")

    if os.path.exists(FICHIER_UTILISATEURS):
        df = pd.read_csv(FICHIER_UTILISATEURS)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucun utilisateur enregistré.")

    st.markdown("---")
    st.subheader("➕ Ajouter un nouvel utilisateur")

    with st.form("form_ajout_user"):
        email = st.text_input("Email")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        role = st.selectbox("Rôle", ["utilisateur", "admin"])
        submit = st.form_submit_button("Ajouter")

    if submit:
        if email and mot_de_passe:
            ajouter_utilisateur(email, mot_de_passe, role)
            st.success(f"Utilisateur **{email}** ajouté avec le rôle **{role}**")
        else:
            st.warning("Veuillez remplir tous les champs.")

# ✅ Ajoute un utilisateur dans le fichier CSV
def ajouter_utilisateur(email, mot_de_passe, role):
    utilisateur = {
        "email": email,
        "mot_de_passe": mot_de_passe,
        "role": role
    }

    fichier_existe = os.path.exists(FICHIER_UTILISATEURS)

    with open(FICHIER_UTILISATEURS, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=utilisateur.keys())
        if not fichier_existe:
            writer.writeheader()
        writer.writerow(utilisateur)
