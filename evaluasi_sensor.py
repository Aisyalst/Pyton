import os
os .system('cls' if os.name =='nt' else 'clear')

data_mentah = "ID:PCT-08|VOL:42.5|STAT:ON"

lokasi = data_mentah[3:9]
volume = data_mentah[14:18]
status = data_mentah[24:]
volume = float(volume)
status_sensor = volume > 40 and status == "ON"

print(f"Id Lokasi: {lokasi}")  
print(f"Volume: {volume}")  
print(f"Status: {status}") 

print(f"Status Sensor: {status_sensor}")

if status_sensor:
    print(f"Status Sensor: ON")
else:
    print(f"Status Sensor: OFF")