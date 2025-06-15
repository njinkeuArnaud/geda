import streamlit as st
import pandas as pd
import csv
import uuid
from datetime import datetime

# --- Fonction pour charger les ateliers ---
def creer_atelier():
    st.subheader("Créer un nouvel atelier")
    # Formulaire pour créer un atelier
    with st.form("form_ajout_atelier"):
        titre = st.text_input("Titre de l'atelier")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Créer l'atelier")
    
    if submitted:
        if titre.strip() == "":
            st.warning("Le titre est obligatoire.")
        else:
            # Créer une ligne pour le nouvel atelier
            atelier = {
                "id_atelier": str(uuid.uuid4()),
                "titre": titre,
                "description": description,
                "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
    
            # Sauvegarder dans ateliers.csv (création ou ajout)
            fichier_ateliers = "ateliers.csv"
            fichier_existe = os.path.exists(fichier_ateliers)
    
            with open(fichier_ateliers, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=atelier.keys())
                if not fichier_existe:
                    writer.writeheader()
                writer.writerow(atelier)
            st.success(f"L’atelier **{titre}** a été créé avec succès ✅")

# --- Fonction pour charger les utilisateurs ---
def charger_utilisateurs():
    return pd.read_csv("utilisateurs.csv")

# --- Formulaire de connexion ---
st.title("Connexion à la plateforme")

with st.form("login_form"):
    email = st.text_input("Email")
    mot_de_passe = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("Se connecter")

utilisateurs = charger_utilisateurs()

# --- Vérification des identifiants ---
if submitted:
    utilisateur = utilisateurs[
        (utilisateurs['email'] == email) &
        (utilisateurs['mot_de_passe'] == mot_de_passe)
    ]

    if not utilisateur.empty:
        st.session_state['utilisateur'] = utilisateur.iloc[0].to_dict()
        st.session_state['connecté'] = True
        st.success("Connexion réussie ! Rechargez la page pour accéder au tableau de bord.")
    else:
        st.error("Email ou mot de passe incorrect.")

# --- Interface après connexion ---
if st.session_state.get('connecté', False):
    utilisateur = st.session_state['utilisateur']
    role = utilisateur['role']
    nom = utilisateur['nom']

    st.sidebar.success(f"Bienvenue, {nom} ({role})")

    if role == "admin":
        st.header("Tableau de bord Administrateur")
        st.write("Vous avez tous les droits.")
        creer_atelier()
    else:
        st.header("Tableau de bord Utilisateur")
        st.write("Accès limité aux sessions que vous organisez.")
