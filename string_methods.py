message = " Hello my name is Deniz and how are you?"

upper_message = message.upper()
lower_message = message.lower()
title_message = message.title()
capitalize_message = message.capitalize() #ilk harf büyük
strip_message = message.strip()
split_message = message.split()

print(upper_message)
print(lower_message)
print(title_message)
print(capitalize_message)
print(strip_message)
print(split_message)
print(split_message[5])
print(" ".join(split_message)) #mesajları birleştirir sol taraf birleştirmede araya eklenen şeyi belirler.
print('------------')
index = message.find("Deniz")
print(index)
isStart = message.startswith(" ") #başlangıç kontrolü
isEnd = message.endswith("?") #son işaret kontrolü
print(isStart)
print(isEnd)
message = message.replace("Deniz","Duman") #soldakini sağdakiyle değiştir.
print(message)
message = message.center(100,'*')
print(message)


















