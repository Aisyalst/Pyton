def tambah(a, b):
    """Menambah dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangi dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa membagi dengan 0"
    return a / b

def main():
    print("=" * 40)
    print("   KALKULATOR SEDERHANA")
    print("=" * 40)
    print("\nPilihan operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")
    
    while True:
        pilihan = input("\nPilih operasi (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil = tambah(angka1, angka2)
                    print(f"\nHasil: {angka1} + {angka2} = {hasil}")
                elif pilihan == '2':
                    hasil = kurang(angka1, angka2)
                    print(f"\nHasil: {angka1} - {angka2} = {hasil}")
                elif pilihan == '3':
                    hasil = kali(angka1, angka2)
                    print(f"\nHasil: {angka1} × {angka2} = {hasil}")
                elif pilihan == '4':
                    hasil = bagi(angka1, angka2)
                    print(f"\nHasil: {angka1} ÷ {angka2} = {hasil}")
            
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, 4, atau 5.")

if __name__ == "__main__":
    main()
