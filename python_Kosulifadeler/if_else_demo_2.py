
sayi = int(input("sayı: "))
#sayi pozitif ve çift mi kontrol et
if (sayi>0):
    if (sayi%2==0):
        print("sayımız pozitif çifttir.")
    else:
        print("sayımız pozitif tektir.")
elif(sayi<0):
    if (sayi%2==0):
        print("sayımız negatif çifttir.")
    else:
        print("sayımız negatif tektir.")
else:
    print("Sayımız 0'dır. ")




