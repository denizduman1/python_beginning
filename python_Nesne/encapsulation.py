class Student: 
    __name = ""
    __surname = ""
    __number = "0"
    def display(self):
        print("name = " + self.__name + " surname = " + self.__surname + " number = " + self.__number)
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    
s1 =  Student()
s1.display()
print("-"*50)
s1.setName("Deniz")
s1_name = s1.getName()
print(s1_name)
s1.display()