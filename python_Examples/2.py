# liste = [1,2,3,4,5,6,7,8,9,10]

# tekSayilar = []
# ciftSayilar = []

# for x in liste:
#     if(x%2==0):
#         ciftSayilar.append(x)
#     else:
#         tekSayilar.append(x)

# print("Tek Sayılar:",tekSayilar)
# print("Çift Sayılar:",ciftSayilar)

# 1 1 2 3 5 8

# fibonacciSayisi = int(input("fibonacci sayısı: "))
# ilkEleman = 1
# ikinciEleman = 1
# toplam = 0
# if(fibonacciSayisi==0):print(fibonacciSayisi)
# else:
#     while toplam<=fibonacciSayisi: #1 2 3 
#         ilkEleman = toplam         #ilk eleman = 1 toplam = 0 ikinci eleman = 1
#         toplam = ikinciEleman + ilkEleman #ilk eleman = 1 toplam = 2 ikinci eleman = 1
#         ikinciEleman = ilkEleman  #ilk eleman = 1 toplam = 2 ikinci eleman =1
#         if(toplam>fibonacciSayisi):
#             break
#         print(toplam) #12


# while True:
#     islem = input("İşleminizi girin: ")
#     if(islem=="exit"): break
#     elif(islem not in "+-*/"): print("hatalı işlem girişi")
#     else:
#         sayi1 = int(input("sayı1:"))
#         sayi2 = int(input("sayı2:"))
#         print("işleminiz:",islem)
#         if(islem=="+") : print("sonuc= ",(sayi1+sayi2))
#         elif(islem=="-") : print("sonuc= ",(sayi1-sayi2))
#         elif(islem=="*") : print("sonuc= ",(sayi1*sayi2))
#         elif(islem=="/") : print("sonuc= ",(sayi1/sayi2))
#         else: 
#             print("hatalı işlem girişi")

#takım = fb oyun=ali 
#takım = gs oyun=ali 
#takım = bjk oyun=ali 
#takım = fb bjk gs 
#oyuncular = ali ali ali

# x=0
# # liste=[{
# #     'takım':"boş",
# #     'oyuncu':"boş"
# # }]

# liste=[{'1':{}}] 
# x = 0

# while x<3 : 
#    takim = input("takım:") 
#    oyuncu = input("oyuncu:") 
#    id = input("id:")
#    liste.append(
#    {
#        id:
#        {
#        'takim':takim,
#        'oyuncu':oyuncu
#        }
#        }
#    )
#    x = x + 1

# liste.pop(0)

# print("----------")
    
    
# print("takımlar..")

# for x in liste:
#     print(x['takim'])
    
# print("----------")

# print("oyuncular..")

# for x in liste:
#     print(x['oyuncu'])    