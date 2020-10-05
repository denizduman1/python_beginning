#Bankamatik Uygulaması
IbrahimHesap = {
    'ad' : 'İbrahim Duman',
    'hesapNo' : '13245678',
    'bakiye' : 3000,
    'ekHesap' : 2000
}
DenizHesap = {
    'ad' : 'Deniz Duman',
    'hesapNo' : '97984678',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap["ad"]}')
    if hesap['bakiye']>=miktar : 
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap ['ekHesap']
        if toplam >= miktar:
            ekhesapKullanimi = input('ek hesap kullanılsın mı (e/h):')
            if ekhesapKullanimi == 'e' :
                bakiye = hesap['bakiye']
                ekhesapKullanilacakMiktar = miktar - bakiye
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print("paranızı alabilirsiniz.") 
            else:
                print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır.')       
        else:
            print('üzgünüz bakiye yetersiz.')
            bakiyeSorgula(DenizHesap)
            
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Ek hesabınızda ise {hesap['ekHesap']} TL vardır.")
    
bakiyeSorgula(DenizHesap)
paraCek(DenizHesap,4000)
bakiyeSorgula(DenizHesap)
paraCek(DenizHesap,500)
bakiyeSorgula(DenizHesap)
