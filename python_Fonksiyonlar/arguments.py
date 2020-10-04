'''
def changeName(n):
    n= 'ada'

name = 'yiğit'
changeName(name)
print(name)
'''
'''
def change(n): #adres gidiyor.
    n[0]='İstanbul'
    
    
sehirler = ['Ankara','İzmir']
change(sehirler)

print(sehirler)
'''
'''
def add(a,b,c=0):  # *params sınırsız değişken oluşturabiliriz. params tuple list oluşturur.
    return sum((a,b,c))

print(add(53,6))
print(add(53,6,1))

def private_add(*degisken):
    sum = 0
    for n in degisken:
        sum = sum + n
    print(sum)
    
private_add(1,2,3,4,5)
print("****************")

a = [1,2,3]
b = a[0:2] #diziyi kopyaladı.
c = a #a nın referansını tutar dolayısıyla oynamalar a yı da etkiler.
c[1] =3 
print(b)
print(a)

print("****************")

def displayUser(**dic):
    for key,val in dic.items():
        print('{} is {}'.format(key,val))

displayUser(name='deniz',no=556)
displayUser(name='derya',ogrenciMi = True , yas = 18)

print("****************")
'''

def myfunc(a,b,*c,**d):
    print("{} integer değer".format(a))
    print("{} string değer".format(b))
    print("{} tuple list".format(c))
    print("{} dictionary".format(d))

myfunc(5,"a",11,12,13,14,15,16,17,18,19,20,departmant="Bilgisayar Mühendisliği",age = 22)

'''
def func(**a):
    print(a)
func(key=1,isim='deniz')
'''