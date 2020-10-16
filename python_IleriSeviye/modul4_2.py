import os
import json

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                print(users)
                for user in users:
                    user = json.loads(user)
                    # print(user['username'])
                    newUser = User(username=user['username'],password=user['password'],email = user['email'])
                    self.users.append(newUser)
                # print(type(user))
                print(self.users)
    
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı Oluşturuldu.")
    
    def login(self,username,password):  
        for user in self.users:
            if  user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login Başarılı")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
    
    def identity(self):
        if self.isLoggedIn:
            print(f'username:{self.currentUser.username}')
        else:
            print("giriş yapılmadı.")
    
    def savetoFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(liste,file)

repository = UserRepository()


while True:
    print("Menü".center(50,"*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSecim:")
    if secim == '5':
        break
    else: 
        if secim == '1':
            username = input("username: ")
            password = input("password: ")
            email = input("e - mail: ")
            user = User(username,password,email)
            repository.register(user)
            print(repository.users)
        elif secim == '2':
            if repository.isLoggedIn:
                print("zaten giriş yapılı.")
            else:
                username = input("username:")
                password = input("password:")
                repository.login(username,password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print("yanlış seçim")