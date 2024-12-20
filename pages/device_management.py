import streamlit as st

st.header("Geräteverwaltung")
st.subheader("Neues Gerät anlegen oder bestehendes Gerät ändern")

device_id = st.number_input("Geräte ID", step=1)
device_select = st.selectbox("Gerät auswählen:", ["Testgerät1", "Testgerät2"])
responsible_user = st.selectbox("Verantwortlicher Nutzer:", ["Max Mustermann", "Erika Musterfrau"])
next_maintenance = st.date_input("Nächste Wartung:")
maintenance_interval = st.number_input("Wartungsintervall (in Tagen):", 0, 365)
maintenance_costs = st.number_input("Wartungskosten (in €)")

if st.button("Gerät speichern"):
    if (device_id and device_select and responsible_user and next_maintenance and maintenance_interval and maintenance_costs):
        st.success(f"{device_select} mit ID: {device_id} wurde erfolgreich gespeichert.")
    else:
        st.error("Bitte alle Felder ausfüllen!")

