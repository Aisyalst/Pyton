import os
os .system('cls' if os.name =='nt' else clear)

nama_nasabah = input("Nama Nasabah :")
skor_kredit = float(input("Skor Kredit :"))

if skor_kredit > 800 :
    print(f"Sangat Layak: Bunga 2.5%, Persetujuan Instan")
elif skor_kredit >= 700 and skor_kredit <=800 :
    print(f"Layak: Bunga 3.5%, Persetujuan Cepat")
elif skor_kredit >= 600 and skor_kredit <=699 :
    print(f"Cukup Layak: Bunga 5%, Memerlukan Dokumen Tambahan")
elif skor_kredit >= 500 and skor_kredit <=599 :
    print(f"Resiko Tinggi: Bunga 7.5%, Wajib Jaminan Tambahan")
elif skor_kredit < 500 :
    print(f"Ditolak: Skor Terlalu Rendah")
else :
    print(f"Skor invalid")
    
