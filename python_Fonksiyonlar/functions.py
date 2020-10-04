def sayHello(name='default'): #fonksiyon def ile tanımlanır.
    print("sayHello çalıştı isim:"+name)

sayHello("Deniz")
sayHello() #default çalışır.

def sayHello_Upper(name='default'):
    return "Hello " + name.upper()

print(sayHello_Upper("Deniz"))

def sayiTopla(sayi1,sayi2):
    print(f"sayi1: {sayi1}")
    return sayi1+sayi2

result = sayiTopla(sayi2=10,sayi1=20)
print(result)
print("----------")
def YasHesapla(dogumYil):
    return(2020-dogumYil)

ageDeniz = YasHesapla(1998)
print(ageDeniz)
