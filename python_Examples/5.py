# import random

# sayilar = [1,2,3,4,5]
# sayisal_Loto = []
# tahmin = []
# i=0

# while i<5:
#     sayi = int(input("Tahmin Gir= "))
#     tahmin.append(sayi)
#     j = random.randint(0,4)
#     sayisal_Loto.append(sayilar[j])
#     i += 1
    
# score = 0
# for i in range(0,5):
#     if(sayisal_Loto[i]==tahmin[i]):
#         score += 1
#     else:
#         continue
    
# print("Sayısal Loto Sonuçlar = ",end="")

# j=0

# for i in sayisal_Loto:
#     if j<4:
#         print(i,",",end=" ")
#     else:
#         print(i)
#     j += 1

# print("Scorunuz = "  , score , "/ 5")

# sayi = int(input("Sayı Gir = "))
# i = 1
# toplam = 0
# while i<sayi:
#     if(sayi%i==0):
#         toplam = toplam + i
#     i = i + 1

# if(toplam == sayi):
#     print("Sayınız Mükemmel Sayıdır.")
# else: 
#     print("Sayınız Mükemmel Sayı Değildir.")

# bas_sayi = int(input("başlangıç sayı Gir = "))
# son_sayi = int(input("son sayı Gir = "))

# for i in range(bas_sayi,son_sayi):
#     j = 1
#     toplam = 0
#     while j < i :
#         if(i%j==0):  
#             toplam = toplam + j
#         j = j + 1
#     if(toplam == i):
#         print(i,end=" ")

# liste = []
# sayi = int(input("Sayi = "))
# i = 1
# while True:
#     i = i * 10
#     a = sayi % (i) 
#     if (a>0):
#         liste.append((a//(i//10)))
#     else:
#         break
#     sayi = sayi - a 

# liste.reverse()
# toplam = 0
# print(liste)
# for i in liste:
#     toplam = toplam +  (i ** (len(liste)))
# print(toplam)