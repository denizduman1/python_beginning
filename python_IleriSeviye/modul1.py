# from datetime import datetime
# from datetime import date
# from datetime import time

from datetime import datetime

# result = dir(datetime)
# print(result)

# print(datetime.now())
# result = datetime.now().day
# print(result)
# print(datetime.now().year)
# print(datetime.now().hour)
# print(datetime.now().minute)
# simdi = datetime.today()
# result = datetime.ctime(datetime.now()) #daha açık gösteriyor.(ay gün adı)
# print(result)
# result = datetime.strftime(datetime.now(),'%Y') #yıl
# result = datetime.strftime(datetime.now(),'%X') #saat
# result = datetime.strftime(datetime.now(),'%d') #gün
# result = datetime.strftime(datetime.now(),'%A') #gün adıyla
# result = datetime.strftime(datetime.now(),'%Y %B %A') #yıl ay gün adıyla
# print(result)

# t = '21 Nisan 2019'
# gun,ay,yil = t.split()
# print(gun,ay)

# x = '23 April 1920 hour 10:12:30'
# dt = datetime.strptime(x,'%d %B %Y hour %H:%M:%S') #verdiğimiz bilgileri tarih formatına çevirdi.
# print(dt)
# print(datetime.strftime(dt,'%A'))

# deniz_DogumTarih = '13 August 1998'
# dt = datetime.strptime(deniz_DogumTarih,'%d %B %Y')
# print(dt)
# print(datetime.strftime(dt,'%A'))

# birthday = datetime(1998,8,13) #istediği şekilde ekleme
# print(birthday)
# print("--------------------------")
# result = datetime.timestamp(birthday) #pc nin miladı 1970 e göre geçen saniye
# result = datetime.fromtimestamp(result) #ilgili saniyenin hangi tarihe denk geldiği
# result = datetime.fromtimestamp(0) #pc nin miladını öğrenme
# print(result)

# print(datetime.now()-birthday) #şuandan doğum tarihine geçen gün ve saat,timedelta class

from datetime import timedelta

result = datetime.now() + timedelta(days=10) #zamanı ileriye alma
result = result + timedelta(minutes=26)
print(result)
sonuc = result - datetime.now()
print(sonuc)