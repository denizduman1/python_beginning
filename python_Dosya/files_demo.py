def notHesapla(satir):
    # satir = satir[:-1] #aradaki boşlukları sil
    liste = satir.split(":")
    ogrenciAdi= liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+not2+not3)/3
    if ortalama>=70:
        basariDurumu = "başarılı"
    else:
        basariDurumu = "başarısız"
    return ogrenciAdi+": " + basariDurumu + "\n"

def ortalamalari_Oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file: #satır satır okur.
            print(notHesapla(satir))
 
def notGir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
         file.write(ad+' '+soyad+':' + not1 + ',' + not2 + "," + not3 + '\n')
    
def notlari_KayitEt():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(notHesapla(i)) #satır satır yazar.
    with open("sinav_ortalama.txt","w",encoding='utf-8') as file2:
        for i in liste:
            file2.write(i)
        

while True:
    islem = input("1-Notları Oku \n2-Not Gir \n3-Notları Kayıt Et\n4-Çıkış yap.\n")
    if islem == '1':
        ortalamalari_Oku()
    elif islem == '2':
        notGir()
    elif islem == '3':
        notlari_KayitEt()
    else:
        break