'''
lst = [1,2,3] 
result = type(lst) #list class'ı üzerinden çalışıyoruz.
print(result)
#instance = object = nesne
'''

class Person:
    adress = 'no' #class attribute
    def __init__(self,name,year): #kurucu fonksiyon
        #object attributes
        self.name = name        
        self.birthyear = year
        print('init metot çalıştı.')
    #instance methods
    def intro(self):
        print("Hello There " + self.name)
    def calculateAge(self):
        return 2019 - self.birthyear



p1 = Person("Deniz",1998) #object
p2 = Person("Derya",2002) #object

print(f'name:{p1.name} year:{p1.birthyear}')
print(p1.adress)
p1.name = 'İbrahim'
print("name:",p1.name)
print("-------------------------")
p1.intro()
p2.intro()
print("-------------------------")
print(p1.calculateAge())
print("-------------------------")
print(p2.calculateAge())



'''
print(p1)
print(p2)
p1 = p2 #aynı adresi tutmaya başladılar.
print(p1)
print(p2)
print(type(p1))
'''