import streamlit as st
import users

st.write("Nutzerverwaltung")

name = st.text_input("Nutzername")
nutzerid = st.text_input("ID (Optional)")

suchen = st.button("Nutzer suchen")
loeschen = st.button("Nutzer löschen")

if (suchen):
    user = users.User.find_by_attribute("name", name)
    if (user == None):
        st.text("Nutzer nicht gefunden❌")
    else:    
        st.text("Nutzer gefunden✅")

if (loeschen):
    user = users.User.find_by_attribute("name", name)
    if (user == None):
        st.text("Nutzer existieirt nicht❌")
    else:
        user.delete()
        st.text("Nutzer wurde gelöscht✅")


def clearText():
    st.session_state.name = ""
    st.session_state.nutzerId = ""
    st.session_state.alter = ""
    st.session_state.jahrgang = ""
    st.session_state.email = ""

with st.popover("Neuen Benutzer Anlegen"):
    st.write("Neuer Benutzer:")

    name = st.text_input("Name", key="name")
    nutzerId = st.text_input("ID",key="nutzerId")
    alter = st.text_input("Alter",key="alter")
    jahrgang = st.text_input("Jahrgang",key="jahrgang")
    email = st.text_input("email",key="email")
    create = st.button("Nutzer Anlegen")

    st.button("Eingabe löschen",on_click=clearText)

    if(create and (name == '' or nutzerId == '')):
        st.markdown("❌ Nutzerdaten fehlen!")
    elif(create):
        st.markdown("✅ Nutzer Angelegt/Geändert")
        temp = users.User(nutzerId,name)
        temp.setOptionalData(alter,jahrgang,email)
        temp.store_data()
