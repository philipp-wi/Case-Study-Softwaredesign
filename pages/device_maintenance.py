import streamlit as st
from tinydb import TinyDB
from serializer import serializer

db = TinyDB('database.json', storage=serializer)
devices_table = db.table('devices')

st.header("Gerätewartung")
st.subheader("Wartungsinformationen")

devices = devices_table.all()

if devices:
    for device in devices:
        if 'next_maintenance' in device:
            st.write(f"Gerät: {device['device_name']}")
            st.write(f"Nächste Wartung: {device['next_maintenance']}")
            st.write(f"Wartungsintervall: {device['maintenance_interval']} Tage")
            st.write(f"Wartungskosten: {device['maintenance_costs']} €")
            st.write("---")
else:
    st.info("Keine Wartungen vorhanden!")
