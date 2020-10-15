import os
# # result = dir(os)
# # print(result)

# # os.chdir('C:\\') c dizinine çeker.
# print(os.name) #işletim sistemi adı nv
# print(os.getcwd()) #dosyanın bulunduğu konum.
# #os.mkdir("newdirectory") #dizine klasör oluşturur.
# #os.chdir('../..') iki klasör üste yani C diskine geçer.
# # os.makedirs('newdirectory/yeni') #klasör içine klasör oluşturur.

# #klasörleri listeleme
# print(os.listdir())
# # os.chdir('..') bir üst dosyadaki klasörleri gösterir.
# # os.chdir('newdirectory')
# print(os.listdir())

# # for dosya in os.listdir():
# #     if dosya.endswith('.py'): py uzantılı dosyaları bulur.
# #         print(dosya)

# # print(os.stat("modul2.py")) #dosya hakkında bilgi verir. st_size bayt cinsinden boyutu.
# # import datetime
# # result = os.stat("modul2.py")
# # # print(result.st_size/1024) #kb cinsinden 
# # print(datetime.datetime.fromtimestamp(result.st_ctime)) #dosyanın oluşturulma zamanı saniye
# # print(datetime.datetime.fromtimestamp(result.st_atime)) #son erişilme tarihi.
# # print(datetime.datetime.fromtimestamp(result.st_mtime)) #değiştirilme tarihi.

# # os.system("notepad.exe") # not defterini açar

# # os.rename("newdirectory","yeniklasör") #klasör adı değişir
# # os.rmdir("silinecek") #removedir klasör silinir

# result = os.path.abspath("modul1.py") #klasör yolu gösterir.
# print(result)

# result = os.path.dirname(os.path.abspath("modul2.py")) #dizinini gösterir.
# result = os.path.exists("modul2.py") #dosya var mı dizinde.
# result = os.path.dirname("C:/Users/Deniz/Desktop/python/python_IleriSeviye/modul2.py")
# #result = os.path.join("") parçaları birleştirir.
# liste = os.path.splitext("modul2.py")
# print(result)
# print(liste[0])
# print(liste[1])