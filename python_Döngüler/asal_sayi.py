sayi = int(input("sayınız:"))
asalmi = True
if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0): #kalan kontrol etme
        asalmi = False
        break
    i+=1
        
if asalmi:
    print('sayi asaldır.')
else:
    print("asal değildir.")
