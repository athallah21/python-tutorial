game = input("Masukkan nama game: ")
print("Nama game Anda adalah", game)

while True:
    try:
        biner_input = int(input("Masukkan angka biner yang ingin dikirim ke server (1-9): "))
        if 1 <= biner_input <= 9:
            biner = bool(biner_input)
            print("HASIL biner =", biner, "type =", type(biner))
            break
        else:
            print("Mohon masukkan angka antara 1 hingga 9.")
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka antara 1 hingga 9.")

while True:
    try:
        angka = int(input("Masukkan angka yang ingin dikonversi ke boolean: "))
        bool_angka = bool(angka)
        print("HASIL konversi ke boolean:", bool_angka, "type =", type(bool_angka))
        break
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")
