'''
sayilar = [1,3,5,7,9,12,19,21]
toplam = 0
for sayi in sayilar:
    if (sayi%3==0):
        print(f"3'ün katı sayilar: {sayi}")
for sayi in sayilar:
    toplam = sayi + toplam
    
print ("toplamı: ",toplam)

for sayi in sayilar:
    if(sayi%2==1):
        print("tek sayıların karesi",sayi**2)
'''
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)
        
urunler = [
   {
        'name' : 'SamsungS6',
        'price' : 3000    
    },
      {
        'name' : 'SamsungS7',
        'price' : 4000    
    },
        {
        'name' : 'SamsungS8',
        'price' : 5000    
    },
          {
        'name' : 'SamsungS9',
        'price' : 6000    
    },
]

sonuc = 0
for urun in urunler:
    sonuc=(urun['price'])+sonuc
print(sonuc)

for urun in urunler: 
    if (urun['price']<=5000):
        print(urun['name'],urun['price'])