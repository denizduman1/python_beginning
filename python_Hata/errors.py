#hata yönetimi..

# print(a) => NameError
# int('1a2') => valueError
# print(10/0) => zeroDivisionError

try:
    x = int(input("x= "))
    y = int(input("y= "))
    print(x/y)
# except ZeroDivisionError:
#     print('y için 0 girilemez.')
# except ValueError:
#     print("x ve y için sayısal değer girmelisiniz.")
# except:
#     print("yanlış girdiniz.")
except Exception as e: #e objesi oluşturuluyor.
    print(e)
else: 
    print("her şey yolunda.") # else kısmına break yazarsak while döngüsüne alıp hata almayana kadar kullanıcıya giriş yaptırabiliriz.
finally:
    print("try except sonlandı.")