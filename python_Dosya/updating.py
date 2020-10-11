# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ güncelleme işine yarıyor.
#     print(file.read())
#     print("----------")
# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ güncelleme işine yarıyor.
#     file.seek(20)
#     file.write("deneme") # 20 den diziye deneme atar.
    
# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ güncelleme işine yarıyor.
#     print(file.read())

# with open("newfile.txt","a",encoding="utf-8") as file: #sonuna ekler.
#     file.write("\nyeniyazı eklendi.")
    
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(9,"Ayşe Duman ")
#     file.seek(0)
#     # for i in list:
#     #     file.write(i)
#     file.writelines(list)
#     print("--------")
    
# with open("newfile.txt","r",encoding="utf-8") as oku:
#     print(oku.read())