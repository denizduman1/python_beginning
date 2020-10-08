import random

#result = dir(random)
#print(result)
'''
result = random.random() #0.0 1.0 arası
print(result)

intSayi = random.randint(0,10) # 0 ve 10 dahil.
print(intSayi)
'''


names = ['deniz','derya','emine','ibrahim']
result = []
sayi = 0
x = 0
while x<len(names):
    sayi = random.randint(0,len(names)-1)
    if result.__contains__(names[sayi]):
        continue
    else: 
        result.append(names[sayi])
        x += 1    
print(result)
print("-------------")
print(random.choice(names)) # liste elemanlarından birini çekiyor.
print("-------------")
random.shuffle(names) # liste elemanlarını karıştırıyor.
print(names)
print("-------------")
ikiElaman=random.sample(names,2) # liste elemanlarından istediğin kadarını çekiyor.
print(ikiElaman)

