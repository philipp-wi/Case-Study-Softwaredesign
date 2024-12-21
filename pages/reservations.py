import streamlit as st

st.header("Reservierungen")
st.subheader("Neue Gerätereservierung anlegen oder entfernen")

device_id = st.number_input("Geräte ID", step=1)
device_select = st.selectbox("Gerät auswählen:", ["Testgerät1", "Testgerät2"])
responsible_user = st.selectbox("Verantwortlicher Nutzer:", ["Max Mustermann", "Erika Musterfrau"])
reservation_start = st.date_input("Startdatum:")
reservation_end = st.date_input("Enddatum:")

st.button("Reservierung anlegen")
st.button("Reservierung löschen")
 
st.subheader("Aktuelle Reservierungen:")