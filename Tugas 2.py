def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Meminta pengguna memasukkan suhu dalam Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Mengonversi ke Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Menampilkan hasil
print(f"Suhu dalam Celsius: {celsius:.2f}°C")

===task 2===
def cm_to_km(cm):
    return cm / 100000

def km_to_cm(km):
    return km * 100000

# Meminta pengguna memilih konversi
choice = input("Pilih konversi (1: cm ke km, 2: km ke cm): ")

if choice == "1":
    cm = float(input("Masukkan panjang dalam sentimeter: "))
    print(f"Hasil: {cm_to_km(cm)} km")
elif choice == "2":
    km = float(input("Masukkan panjang dalam kilometer: "))
    print(f"Hasil: {km_to_cm(km)} cm")
else:
    print("Pilihan tidak valid.")

===task 3===
def is_odd(n):
    return n % 2 != 0

def is_even(n):
    return n % 2 == 0

# Meminta pengguna memasukkan bilangan bulat
n = int(input("Masukkan bilangan bulat: "))

# Menentukan apakah bilangan tersebut genap atau ganjil
if is_even(n):
    print(f"{n} iseven: true")
else:
    print(f"{n} iseven: false")

===task 4===
def remove_first_occurrence(s, search):
    return s.replace(search, "", 1)

# Meminta pengguna memasukkan string dan string pencarian
string = input("Masukkan string: ")
search_string = input("Masukkan string pencarian: ")

# Menghapus kejadian pertama dari string pencarian
result = remove_first_occurrence(string, search_string)

# Menampilkan hasil
print(f"Hasil: {result}")

===task 5===
def is_palindrome(s):
    return s == s[::-1]

# Meminta pengguna memasukkan string
string = input("Masukkan string: ")

# Memeriksa apakah string adalah palindrom
if is_palindrome(string):
    print(f"{string} palindrome")
else:
    print(f"{string} bukan palindrome")

