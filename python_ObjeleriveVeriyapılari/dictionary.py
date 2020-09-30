#key - value ilişkisi (34-İst)

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('kocaeli')])
print("---------------")

plaka = {'kocaeli':41 , 'istanbul' : 34} #dictionary kullanımı { } ve : işaretleri

print(plaka['istanbul']) 

cars = {14800:'Hyundai',24792:'Ford','ww':35000}
print(cars[14800])

cars['bmw'] = 70000
cars['ww'] = 50000
print(cars)

users = {
    'sadikturan' : {
        'yas': 2,
        'memleket': 'adana',
         'job' : ['yazılımcı','eğitimci']
        },
    'cinarturan'  : 2
}
print(users['sadikturan']['job'][0])