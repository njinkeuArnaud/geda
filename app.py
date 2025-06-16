# app.py

import streamlit as st
from gestion import ateliers
# from gestion import ateliers, sessions, utilisateurs

# Initialisation des variables de session
if "authentifie" not in st.session_state:
    st.session_state["authentifie"] = False
    st.session_state["role"] = None
    st.session_state["email"] = ""

# Interface de connexion
if not st.session_state["authentifie"]:
    st.title("Connexion à la plateforme")

    email = st.text_input("Email")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        role = utilisateurs.verifier_identifiants(email, mot_de_passe)
        if role:
            st.session_state["authentifie"] = True
            st.session_state["role"] = role
            st.session_state["email"] = email
            st.success(f"Bienvenue, {role.capitalize()} 👋")
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")
else:
    st.sidebar.success(f"Connecté en tant que : {st.session_state['email']} ({st.session_state['role']})")
    if st.sidebar.button("Se déconnecter"):
        st.session_state["authentifie"] = False
        st.session_state["role"] = None
        st.session_state["email"] = ""
        st.rerun()

    # Interface ADMINISTRATEUR
    if st.session_state["role"] == "admin":
        onglets = st.tabs(["➕ Créer un atelier", "📋 Voir les ateliers", "👥 Gérer les utilisateurs"])
        with onglets[0]:
            ateliers.creer_atelier()
        with onglets[1]:
            ateliers.afficher_ateliers()
        with onglets[2]:
            utilisateurs.gestion_utilisateurs()

    # Interface UTILISATEUR
    elif st.session_state["role"] == "utilisateur":
        onglets = st.tabs(["📅 Créer une session", "📋 Mes sessions"])
        with onglets[0]:
            sessions.creer_session(st.session_state["email"])
        with onglets[1]:
            sessions.afficher_sessions(st.session_state["email"])
