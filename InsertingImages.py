import streamlit as st
from PIL import Image

image = Image.open("icon.png")

st.title("StreamLit Tutorials")

st.image(image, caption="App Logo", width=100)

st.markdown("<h3 style='text-align: left; font-size: 18px; margin-left: 10px;'>Description</h3>",
            unsafe_allow_html=True)

st.divider()

with open("icon.png", "rb") as file:
    btn = st.download_button(
        label="Télécharger l'image",
        data=file,
        file_name="icon.png",
        mime="image/png"
    )

# Création de deux colonnes avec st.beta_columns()
col1, col2 = st.columns([1, 3])

# Colonne 1 : Affichage de l'image
with col1:
    st.image(image, caption="", width=100)

# Colonne 2 : Affichage du texte
with col2:
    st.markdown("<h1 style='font-size: 25px;'>Description</h1>", unsafe_allow_html=True)
# st.write("Voici une description de l'application.")
