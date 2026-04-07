import os
os .system('cls' if os.name =='nt' else clear)

nama_lokasi = input("Masukkan nama lokasi       : ")
kapasitas    = float(input("Masukkan kapasitas maksimal: "))
volume       = float(input("Masukkan volume isi saat ini: "))

sisa = kapasitas - volume

print()
print(f"Lokasi             : {nama_lokasi}")
print(f"Kapasitas Maksimal : {kapasitas} liter")
print(f"Volume Saat Ini    : {volume} liter")
print(f"Sisa Kapasitas     : {sisa} liter")
