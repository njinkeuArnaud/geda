import streamlit as st
import pandas as pd
import os

DATA_FILE = 'participants.csv'

# Fonction pour charger les données
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=['Nom', 'Prénom', 'Email'])

# Fonction pour enregistrer un participant
def save_participant(nom, prenom, email):
    df = load_data()
    new_entry = pd.DataFrame([[nom, prenom, email]], columns=['Nom', 'Prénom', 'Email'])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

st.title("Inscription aux ateliers")

# Formulaire d'inscription
with st.form(key='inscription_form'):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    email = st.text_input("Email")
    submit_button = st.form_submit_button(label='S\'inscrire')

if submit_button:
    if nom and prenom and email:
        save_participant(nom, prenom, email)
        st.success(f"Merci {prenom} {nom}, votre inscription est bien prise en compte !")
    else:
        st.error("Veuillez remplir tous les champs.")

st.header("Liste des participants inscrits")
data = load_data()
st.dataframe(data)
