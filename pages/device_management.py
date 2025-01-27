import streamlit as st
from devices import Device
from users import User 

st.header("Geräteverwaltung")
st.subheader("Neues Gerät anlegen, bestehendes Gerät ändern oder löschen")

devices = Device.find_all()
device_choices = ["Neues Gerät anlegen"] + [device.device_name for device in devices]
users = User.db_connector.all()
user_choices = [user["name"] for user in users]

selected_device = st.selectbox("Gerät auswählen", device_choices)
if selected_device == "Neues Gerät anlegen":
    device_name = st.text_input("Neuer Gerätename")
else:
    device_name = selected_device

responsible_user = st.selectbox("Verantwortlicher Nutzer", user_choices)
next_maintenance = st.date_input("Nächste Wartung:")
maintenance_interval = st.number_input("Wartungsintervall (in Tagen):", min_value=0, step=1)
maintenance_costs = st.number_input("Wartungskosten (in €):", min_value=0.0, step=1.0)
is_active = st.checkbox("Gerät ist aktiv", value=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Gerät speichern/ändern"):
        if device_name and responsible_user and next_maintenance and maintenance_interval >= 0 and maintenance_costs >= 0:
            existing_device = Device.find_by_attribute("device_name", device_name)
            if existing_device:
                existing_device.managed_by_user_id = responsible_user
                existing_device.next_maintenance = str(next_maintenance)
                existing_device.maintenance_interval = maintenance_interval
                existing_device.maintenance_costs = maintenance_costs
                existing_device.is_active = is_active
                existing_device.store_data()
                st.success(f"Das Gerät '{device_name}' wurde erfolgreich aktualisiert!✅")
            else:
                new_device = Device(device_name=device_name, managed_by_user_id=responsible_user)
                new_device.is_active = is_active
                new_device.next_maintenance = str(next_maintenance)
                new_device.maintenance_interval = maintenance_interval
                new_device.maintenance_costs = maintenance_costs
                new_device.store_data()
                st.success(f"Das neue Gerät '{device_name}' wurde erfolgreich gespeichert!✅")
        else:
            st.error("Bitte alle Felder korrekt ausfüllen!❌")

with col2:
    if st.button("Gerät löschen"):
        if device_name and device_name != "Neues Gerät anlegen":
            device_to_delete = Device.find_by_attribute("device_name", device_name)
            if device_to_delete:
                device_to_delete.delete()
                st.success(f"Das Gerät '{device_name}' wurde erfolgreich gelöscht!✅")
            else:
                st.error(f"Gerät mit dem Namen '{device_name}' nicht gefunden!")
        else:
            st.error("Bitte einen gültigen Gerätenamen eingeben oder auswählen, um es zu löschen!❌")
st.text("Um ein Gerät zu löschen, muss nur das Gerät oben ausgewählt werden.")