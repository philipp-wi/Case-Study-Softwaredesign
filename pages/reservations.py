import streamlit as st
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import date

db = TinyDB('database.json', storage=serializer)
reservations_table = db.table('reservations')
devices_table = db.table('devices')
users_table = db.table('users')

st.header("Reservierungen")
st.subheader("Neue Gerätereservierung anlegen oder entfernen")

available_devices = [device['device_name'] for device in devices_table.all()]
available_users = [user['name'] for user in users_table.all()]

selected_device = st.selectbox("Gerät auswählen:", available_devices)
responsible_user = st.selectbox("Verantwortlicher Nutzer:", available_users)
reservation_start = st.date_input("Startdatum:", min_value=date.today())
reservation_end = st.date_input("Enddatum:", min_value=reservation_start)

if st.button("Reservierung anlegen"):
        new_reservation = {
            "device_name": selected_device,
            "responsible_user": responsible_user,
            "start_date": reservation_start.isoformat(),
            "end_date": reservation_end.isoformat()
        }
        reservations_table.insert(new_reservation)
        st.success("Reservierung angelegt!✅")

if st.button("Reservierung löschen"):
    ReservationQuery = Query()
    result = reservations_table.search((ReservationQuery.device_name == selected_device))
    if result:
        reservations_table.remove(doc_ids=[result[0].doc_id])
        st.success("Reservierung gelöscht!✅")
    else:
        st.error("Keine Reservierung gefunden!❌")

st.text("Um eine Reservierung zu löschen, muss nur das Gerät oben ausgewählt werden.")
st.subheader("Aktuelle Reservierungen:")
reservations = reservations_table.all()

if reservations:
    for reservation in reservations:
        st.write(f"Gerät: {reservation['device_name']} | Verantwortlich: {reservation['responsible_user']} | Reservierungszeitraum: {reservation['start_date']} bis {reservation['end_date']}")
else:
    st.info("Keine Reservierungen vorhanden")
