'''
sayilar = [1,3,5,7,9,12,19,21]

sayi = 0
while sayi < len(sayilar) : 
    print(sayilar[sayi])
    sayi = sayi + 1
'''
'''
start = int(input("start:"))
end = int(input("end:"))

while (start<=end):
    if(start%2==1):
        print("tek sayımız:",start)
    start+=1
'''
'''
sayi=100
while sayi > 1 :
    print(sayi)
    sayi -= 1
'''
'''
numbers = []

sayi=0
while (sayi<5):
    numbers.append(int(input("sayi gir:"))) 
    sayi+=1
numbers.sort()
print(numbers)
'''
i = 0
urunler = []
name = ''
price = 0
adet = int(input("kaç adet ürün gireceksiniz:"))

while (i < adet):
    name = input("name:")
    price = int(input("fiyat:"))
    urunler.append({
        'name' : name,
        'price' : price
    })
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")