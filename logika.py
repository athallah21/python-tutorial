## operasi logika atau boolean
## not , or , and, xor

print("========NOT========")
b = False
c  = True
d =  not b 
e= not c

print("data b =",b)
print("data c =",c)
print ("data d= ", d)
print ("data e=",e )

## or (jika salah satu true maka hasilnya true )
print("========OR==========")
e= False
f= True
g= e or f
print( e  ," OR ",f," = ", g )
a =False
b =False
c = a or b
print( a  ," OR ",b," = ", c )

## and (jika salah satu false maka hasinya akan false)
print("========AND==========")
e= False
f= True
g= e and f
print( e  ," AND ",f," = ", g )
a =True
b =True
c = a and b
print( a  ," AND ",b," = ", c )

## XOR (jika sama sama true atau false maka hasilnya false)
print("========AND==========")
e= False
f= True
g= e ^ f
print( e  ," XOR ",f," = ", g )
a =True
b =True
c = a ^ b
print( a  ," XOR ",b," = ", c )




