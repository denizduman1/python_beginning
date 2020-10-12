# liste = [1,2,3,4,5] #iterable => yenilenebilir obje

# iterator = iter(liste)
# print(next(iterator)) #1
# print(next(iterator)) #2
# print(next(iterator)) #3
# print(next(iterator)) #4
# print(next(iterator)) #5
# #print(next(iterator)) #hata

# for i in liste:
#     print(i)

# iterator = iter(liste)

# while True: #for döngüsü arkada bu işlemi yapıyor.
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# class MyNumbers:
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
#     def __iter__(self): #çift altçizgi özel methodları tanımlar.
#         return self
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration
        
# list = MyNumbers(10,20)
# # for x in list:
# #     print(x)

# myiter = iter(list)

# while True:
#     try:
#         element = next(myiter)
#         print(element)
#     except StopIteration:
#         print("hata")
#         break


class HarfOlustur:
    def __init__(self,start,end,harf):
        self.harf = harf
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return self.harf * self.start
        else:
            raise StopIteration
    
harfCikart = HarfOlustur(0,5,"a")
for x in harfCikart:
    print(x) 
print("------------------------------------")
harfCikart2 = HarfOlustur(0,5,"a")
harfCikart2 = iter(harfCikart2)
while True:
    try:
        print(next(harfCikart2))
    except StopIteration:
        break