'''
lst = [1,2,3] 
result = type(lst) #list class'ı üzerinden çalışıyoruz.
print(result)
#instance = object = nesne
'''

class Person:
    adress = 'no' #class attribute
    def __init__(self,name,year): #kurucu fonksiyon
        self.name = name
        self.birthyear = year
        print('init metot çalıştı.')

p1 = Person("Deniz",22) #object
p2 = Person("Derya",18) #object

print(f'name:{p1.name} year:{p1.birthyear}')
print(p1.adress)

p1.name = 'ahmet'
print("name:",p1.name)


'''
print(p1)
print(p2)
p1 = p2 #aynı adresi tutmaya başladılar.
print(p1)
print(p2)
print(type(p1))
'''
