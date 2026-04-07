# Contoh Slicing dengan Python

# ===== 1. SLICING STRING =====
print("=" * 50)
print("1. SLICING STRING")
print("=" * 50)

text = "Hello World"
print(f"Text: {text}")
print(f"text[0:5]: {text[0:5]}")          # Hello
print(f"text[6:11]: {text[6:11]}")        # World
print(f"text[:5]: {text[:5]}")            # Hello (dari awal sampai index 5)
print(f"text[6:]: {text[6:]}")            # World (dari index 6 sampai akhir)
print(f"text[-5:]: {text[-5:]}")          # World (5 karakter terakhir)
print(f"text[::2]: {text[::2]}")          # HloWrd (setiap 2 karakter)
print(f"text[::-1]: {text[::-1]}")        # dlroW olleH (reverse)

# ===== 2. SLICING LIST =====
print("\n" + "=" * 50)
print("2. SLICING LIST")
print("=" * 50)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {numbers}")
print(f"numbers[0:5]: {numbers[0:5]}")    # [0, 1, 2, 3, 4]
print(f"numbers[5:10]: {numbers[5:10]}")  # [5, 6, 7, 8, 9]
print(f"numbers[:3]: {numbers[:3]}")      # [0, 1, 2]
print(f"numbers[7:]: {numbers[7:]}")      # [7, 8, 9]
print(f"numbers[-3:]: {numbers[-3:]}")    # [7, 8, 9] (3 elemen terakhir)
print(f"numbers[::2]: {numbers[::2]}")    # [0, 2, 4, 6, 8] (setiap 2 elemen)
print(f"numbers[::-1]: {numbers[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# ===== 3. SLICING TUPLE =====
print("\n" + "=" * 50)
print("3. SLICING TUPLE")
print("=" * 50)

fruits = ("apel", "pisang", "mangga", "jeruk", "anggur")
print(f"Tuple: {fruits}")
print(f"fruits[1:3]: {fruits[1:3]}")      # ('pisang', 'mangga')
print(f"fruits[::2]: {fruits[::2]}")      # ('apel', 'mangga', 'anggur')
print(f"fruits[::-1]: {fruits[::-1]}")    # ('anggur', 'jeruk', 'mangga', 'pisang', 'apel')

# ===== 4. SLICING DENGAN STEP NEGATIF =====
print("\n" + "=" * 50)
print("4. SLICING DENGAN STEP NEGATIF")
print("=" * 50)

data = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Data: {data}")
print(f"data[7:2:-1]: {data[7:2:-1]}")    # [80, 70, 60, 50, 40]
print(f"data[::-2]: {data[::-2]}")        # [80, 60, 40, 20]
print(f"data[5:1:-2]: {data[5:1:-2]}")    # [60, 40]

# ===== 5. SLICING NESTED LIST =====
print("\n" + "=" * 50)
print("5. SLICING NESTED LIST")
print("=" * 50)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")
print(f"matrix[0]: {matrix[0]}")                  # [1, 2, 3]
print(f"matrix[1][2]: {matrix[1][2]}")           # 6
print(f"matrix[:2]: {matrix[:2]}")                # [[1, 2, 3], [4, 5, 6]]
print(f"matrix[0:2][1]: {matrix[0:2][1]}")       # [4, 5, 6]
print(f"matrix[0][1:3]: {matrix[0][1:3]}")       # [2, 3]

# ===== 6. MODIFIKASI DENGAN SLICING =====
print("\n" + "=" * 50)
print("6. MODIFIKASI LIST DENGAN SLICING")
print("=" * 50)

items = [1, 2, 3, 4, 5]
print(f"Items awal: {items}")

# Mengganti elemen dengan slicing
items[1:3] = [20, 30]
print(f"Setelah items[1:3] = [20, 30]: {items}")

# Menambah elemen dengan slicing
items[1:1] = [10, 15]
print(f"Setelah items[1:1] = [10, 15]: {items}")

# Menghapus elemen dengan slicing
items[2:4] = []
print(f"Setelah items[2:4] = []: {items}")

# ===== 7. KASUS PRAKTIS =====
print("\n" + "=" * 50)
print("7. KASUS PRAKTIS")
print("=" * 50)

# Mengambil nama file dari path
file_path = "d:/Documents/photo_2025_01.jpg"
filename = file_path.split('/')[-1]
name_only = filename[:-4]  # Hapus ekstensi
print(f"Path: {file_path}")
print(f"Filename: {filename}")
print(f"Nama tanpa ekstensi: {name_only}")

# Mengambil digit pertama dan terakhir dari number
number_str = "123456789"
print(f"\nNumber: {number_str}")
print(f"3 digit pertama: {number_str[:3]}")
print(f"3 digit terakhir: {number_str[-3:]}")
print(f"Middle (exclude first & last): {number_str[1:-1]}")

# Mengambil setengah dari list
values = list(range(1, 11))
mid = len(values) // 2
first_half = values[:mid]
second_half = values[mid:]
print(f"\nValues: {values}")
print(f"Separuh pertama: {first_half}")
print(f"Separuh kedua: {second_half}")

print("\n" + "=" * 50)
print("Slicing selesai!")
print("=" * 50)
