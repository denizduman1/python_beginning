'''
ogrenciler = {
    '120': {
        'ad' : 'Ali',
        'soyad' : 'Yılmaz',
        'telefon' : '532 000 00 01'
    },
    '125': {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'
    },
    '128': {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 03'
    }
}
'''
ogrenciler ={}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
telephone = input("Öğrenci tel: ")

'''ogrenciler[number] = {
    'ad':name,
    'soyad':surname,
    'telefon':telephone
}'''

ogrenciler = {
number:
{
    'ad':name,
    'soyad':surname,
    'telefon':telephone
}
}


name='Derya'
surname='Duman'
number = '345'
telephone = '15604654654'

ogrenciler.update ({
number:
{
    'ad':name,
    'soyad':surname,
    'telefon':telephone
}
})

print(ogrenciler)
print("------------")
numara = input("aradığınız num gir: ")
print(ogrenciler[numara])