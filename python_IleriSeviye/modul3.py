import re 
# result = dir(re)
# print(result)

metin = "Python, Dünyanın En Popüler Programlama Dilidir . Python Dili Nesne İlişkilidir."

result = re.findall("Python",metin)
print(result)
print(len(result))
print("--------------------------")
result = re.split(" ",metin)
result = re.split(",",metin)
#result = re.split(".",metin)
print(result)
print("-------------------------")
result = re.sub("Python","C#",metin)
print(result)
print("-------------------------")
result = re.search("Dilidir",metin)
#result = result.start()
#result = result.end()
#result = result.span() #aralık gösterir.
result = result.string
print(result)
print("-------------------------")
sonuc = re.findall("[^a-z]",metin)
print(sonuc)
print("-------------------------")
text = re.findall("...",metin)
print(text)
print("-------------------------")
text = re.findall("Ne*sne",metin)
print(text)
print("--------------------------")
kelime = "Saat,Vaat,Bayat,Höyt,Giresun"
print(len(kelime))
print(len(re.findall("a|t",kelime)))
print(re.findall("(a|y)t",kelime))
print("--------------------------")
print(re.findall("n$",kelime)) #n ile bitiyor mu
