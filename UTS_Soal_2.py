import os
os.system('cls' if os.name == 'nt' else 'clear')

#mendklarasikan variabel untuk kode sensor
kode_sensor = "BIN-05-PAPR"
#mencetak kode sensor yang diberikan
print(f"\nKode dari Sensor: {kode_sensor}")

#mengambil kode sampah menggunakan dari 4 huruh terakhir dari kode_sensor
kode_sampah = kode_sensor[-4:]

#mencetak kode sampah yang diambil
print(f"Kode Sampah: '{kode_sampah}'")

#logika if-elif-else untuk menentukan kategori sampah
if kode_sampah == "PLST": #kondisi untuk sampah plastik
    kategori = "Sampah Plastik"
elif kode_sampah == "PAPR": #kondisi untuk sampah kertas
    kategori = "Sampah Kertas"
else: #kondisi untuk sampah umum jika kode sampah tidak cocok dengan plastik atau kertas
    kategori = "Sampah Umum"

#menampilkan kategori sampah berdasarkan kode yang diambil
print(f"Kategori: {kategori}")