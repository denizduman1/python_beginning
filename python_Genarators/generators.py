#bellekte yer işgal etmeyen 

# def cube():
#     for i in range(5):
#         yield i ** 3 # yield değer üretiyor. ve bi yerde saklamıyor. Generators olur. Bellekte yer tutulmaz performans artar.

# generator = cube()
# # iterator = iter(generator) buna da gerek yok otomatik iter oluyor.

# for i in generator:
#     print(i)  
    
# print("-----")

# for i in cube():
#     print(i)

#tekrar ulaşılmayacaksa tek sefer gösterilip geçilcekse ram yer harcamaması için değişkene atayıp yer tutmayız.

liste = (i**3 for i in range(5)) #koseli parantez yapmazsak liste özelliği gider genaratorse döner.

for i in liste:
    print(i)
