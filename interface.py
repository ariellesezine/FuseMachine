import streamlit as st
import requests

st.title("calculatrice")

nb1 = st.number_input("entrez un nombre ")
nb2 = st.number_input("entrez un autre nombre")
op = st.text_input("operateur")

if st.button("Envoyer à l'API"):
    data = {
        "nb1": nb1,
        "nb2": nb2,
        "op": op
    }

    try:
        response = requests.post("http://127.0.0.1:8000/calculer/", json=data)
        if response.status_code == 200:
            st.success(f"Réponse API :")
            st.json(response.json())
        else:
            st.error(f"Erreur : {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Erreur lors de la requête : {e}")