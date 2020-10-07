class Movie():
    def __init__(self,name,director,duration):
        self.name = name
        self.director = director
        self.duration = duration
        print("constructor")
    def __str__(self): #özel methodlardandır.
        return f"fimin adı {self.name} dir."
    def __len__(self): #özel method uzunluk olduğu için int değer ister.
        return self.duration
    def __del__(self): #objeyi silen özel method.
        print("obje silindi.")

m1 = Movie("name","director",120)
l1 = []
print(type(m1))
print(type(l1))
print("----")
print(l1)
print("----")
print(m1)
print(str(m1))
print(len(m1))
print("----")
del(m1)
print("----")
print(m1)