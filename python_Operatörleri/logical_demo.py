'''
girilen_Sayi = int(input("Sayı gir: "))
kontrol = girilen_Sayi<100 and girilen_Sayi>0
print(kontrol)
girilen_Sayi = int(input("Bir başka sayı gir: "))
kontrol = girilen_Sayi%2== 0 and girilen_Sayi>0
print(kontrol)
print("----------------")
vize1 = float(input("1.Vize= "))
vize2 = float(input("2.Vize= "))
final = float(input("Final= "))
avarage = (((vize1+vize2)/2)*0.6 + final*0.4)
result = (((avarage>50) or (avarage==50)) and ((final>50)or(final==50))) or ((final>70) or (final==70))
print(f"ortalamanız: {avarage} ve geçme durumunuz: {result}")
print("----------------")
'''

print("Kullanıcı Bilgilerini Giriniz..")
isim = input("İsim: ")
kilo = float(input("Kilo: "))
boy  = float(input("Boy: ")) # 1.75 şeklinde gir

users = {
    1: {
        'isim': isim,
        'kilo': kilo,
        'boy': boy
    }
}
print(users)
index = (kilo) / (boy**2) 
result_zayif =  index < 18.4
result_normal = (((users[1]['kilo'])/(boy**2)) < 24.9) and (((users[1]['kilo'])/(boy**2)) > 18.5)
result_fazla = (((users[1]['kilo'])/(boy**2)) < 29.9) and (((users[1]['kilo'])/(boy**2)) > 25.0)
result_sisman = (((users[1]['kilo'])/(boy**2)) < 34.9) and (((users[1]['kilo'])/(boy**2)) > 30.0)
print(f"Sayın {users[1]['isim']}, kilonuz: {users[1]['kilo']} ve kilo indeksinize göre zayıfsınız: {result_zayif}")
print(f"Sayın {users[1]['isim']}, kilonuz: {users[1]['kilo']} ve kilo indeksinize göre normalsiniz: {result_normal}")
print(f"Sayın {users[1]['isim']}, kilonuz: {users[1]['kilo']} ve kilo indeksinize göre fazlasınız: {result_fazla}")
print(f"Sayın {users[1]['isim']}, kilonuz: {users[1]['kilo']} ve kilo indeksinize göre obezsiniz: {result_sisman}")