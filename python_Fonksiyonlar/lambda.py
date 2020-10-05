def square(num): return num**2

numbers=[1,3,5,6,8,9]

result = list(map(square,numbers)) #map metodu list veya for ile çevrilmesi gerekiyor.
print(result)

result = list(map(lambda num: num**3,numbers)) #kısa fonksiyon lambda ile
print(result)

def check_even(num): return num%2==0

result = list(filter(check_even,numbers)) #listenin elemanlarını filtrelemeye yarıyor.
print(result)

