class BaseClass: 
    def show(self):
        print("Base class is working.")
    
class A(BaseClass): 
    def show(self):
        print("A class is working")

class B(BaseClass):
    pass



a1 = A()
b1 = B()

a1.show()
b1.show()

print ("-"*50)


class Language: 
    def sayHello(self):
        raise "sayHello from Base Class"
    
class English:
    def sayHello(self):
        print("Hello")

class Turkish:
    def sayHello(self):
        print("Merhaba")
        
        
def say(object):
    object.sayHello()
    
en = English()
tr = Turkish()
lng = Language()

#lng.sayHello()
print("English -> ",end=" ")
en.sayHello()
print("Turkish -> ",end= " ")
tr.sayHello() 