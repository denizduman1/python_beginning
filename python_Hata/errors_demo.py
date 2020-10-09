# # # liste = ["1","2","5a","10b","abc","10","50"]
 
# # # for x in liste:
# # #     try:
# # #         result = int(x)   
# # #         print(result)
# # #     except ValueError:
# # #         continue

# # while True:
# #     sayi = input('sayı: ')
# #     if sayi == 'q':
# #         break
# #     try:
# #         result = float(sayi)
# #         print("girdiğiniz sayı:",result)
# #     except ValueError:
# #         print("geçersiz sayi")
# #         continue

# turkce_karakter = "şçğüöıİ"

# try:
#     parola = input("parola:")
#     for x in turkce_karakter:
#         if(x in parola):
#             raise Exception("türkçe karakter var.karakter:",x)    
#         else:
#             continue
#     print("parolanız:",parola)
# except Exception as e: #raisede verdiğimiz excepitonu yakalar.
#     print("hatanız:",e)


def faktoriyelAl(faktoriyelAlinacakSayi):
        result = int(faktoriyelAlinacakSayi)
        sonuc = 1
        if result < 0 : 
            raise ValueError(result," sayısı"," negatif sayıdır girilemez.")
        else:    
            for x in range(1,result+1):
                sonuc = sonuc * x
            return sonuc

for x in [5,10,20,-3,"10a","-5"]:
    try:
        y = faktoriyelAl(x)
        print(x," sayısının faktoriyeli: ",y)
    except Exception as e:
        print(e)
        continue
