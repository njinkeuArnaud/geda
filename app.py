import pandas as pd

# Chargement des utilisateurs depuis le fichier CSV
def charger_utilisateurs():
    return pd.read_csv("utilisateurs.csv")

# Appel de la fonction
utilisateurs = charger_utilisateurs()
