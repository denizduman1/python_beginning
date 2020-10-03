name = 'Lionel Messi'
'''
for letter in name: 
    if letter == 'e':
        continue #yukardaki şart hariç devam et. #break olursa döngü şart bittiği anda durur.
    print(letter)
'''
sayi = 10
num = 0

while num < sayi: 
    num += 1 #aşağıda olursa döngü takılı kalır.
    if num==3:
        continue #başa çeker.
    print(num)
  
sayi=0
toplam=0

while sayi<10:
    sayi+=1
    if sayi%2==0:
        continue
    toplam = sayi + toplam
print(toplam)