#w->üzerine 0 dan yazma
#x->create
#a->üzerine kaldığı yerden ekleme
#r->read

# open("newfile3.txt","x")

# file = open("newfile3.txt","w")
# file.write("0123456789")
# file.close()

# with open("newfile3.txt","a",encoding="utf-8") as file: #file.close() dememize gerek yok kendisi kapatıyor.
#     file.write("abcçdefgğhıijklmnoöprsştuüyz")

with open("newfile3.txt","r",encoding="utf-8") as oku:
    print(oku.read())
    print(oku.tell()) #kürsünün kaçta kaldığını gösterir.
    print(oku.read()) #boş döner.
    oku.seek(5) #kürsüyü 5e çeker
    print(oku.read()) #5 ten itibaren okur.
    oku.seek(0)
    print(oku.read(10)) #kürsünün kaldığı yerden itibaren 10 harf okur.
    print(oku.read(5)) # en son 10 harf okumuştu üstüne 5 harf okur