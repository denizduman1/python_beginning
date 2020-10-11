def dosyaOlustur(dosyaAdi):
    open(dosyaAdi+".txt","x",encoding="utf-8")
        
def arabaGir(marka,model,fiyat):
    with open("arabalar.txt","a",encoding="utf-8") as file: 
        file.write(marka+":"+model+":"+fiyat+"\n")
    
def arabalariGoster():
    with open("arabalar.txt","r",encoding="utf-8") as file:
        for satir in file: 
            liste = satir
            liste = liste.split(":")
            print("marka:",liste[0]," model:",liste[1]," fiyat:",liste[2])

def yuzBinArabaGoster():
    with open("arabalar.txt","r",encoding="utf-8") as file:
        for satir in file:
            liste = satir
            liste = liste.split(":")
            if(int(liste[2])>100000):
                print("marka:",liste[0]," model:",liste[1]," fiyat:",liste[2])    

# def arabaGuncelle():
#     with open("arabalar.txt","r+",encoding="utf-8") as file:
#         marka = input("Güncelleyeceğiniz arabanın markası:")
#         secim = input("Güncelleyeceğiniz özellik(model/fiyat = 0/1)")
#         for satir in file:
#             liste = satir
#             liste = liste.split(":")
#             for i in range (0,500):
#                 if(liste[0]==marka):
#                     if secim:
#                         fiyat = input("yeni fiyat:")
#                         liste[2] = fiyat
#                         file.write(liste[2])
#                         break
#                     else:
#                         model = input("yeni model:")
#                         liste[1] = model
#                 i = i + 1 
        
while True:

    print("1-Dosya Oluştur")
    print("2-Yeni Araba Ekle")
    print("3-Arabaları Göster")
    print("4-Fiyatı 100000'den büyük olan Arabaları Göster")
    print("5-Güncelleme Yap")
    print("6-Çıkış Yap.")
    secim = input("Seçim:")

    if secim == "1": 
        try:
            ad = input("Dosya adını gir:")
            dosyaOlustur(ad)
        except:
            print("daha önce böyle bir dosya oluşturulmuş.")

    elif secim == "2": 
        marka = input("Marka:")
        model = input("Model(YIL OLARAK GİRİN):")
        fiyat = input("Fiyat:")
        arabaGir(marka,model,fiyat)
    
    elif secim == "3":
        arabalariGoster()
    
    elif secim == "4":
        yuzBinArabaGoster()
    
    elif secim == "5":
        # arabaGuncelle()
    
    else : 
        break
