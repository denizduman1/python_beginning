x,y,z = 2,5,107 #atama
numbers = 1,5,7,10,6 #tuple

a = input("ilksayi: ") #veriler inputtan string olarak geliyor.önce inte dönüştürmemiz lazım
b = input("ikincisayi: ")
sonuc = (int(a)*int(b))-(x+y+z)
print("sonuc: ",sonuc)
print("-------------")
sonuc = y / x
print(sonuc)
mod_al = (x+y+z)%3
print("mod",mod_al)
print(y**x)

x,*y,z = numbers
print(x,y,z)
print("z küp: ",z**3)
print(y[0]+y[1]+y[2])