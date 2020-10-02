'''
numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ['deniz','derya','emine','ibrahim']

for name in names:
    print(f"my name is {name}")
    
name = 'deniz'

for n in name:
    print(n)
    
    
tuple = [(1,2),(3,4)]
for t,p in tuple:
    print(t,p)
'''   
'''
users = {
    '1': {
    'ad'  : 'deniz',
    'soyad' : 'duman'
    },
    
    '2': {
    'ad'  : 'derya',
    'soyad' : 'duman'
    }
}

for user,value in users.items():
    print(value["ad"],value["soyad"])'''

''' 
dic = {'1':'a','2':'b'}
#print(dic['1'])

for d,val in dic.items():
    print(val)
'''

ogr_Bilgi = {      #id si olmayan list yapacaksak {} yerine [] kullanırız.
    '1': {
     'name' :  'deniz',
     'surname' : 'duman',
     'okulno'  : '556'
    },
    '2': {
     'name' :  'derya',
     'surname' : 'duman',
     'okulno'  : '340'
    },
}
#print(ogr_Bilgi['1'])

for ogr,val in ogr_Bilgi.items():  #items eklenmesse val alınamaz.
    print(ogr,val['name'],val['surname'])
    
print("**************")

for ogr in ogr_Bilgi: #sadece keyler çıkıyor.
    print(ogr)