import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos") #Response 200 başarılı.
# print(result)
# result = result.text 
result = json.loads(result.text) # içindeki string bilgiyi dicte alıyor.
#print(result)
#print(result[0]['title'])
# print(result[0])
# print(result[0]['title'])

# for i in result:
#     if i['userId'] == 1 :
#         print(i['title'])
# liste = []
# liste.append(json.dumps(result))

# with open("website.json","w") as file:
#     json.dump(result,file)

# result = json.dumps(result)
# with open("website.json","w") as file:
#     json.dump(result,file)

# with open("website.json","r") as file:
#     oku = json.load(file)
#     oku = json.loads(oku)

# for o in oku:
#     print(o['completed'])