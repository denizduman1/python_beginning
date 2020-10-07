#kalıtım (inheritiance): Miras alma

class Person():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        print('Person Created')
    def eat(self):
        print(f"{self.name} kişisi yemek yer.")
    def who_am_i(self):
        print("ben bir insanım.")
    
class Student(Person): #parantez içine kalıtım alacağı sınıf yazıldı.Person sınıfındaki özellik ve methodların hepsine bu sınıftan dahil olmuş oluyoruz.
    def __init__(self,name,surname,studentNo):
        Person.__init__(self,name,surname)
        self.studentNo = studentNo
        print('Student Created')
    def who_am_i(self): #üst sınıfta aynı adda fonksiyon varsa bunu ovverride eder.
        print("ben bir öğrenciyim.")
    def sayHello(self):
        print("hello i am a student")
    
class Teacher(Person):
    def __init__(self,name,surname,branch):
        super().__init__(name,surname) #super fonksiyonu kalıtım aldığı sınıfa götürür.
        self.branch = branch
        print("Teacher Created")
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

'''
p1 = Person()
print("---------")
s1 = Student()
print("---------")
'''
p1 = Person('Deniz','Duman')
s1 = Student('Derya','Duman',556)
print("---------")
print(p1.name+' '+p1.surname)
print(s1.name+' '+s1.surname+' '+str(s1.studentNo))
print("---------")
p1.eat()
s1.eat()
print("---------")
p1.who_am_i()
s1.who_am_i()
print("---------")
s1.sayHello()
print("---------")
t1 = Teacher("Emine","Duman","Matematik")
t1.who_am_i()
t1.eat()