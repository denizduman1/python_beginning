# # x = 10

# # if x>5:
# #     raise Exception("x 5 den büyük değer alamaz.") exception fırlatma.

# def check_password(psw):
#     import re #regular expressions
#     if len(psw) <= 6 :
#         raise Exception("parola en az 7 karakter olmalıdır.")
#     elif not re.search("[a-z]",psw): #parolada küçük harf kontrolü
#         raise Exception("parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]",psw): #parolada büyük harf kontrolü
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]",psw): #parolada rakam kontrolü
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$?]",psw): #parolada alphanumeric kontrolü
#         raise Exception("parola alphanumeric içermelidir.")
#     elif re.search("\\s",psw): #boşluk kontrolü
#         raise Exception("parola boşluk içermemelidir.")
#     else:
#         print("parola girişi doğrudur.")
        
# password = "1234567aA?an"

# try: 
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola else")
# finally:
#     print("validation tamamlandı.") # yanlış olsun olmasın her türlü çıkar.

class Person:
    def __init__(self,name,year):
        if len(name) > 10 :
            raise Exception("name alanı fazla karakter içeriyor.")
        else: 
            self.name = name

p = Person("Denizzzzzzzzzzzzzzzz",1998)