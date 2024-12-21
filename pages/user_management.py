
st.write("Nutzerverwaltung")

def clearText():
    st.session_state.name = ""
    st.session_state.alter = ""
    st.session_state.jahrgang = ""
    st.session_state.email = ""

with st.popover("Neuen Benutzer Anlegen"):
    st.write("Neuer Benutzer:")

    name = st.text_input("Name", key="name")
    alter = st.text_input("Alter",key="alter")
    jahrgang = st.text_input("Jahrgang",key="jahrgang")
    email = st.text_input("email",key="email")
    create = st.button("Nutzer Anlegen")

    st.button("Eingabe löschen",on_click=clearText)

    if(create and (name == '' or alter == '' or jahrgang == '' or email == '')):
        st.markdown("❌ Nutzerdaten fehlen!")
    elif(create):
        st.markdown("✅ Nutzer Angelegt")
