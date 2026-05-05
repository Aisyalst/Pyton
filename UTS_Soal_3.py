import os
os.system('cls' if os.name == 'nt' else 'clear')

#perulangan dan pendklarasian variabel untuk nomor titik
for nomor in range(1, 7):
    #menggunakan operator modulus untuk menentukan genap/ganjil
    if nomor % 2 == 0: #kondisi untuk nomor genap
        status = "Koneksi Internet Stabil"
    else: #kondisi untuk nomor ganjil
        status = "Koneksi Internet Lemah"
    
    #menampilkan hasil untuk setiap titik
    print(f"Titik {nomor}: {status}")
    #mengulangi proses sampai nomor 6