# def greeting(name):
#     print('hello ',name)

# # # print(greeting('ali'))
# # # print(greeting)

# sayHello = greeting #adresi atıyoruz. 
# # print(sayHello)
# # print(greeting)

# # greeting('deniz')
# # sayHello('deniz')

# del sayHello # adres silinmiyor tanımlanma siliniyor.
# #del greeting
# print(greeting)

#encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         return num1+1
#     num2=inner_increment(num1)
#     print(num1,",",num2)
    
# outer(5)
# inner_increment(10) #çalışmaz.


# def factorial(number):   
#     if not isinstance(number,int):
#         raise TypeError("number must be an integer.")
#     if not number > 0:
#         raise ValueError("number must be zero or pozitive")
#     def inner_factorial(number):
#         if number <= 1: 
#             return 1 
#         return number * inner_factorial(number-1)
#     return inner_factorial(number)

# try:
#     print(factorial(-5))
# except Exception as e:
#     print(e)

# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner #fonksiyon döndürme

# two = usalma(2)
# print(two(3))
# three = usalma(3)
# print(three(4))


# def yetki_sorgula(page):
#     def inner_auth(role):
#         if role == "Admin":
#             print("{0} yetkisindeki kişi {1} sayfasına giriş yapabilir.".format(role,page))
#         else:
#             print("{0} yetkisindeki kişi {1} sayfasına giriş yapamaz.".format(role,page))
#     return inner_auth


# user = yetki_sorgula("index.html")
# user("User")


# def islem(islem):
#     def topla(*args):
#         toplam = 0
#         for i in args:
#             toplam = toplam+i
#         return toplam
#     def carp(*args):
#         carpma = 1 
#         for i in args:
#             carpma = carpma * i
#         return carpma
#     if islem == "topla":
#         return topla
#     if islem == "carp":
#         return carp
    
# toplama = islem("topla")
# print(toplama(1,2,3,4,5))
# print("---------")
# carpma = islem("carp")
# print(carpma(1,2,3,4,5))    
    