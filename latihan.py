nilai_a = 12 
nilai_b = "POLIWANGI"
nilai_c= 21
print("hello world")
print("nilai b bertipe =", type(nilai_b))
print ("nilai a ", nilai_a, "bertipe", type(nilai_a))


##belajar casting
## Merubah dari satu tipe ke tipe lainnya
## Integer ke data lain nya (String, Float)
# print(int(nilai_b)) #error karena tidak bisa di cast ke integer
try:
    nilai_bool= bool(nilai_c)
    print("nilai bool= " ,nilai_bool,"type =", type(nilai_bool)) 
#menampilkan tipe data yang dihasil
    nilai_float= float(nilai_a)
    print("nilai float = " ,nilai_float,"type =", type(nilai_float)) 
    data_string=int(nilai_b) 
    print("data_string = ", nilai_b , "type = ", type(data_string))
except  ValueError :
    print("data tidak dpat diubah ke  integer")  
#mengubah string menjadi integer
nilai_d= 0
nilai_false= bool(nilai_d)
print("hasil = "  , nilai_false, "type = ", type(nilai_false)) 
#boolean hanya mempunyai dua isi salah
#boolean hanya mempunyai dua isi salah satunya True atau

## float ke data lain
float_1=5.6789
int_1= int(float_1)
print("hasil int_1 = ", int_1 ,"type = "  , type(int_1))

str_1=str(float_1)
print("hasil str 1=", str_1, "type = ", type(str_1))

bool_1= bool(float_1)
print("hasil bool_1 = ", float_1, "type = ", type(bool_1))

## string kedata lain
data_str= "Halo Dunia"
try:
    angka_str= int(data_str)
    bool_str= bool(data_str)
    float_str= float(data_str)
    print("hasil angka_str = "  , angka_str, "type = " , type(angka_str))
    print("hasil bool_str = " , bool_str, "type = " , type(bool_str))
    print("hasil float_str = " , float_str, "type = " , type(float_str))
except  ValueError :
    print("data tidak dpat diubah ke data ini ")

## bool ke data lain
data_bool= True
try:
    data_int= int(data_bool)
    data_float= float(data_bool)
    data_str= str(data_bool)
    print("hasil data_int = "  , data_int, "type = " , type(data_int))
    print("hasil data_float = " , data_float, "type = " , type(data_float))
    print("hasil  data_str = " , data_str, "type = " , type(data_str))
except ValueError :
    print("data tidak dpat diubah ke data ini ")