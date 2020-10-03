import random
sayi = random.randint(1,100) #int sayi döndürür.
hp = int(input("kaç can istersiniz:"))
deger = 100 / hp
print(sayi)
while hp>0:
    tahmin = int(input("tahmin et:"))
    if tahmin<sayi:
        hp -= 1
        if hp==0:
            print("game over")
        else:
            print("yukarı")
    elif tahmin>sayi:
        hp -= 1
        if hp==0:
            print("game over")
        else:
            print("aşağı")
    else: 
        points = deger * hp 
        print(f"tebrikler {sayi} sayisiniz buldunuz. Puanınız: {points}")
        break