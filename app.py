from gestion import ateliers

if role == "admin":
    st.header("Espace Administrateur")
    onglets = st.tabs(["Créer un atelier", "Voir les ateliers"])
    with onglets[0]:
        ateliers.creer_atelier()
    with onglets[1]:
        ateliers.afficher_ateliers()
