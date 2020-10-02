'''
ad = input("isim: ")
yas = int(input("yaş: "))
egitim = input("eğitiminiz: ")
result = (yas>=18) and (egitim=='üniversite' or egitim=='lise')
if result:
    print(f"sayın {ad} ehliyet alma durumunuz: başarılı")
else: 
    print(f"sayın {ad} ehliyet alma durumunuz: başarısız")
''' 
'''
quiz1 = float(input("quiz notunuzu giriniz: "))
exam1 = float(input("exam1 notunuzu giriniz: "))
exam2 = float(input("exam2 notunuzu giriniz: "))

avarage = ((quiz1+exam1+exam2)/3)

if (avarage>0 and avarage<24.1):       
    print(f"ortalamanız:{avarage} 0")
elif (avarage>24.1 and avarage<44.1):
    print(f"ortalamanız:{avarage} 1")
elif (avarage>44.1 and avarage<54.1):
    print(f"ortalamanız:{avarage} 2")
elif (avarage>54.1 and avarage<69.1):
    print(f"ortalamanız:{avarage} 3")
elif (avarage>69.1 and avarage<84.1):
    print(f"ortalamanız:{avarage} 4")
elif (avarage>84.1 and avarage<100.1):
    print(f"ortalamanız:{avarage} 5")
else:
    print("başarısız not girişi.")
'''
import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ') #years/months/days
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2])) #tarih objesi hazırlandı.
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print('1.servis aralığı')
elif days>365 and days <=365*2:
    print("2.servis aralığı")
elif days>365*2 and days <=365*3:
    print("3.servis aralığı")
else:
    print("hatalı süre")