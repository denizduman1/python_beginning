'''
for item in range(-5,10,2):
    print(item)
'''
'''
# 1'den 10 a kadar liste oluştur.

list = list(range(1,11,1)) #liste yapar sondaki artış miktarı
print(list)
'''
'''
greeting = 'Hello There'

for index,letter in enumerate(greeting): #listeyi numaralandırmaya yarar.
    print(f'index:{index} letter:{letter}')
'''

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
    
for a,b,c in zip(list1,list2,list3):
    print(a,b)