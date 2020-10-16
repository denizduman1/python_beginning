#json database'den verileri mobil webe kolaylıkla taşıyabiliyoruz.Her programlama dili anlıyor.
import json
person_string = '{"name":"Ali","languages":["python","C#"]}'
# #Json string to Dict
# result = json.loads(person_string) #dic'te çeviriyor.
# print(result)
# print(type(result))
# print(result["languages"])

# with open("person.json") as f:
#     data = json.load(f) # load-> stringsiz loads ->stringli
#     print(data) 
#     print(data["name"])

person_dict = {
    'name' : "Ali",
    'languages' : ['python','C#']
}

# result = json.dumps(person_dict) #dict to json
# print(result)
# print(type(result))

# with open("person.json","w") as file:
#     file.write(result)

# person_dict = json.loads(person_string)
# result = json.dumps(person_dict,indent=4,sort_keys=True)
# print(person_string)
# print(result)

