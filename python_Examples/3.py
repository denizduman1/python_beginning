# def topla(sayi1,sayi2):
#     return sayi1+sayi2

# def cikar(sayi1,sayi2):
#     return  sayi1-sayi2

# def carp(sayi1,sayi2):
#     return sayi1*sayi2

# def bol(sayi1,sayi2):
#     return sayi1/sayi2


# while True:
#     islem = input("işlem: ")
#     if(islem=="exit"):
#         print("hesap makinesi kapatılıyor..")
#         break
#     else:
#         sayi1 = int(input("sayı1:"))
#         sayi2 = int(input("sayı2:"))
#         if(islem=="+"):
#             sonuc = topla(sayi1,sayi2)
#             print("sonuç:",sonuc)
#         elif(islem=="-"):
#             sonuc = cikar(sayi1,sayi2)
#             print("sonuç:",sonuc)
#         elif(islem=="*"):
#             sonuc = carp(sayi1,sayi2)
#             print("sonuç:",sonuc)
#         elif(islem=="/"):
#             sonuc = bol(sayi1,sayi2)
#             print("sonuç:",sonuc)
#         else:
#             print("hatalı işlem girişi")

# def isimGoster(ad,soyad):
#     return ad + " " + soyad

# ad = input("adınız: ")
# soyad = input("soyadınız: ")

# adSoyad = isimGoster(ad,soyad)
# print(adSoyad)


# def sozlukOlustur(marka,model,fiyat,cikisTarihi="2020"):
#     sozluk = {} 
#     sozluk.update(
#         {
#           marka: {
#              'model' : model,
#              'fiyat' : fiyat,
#              'cikisTarihi' : cikisTarihi
#           }
#         }
#     )
#     return sozluk

# def sozlukOku(marka,sozluk):
#     for key,val in sozluk.items():
#         if(key==marka):
#             print("key:",key, "model:" ,val['model'],"fiyat" , val['fiyat'] , "Çıkış Tarihi:",val["cikisTarihi"])
#         else:
#             continue
# x= 0
# a = {}

# while x<2:
#     marka = input("marka:")
#     model = input("model:")
#     fiyat = int(input("fiyat:"))
#     a.update(sozlukOlustur(marka,model,fiyat))
#     #a = sozluk
#     x = x+1
# print(a)
# print("---------------------")

# id = input("Bakmak istediğiniz marka:")
# sozlukOku(id,a)

# def func(no,ad,gorev):
#     return "enesburak" + no + ad

# a = func(gorev="admin",ad="Tahsin",no="123")

# print("-------")
# print(a)
 
            

# def anaFonksiyon(func):
#     print("ana fonksiyon çalıştırılıyor.")
#     print("-----------------------------")
#     def altFonksiyon(liste):
#         print("alt fonksiyon çalıştırılıyor.")
#         print("-----------------------------")
#         func(liste)
#         print("-----------------------------")
#     return altFonksiyon   
        

# @anaFonksiyon
# def tekSayilariCikart(liste):
#     for x in liste:
#         if(x%2==1):
#             print("tek sayilar: ", x , end=" ") 
#     print() 
# @anaFonksiyon
# def ciftSayilariCikart(liste):
#     for x in liste:
#         if(x%2==0):
#             print("çift sayilar: ", x , end=" ")     
#     print()        
# liste = [0,7,5,1,3,11,33,77,95,47,2,8,40]
# tekSayilariCikart(liste)
# ciftSayilariCikart(liste)