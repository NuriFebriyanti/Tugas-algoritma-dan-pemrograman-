import random


# Membuat list dengan 100 angka acak antara 1 - 399
numbers = (random.randint(1, 399) for _ in range(100))

# Menyimpan angka-angka ke dalam file
with open('angka_acak.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')

        # Membuka file untuk dibaca
with open('angka_acak.txt', 'r') as file:
    # Membaca setiap baris dalam file
    for line in file:
        # Mengambil angka dari setiap baris dan mengubahnya menjadi integer
        number = int(line.strip())
        
        # Menampilkan apakah angka tersebut ganjil atau genap
        if number % 2 == 0:
            print(f'{number} adalah angka genap.')
        else:
            print(f'{number} adalah angka ganjil.')