names=['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

names.append('Cenk')
print(names)
print("----------------")
names.insert(0,"Sena")
print(names)
print("----------------")
names.remove('Deniz')
print(names)
print("----------------")
index = names.index('Yağmur')
print(index)
isContainAli = names.__contains__('Ali')
print("----------------")
print(isContainAli)
print("----------------")
print("düz hali: ",names)
print("----------------")
names.reverse()
print("ters hali: ",names)
names.sort()
print("----------------")
print(names)
print("----------------")
years.sort()
years.reverse()
print(years)
print("----------------")
str = 'Chevrolet,Dacia'
cars = str.split(",")
print(cars)
print("----------------")

minYears = min(years)
maxYears = max(years)
print("max: ",maxYears,"min: ",minYears)

print("----------------")

count_1998 = years.count(1998)
print(count_1998)

print("----------------")

years.clear()
print(years)

markalar= []
marka = input("marka: ")
markalar.append(marka)
print(markalar)

ad = input("adınız:")
soyad = input("soyadınız:")
print(ad+" "+soyad)