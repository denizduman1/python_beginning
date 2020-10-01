sayi = int(input("1.sayi: "))
sayi2 = int(input("2.sayi: "))

result = (sayi > sayi2)
print(f'sayi1: {sayi} sayi2: {sayi2} den büyüktür: {result}')

vize1 = float(input("1.vize: "))
vize2 = float(input("2.vize: "))
final = float(input("final: "))

avarage = ((vize1+vize2)/2*0.6) + (final*0.4)  
result = avarage >= 50 
print(f'ortalamanız: {avarage} dersi geçti: {result}')

x  = int(input ("Sayı gir: "))
tekCift = (x %2 == 0)
print(f"sayınız çift mi= {tekCift}")


gecerli_email = 'example_email@gmail.com'
gecerli_sifre = '123456789'

try_email=  input("email gir: ")
try_sifre = input("şifreni gir: ")

result = (gecerli_email==try_email) and (gecerli_sifre == try_sifre)

print(f"Oturum açma durumunuz: {result}")
