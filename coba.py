import random

def main():
    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100. Coba tebak!")

    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        guess = int(input("Masukkan tebakan Anda: "))
        guesses_taken += 1

        if guess < secret_number:
            print("Tebakan Anda terlalu rendah. Coba lagi!")
        elif guess > secret_number:
            print("Tebakan Anda terlalu tinggi. Coba lagi!")
        else:
            print(f"Selamat! Anda berhasil menebak angka yang benar dalam {guesses_taken} tebakan!")
            break

if __name__ == "__main__":
    main()
