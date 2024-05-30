import streamlit as st

# Title of the app
st.title("Faut-il encore travailler ?")
prenom = st.text_input("Salut, moi c'est Charles, et toi comment t'appelles tu ?","ton_prénom")
age = st.slider("Quel age as tu?", 0, 130, 25)
if age < 16:
    text = "return à l'ecole"
elif age < 25:
    text = "tu es sûr de ne pas vouloir continuer l'école"
elif age < 30:
    text="bon à un moment il faut travailler pour vivre et non vivre pour travailler !"
elif age <70:
    text = "aller encore un effort, faut travailler encore "+str(70-age)+"ans"
elif age <80:
    text = "un repot bien mérité"
else :
    text = "félicitation d'être arrivé jusque là !"
if st.button("synthèse des infos transmises"):
    st.write("Salut, ",prenom, "tu as ", age, "ans, ", text)
else:
    st.write("au revoir")