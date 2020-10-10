#dosya açmak ve oluşturmak için open() fonks
#kullanımı: open(dosya_adi,dosya_erisme_modu)
# w,a,x,r dosya erişme modları.

# w (write) yazma komutu. 

# file = open("newfile.txt","w") #w komutu dosyayı konumda oluşturur.
# file.close()

# file = open("C:/users/Deniz/desktop/newfile.txt","w")
# print(file)
# file.close()

# file = open("newfile.txt","w",encoding="utf-8") # w modu dosyayı oluşturur veri yazar. eğer dosyada yazı varsa siler yeniden ekleme yapar.
# file.write("Deniz Duman")
# file.close()

# file = open("newfile.txt","a",encoding="utf-8") #içerik silinmez sonuna ekler.
# file.write("Deniz Duman")
# file.close()

# file = open("newfile.txt","a",encoding="utf-8") #içerik silinmez sonuna ekler.
# file.write("\nDeniz Duman")
# file.close()


# file = open("newfile2.txt","x",encoding="utf-8") #dosyayı oluşturur.