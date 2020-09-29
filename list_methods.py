numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = max(numbers)
print(val)

val = min(letters)
print(val)

val = numbers[3:6]
print(val)

index = len(numbers)
val = numbers[(index-3):]
print(val)

numbers.append(99) #ekleme yapar.
numbers.insert(3,7) #konuma ekleme yapar.
numbers.pop(2) #eleman çıkar
numbers.remove(10) #seçili elemanı siler.
numbers.sort()
#numbers.reverse() tam terse çevrilir
letters.sort() 
print(numbers)
print(letters)

print(numbers.index(9))




