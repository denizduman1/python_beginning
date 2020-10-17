# class Takim:
#     yildizSayisi = 0
#     def __init__(self,kulup_Isim,kurulus_Yili,sampiyonluk_Sayisi,kulup_Baskan): #method
#         self.kulup_Isim = kulup_Isim
#         self.kurulus_Yili = kurulus_Yili
#         self.sampiyonluk_Sayisi = sampiyonluk_Sayisi
#         self.kulup_Baskan = kulup_Baskan
#     def display(self):
#         return self.kulup_Isim+" "+self.kulup_Baskan
#     def arttir(self):
#         self.sampiyonluk_Sayisi += 1
#     def azalt(self):
#         self.sampiyonluk_Sayisi -= 2
#     def yildizGoster(self):
#         self.yildizSayisi = self.sampiyonluk_Sayisi // 5
        
   
# takim1 = Takim('TS','1967',6,"Ahmet Ağaoğlu") #object
# takim2 = Takim('FB','1907',19,"Ali KOÇ")
# print(takim1.yildizSayisi)
# takim1.yildizGoster()
# print(takim1.yildizSayisi)
# print("-----------------")
# takim2.yildizGoster()
# print(takim2.yildizSayisi)
# takim1.azalt()
# print(takim1.sampiyonluk_Sayisi)
# takim1.sampiyonluk_Sayisi = 7
# print(takim1.sampiyonluk_Sayisi)
# goster = takim1.display()
# print(goster)
# print("-----------")
# takim1.arttir()
# print(takim1.sampiyonluk_Sayisi)

# class Hayvan:
#     canliMi = True
#     fotosentezMi = False
#     nefesAlirMi = True
#     def __init__(self):
#         print("Hayvan Sınıfı")
#     def hayvanozel(self):
#         print("canlılardır.")

# class Kedi(Hayvan):
#     ses = "miyav"
#     def __init__(self): #override
#         print("ben bir kediyim.")
#         Hayvan.__init__(self)
    
# class Kopek(Hayvan):
#     ses = "hav hav"
    

# k1 = Kedi()


# class Ogrenci:
#     __adi = ""
#     num = ""
#     def adDegistir(self,adi):
#         self.__adi = adi
#     def adGoster(self):
#         return self.__adi
    

# o1 = Ogrenci()
# o1.num = "123"
# print(o1.num)
# o1.adDegistir("Tahsin")

# isim = o1.adGoster()
# print(isim)

# class A: 
#     def __str__(self):
#         return "A Sınıfı Burası"

# a1 = A()
# print(a1.__str__())