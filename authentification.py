import streamlit as st

st.title("Connexion à la plateforme")

# Formulaire de connexion
with st.form("login_form"):
    email = st.text_input("Email")
    mot_de_passe = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("Se connecter")

# Chargement des utilisateurs
utilisateurs = charger_utilisateurs()

# Traitement de la connexion
if submitted:
    utilisateur = utilisateurs[
        (utilisateurs['email'] == email) &
        (utilisateurs['mot_de_passe'] == mot_de_passe)
    ]

    if not utilisateur.empty:
        role = utilisateur.iloc[0]['role']
        st.success(f"Connexion réussie en tant que **{role}** !")
        st.session_state['utilisateur'] = utilisateur.iloc[0].to_dict()
        st.session_state['connecté'] = True
    else:
        st.error("Email ou mot de passe incorrect.")