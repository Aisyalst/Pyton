import os
os .system('cls' if os.name =='nt' else clear)

nama_perangkat = input("Nama Perangkat :")
perintah_suara = input("Perintah Suara :")

match perintah_suara :
    case "NYALAKAN_LAMPU" :
        print(f"Aksi: Lampu utama dihidupkan, kecerahan 100%") 
    case "MATIKAN_LAMPU" :
        print(f"Aksi: Semua lampu dimatikan") 
    case "MODE_MALAM" :
        print(f"Aksi: Mengunci semua pintu dan mengaktifkan sensor gerak") 
    case "PUTAR_MUSIK" :
        print(f"Aksi: Memutar daftar lagu favorit di speaker utama") 
    case "CEK_SUHU" :
        print(f"Aksi: Menampilkan suhu dan kelembapan ruangan saat ini") 
    case "SOS" :
        print(f"Aksi: PERINGATAN : Menghubungi nomor darurat dan menyalakan alarm") 
    case _:
        print(f"Perintah Tidak dikenal: Silakan ulangi instruksi anda") 