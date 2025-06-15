import streamlit as st
import pandas as pd

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
    else:
        st.header("Tableau de bord Utilisateur")
        st.write("Accès limité aux sessions que vous organisez.")
