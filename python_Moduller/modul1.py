'''
import math # as islem  -> dersek math yerine islem yazıp modülü kullanabiliriz.

value = dir(math)
#value = help(math)
value = help(math.factorial)
karekok = math.sqrt(49) #karekök alma
print(karekok)
faktoriyel = math.factorial(5)
print(faktoriyel)
asagiYuvarlama = math.floor(5.9)
print(asagiYuvarlama)
yukariYuvarlama = math.ceil(5.9)
print(yukariYuvarlama)
print("----------------")
'''

#from math import * # dersek ilgili kütüphaneden istediğimiz özellikleri çekeriz ve bundan sonrada math. demek yerine direk fonksiyonu yazabiliriz.

from math import factorial,sqrt,ceil

#factoriel,sqrt gibi fonksiyonları kendimiz yaparsak fromdan önce yazarsak from ezer sonra yazarsak from ezilir.
value = factorial(5)
print(value)
value = sqrt(9)
print(value)
#value = ceil(10.2) çalışmaz. ekledikten sonra çalışır.
value = ceil(10.0001)
print(value)
