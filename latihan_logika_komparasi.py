## area rentang angka

inputUser= float(input("masukkan angka kurang dari 3 atau lebih dari 10  : "))

iskurangdari= (inputUser < 3)
print("kurang dari 3= ",iskurangdari)
islebihdari =(inputUser > 10)
print("lebih dari 10= ",islebihdari)

isCorrert= iskurangdari or islebihdari
if(isCorrert):
    print("Angka yang anda masukkan berada diantara keduanya")
else:(isCorrert!= iskurangdari or islebihdari)
print("Angka yang anda masukkan tidak berada diantara keduanya")

## irisan
inputUser= float(input("masukkan angka lebih dari 3 dan kurang  dari 10  : "))
ismore= inputUser>3
print("lebih dari 3= ",ismore)
isless= inputUser<10
print("kurang dari 10= ",isless)
isIrisan= ismore and isless
if(isIrisan):
    print("Angka yang anda masukkan berada diantara keduanya")
else:(isIrisan!= ismore and isless)
print("Angka yang anda masukkan tidak berada diantara keduanya")