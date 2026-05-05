import os
os.system('cls' if os.name == 'nt' else 'clear')

#mendklarasikan variabel untuk batas kapasitas dan total berat saat ini
batas_kapasitas = 30  # kg
total_berat = 5.5     # kg saat ini

#menampilkan informasi awal tentang Smart Bin
print("Smart Bin Area Perpustakaan")
print(f"Kapasitas Maksimal: {batas_kapasitas} kg")
print(f"Berat Saat Ini: {total_berat} kg")

#meminta input berat buku yang dibuang
berat_buku = float(input("\nMasukkan berat buku yang dibuang (kg): "))

#menghitung total berat (total_berat sebelumnya + berat buku baru)
total_berat += berat_buku

#menghitung sisa kapasitas
sisa_kapasitas = batas_kapasitas - total_berat

#menampilkan hasil perhitungan total berat dan sisa kapasitas
print(f"Total Berat Sekarang: {total_berat} kg")
print(f"Sisa Kapasitas: {sisa_kapasitas} kg")