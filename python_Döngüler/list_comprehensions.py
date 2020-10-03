list = []
for x in range(1,10):
    list.append(x)
print(list)

numbers = []
numbers = [x for x in range(10)] #kısa yoldan ekleme
print(numbers)

numbers_1 = []
numbers_1 = [x**2 for x in range(10)]
print(numbers_1)

numbers_2 = []
numbers_2 = [x for x in range(10) if(x%3==0)]
print(numbers_2)

word = 'Leo Messi'
alphabet = [x for x in word]
print(alphabet)

years = [1982,1974,1995,1998,2005]
age = [2019-year for year in years]
print(age)

nums = [x if x%2==0 else 'TEK'  for x in range(10)]
print(nums)

list_xy = []
for x in range(3):
    for y in range (2):
        list_xy.append((x,y))
        
print(list_xy)

list_xy_1 = [(x,y) for x in range(3)  for y in range(2)] #kısayolu
print(list_xy)