game = input("Masukkan nama game: ")
print("nama game anda adalah ", game)

biner= bool(int(input("masukkan angka biner yang ingin dikirim ke server (1-9): ")))

if(biner==True):
    print("HASIL biner = ", biner , "type= ", type(biner))
elif(biner==False):
    num = int(input("masukkan angka  yang ingin dikonversi ke bool :"))
print("HASIL biner = ", bool(num) , "type= ", type(bool(num)))

