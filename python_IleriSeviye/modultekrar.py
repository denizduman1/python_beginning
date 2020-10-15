# import datetime

# # result = dir(datetime)

# result = datetime.datetime.now()
# # result = result.year
# simdi = datetime.datetime.now()
# result = datetime.datetime.ctime(result)
# result = datetime.datetime.strftime(datetime.datetime.now(),'%Y %B %A %H %M %S') #parçalara ayırır.
# t ='15 October 2020'
# result = datetime.datetime.strptime(t,'%d %B %Y') #girilen string tarihi digital tarihe çevirir.
# result = datetime.datetime.ctime(result) #digital tarihi string tarihe çevirir.
# gun,ay,yil = t.split()
# print(gun,ay,yil)
# result = datetime.datetime.timestamp(simdi)
# result = datetime.datetime.fromtimestamp(result)
# print(result)
# print("---------------")

# result = simdi + datetime.timedelta(minutes=6,days=2) #zaman ileriye alma.
# print(result)
# print(result - simdi)

import os 

result = dir(os)
result = os.name #işletim sistem adı
result = os.getcwd()#bulunduğun dizin adı
#os.mkdir("tekrar") #dizine klasör ekleme
#os.chdir("..") #bir üst klasöre çeker.
# os.chdir("../python_Fonksiyonlar")
print(result)
# os.makedirs('tekrar/yeni') klasör içine klasör ekleme
print(os.listdir())#dizindeki klasörleri sıralar.
#os.chdir("..")
for dosya in os.listdir():
    if(dosya.endswith(".py")): #uzantısı py olan dosyaları getirt.
        print(dosya)
    # else: 
    #     print(dosya)
os.chdir(os.getcwd())
# print(os.stat("modultekrar.py"))
import datetime
print(datetime.datetime.fromtimestamp(os.stat("modultekrar.py").st_ctime))
#os.system("notepad.exe")
os.chdir(os.getcwd()+'/günceltekrar')
# os.rename("yeni","güncelyeni")
os.chdir("..")
result = os.path.abspath("modultekrar.py")
print(result)
#os.rmdir("klasör") siler.