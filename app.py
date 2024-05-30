import streamlit as st

# Title of the app
st.title("Student Information")
prenom = st.text_input("Salut, moi c'est Charles, et toi comment t'appelles tu ?","ton_prénom")
age = st.slider("Quel age as tu?", 0, 130, 25)
st.write("tu as ", age, "ans, félicitation d'être arrivé jusque là !")
if st.button("synthèse des infos transmises"):
    st.write("Salut, ",prenom, "tu as ", age, "ans, félicitation d'être arrivé jusque là !")
else:
    st.write("au revoir")