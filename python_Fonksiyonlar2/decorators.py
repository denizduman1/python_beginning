# def homeFunc (func):
#     def innerFunc():
#         print("func öncesi")
#         func()
#         print("func sonrası")
#     return innerFunc

# def sayHello():
#     print("hello")

# def greetings():
#     print("greeting..")
  
# merhaba = homeFunc(sayHello)
# merhaba()
# print("-------")
# mektup = homeFunc(greetings)
# mektup()
# print("-------")
# print(homeFunc(greetings)())

# def homeFunc (func):
#     def innerFunc(names):
#         print("func öncesi")
#         func(names)
#         print("func sonrası")
#     return innerFunc

# @homeFunc
# def sayHello(name):
#     print("hello",name)
    
# sayHello("ronaldo")
# print("-------")



# def usAl(sayi,us):
#     startTime = time.time() 
#     time.sleep(1)
#     sonuc = math.pow(sayi,us)
#     print("sonuc:",sonuc)
#     finishTime = time.time()
#     gecenZaman = finishTime - startTime
#     print("süre:"+str(gecenZaman))

# def faktoriyel(sayi):
#     startTime = time.time() 
#     time.sleep(1)
#     sonuc = math.factorial(sayi)
#     print("sonuc:",sonuc)
#     finishTime = time.time()
#     gecenZaman = finishTime - startTime
#     print("süre:"+str(gecenZaman))
# usAl(5,3)
# print("-----------------")
# faktoriyel(6)

import math
import time

def time_Calculate(func):
    def innerFunc(*args,**kwargs):
        startTime = time.time()
        time.sleep(1)
        a = func(*args,**kwargs)
        finishTime = time.time()
        print("Fonksiyon Adı:",func.__name__,"sonuc:",a," süre:",str(finishTime-startTime))
    return innerFunc

@time_Calculate
def topla(a,b):
    return a+b
@time_Calculate
def usAl(a,b):
    return math.pow(a,b)

topla(5,6)
print("-----")
usAl(7,2)