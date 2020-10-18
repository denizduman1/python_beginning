import random

sayilar = [1,2,3,4,5]
sayisal_Loto = []
tahmin = []
i=0

while i<5:
    sayi = int(input("Tahmin Gir= "))
    tahmin.append(sayi)
    j = random.randint(0,4)
    sayisal_Loto.append(sayilar[j])
    i += 1
    
score = 0
for i in range(0,5):
    if(sayisal_Loto[i]==tahmin[i]):
        score += 1
    else:
        continue
    
print("Sayısal Loto Sonuçlar = ",end="")

j=0

for i in sayisal_Loto:
    if j<4:
        print(i,",",end=" ")
    else:
        print(i)
    j += 1

print("Scorunuz = "  , score , "/ 5")