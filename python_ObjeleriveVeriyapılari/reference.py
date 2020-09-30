x = 5
y = 25 

x = y 
y = 10
print(x,y)

#reference types => list,class

a = ["apple","cherry"]
b = ["apple","cherry"]

a = b #adresler eşitleniyor o yüzden değişiklikler ikisine de kapsıyor.
b[0] = 'grape'
print(a,b) # ikisi de değişiyor.
a.clear()
print(a,b)

#referansın amacı: aynı verilerin kopyalanmasında çift kalıp belleği yormasın diye tercih ediliyor.
