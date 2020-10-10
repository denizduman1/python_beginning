file = open("newfile.txt","r",encoding="utf-8") #dosyayı okuma

# for i in file:
#     print(i,end="") #bilgiler satır satır yazılır.

# content1= file.read() #bilgiler satır satır yazılır.
# print("içerik1")
# print(content1)

# print("içerik2")
# content2 = file.read() #okuncak içerik kalmadığı için content2 boş olur. dosyaay tekrar  open yapmamız lazım.
# print(content2)


# content = file.read(5) #ilk 5 karakter
# print(content)
# content = file.read(3) #sonraki 3 karakter
# print(content)
# content = file.read(3) #sonraki 3 karakter
# print(content)

# content = file.readline()
# print(content,end="") #ilk satırı okur. end parametresi bir satır boş bırakmayı engeller.
# content = file.readline()
# print(content,end="") #ikinci satırı okur.
# #Satır kalmayınca boş çıktı verir.

# liste = file.readlines() #tüm satırları dizi elemanı olarak listeye atar.
# print(liste)
# print(liste[0])
# print(liste[1])
# print("-----")
# for i in liste:
#     print(i)

file.close()