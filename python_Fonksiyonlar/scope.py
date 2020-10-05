#global scope
x = 'global x'

def func(): 
    # local scope
    x = 'local x' #yorum satırı olursa x = global x gösterir
    print(x)
    
func()
print(x)

print("***************************")

name = 'Çınar'
def changeName(new_name):
    name = new_name
    print(name)
    
changeName('Ada') #Ada
print(name) #Çınar
print("************")

name = 'global string'
def greeting():
    #name = 'Çınar'
    def hello():
        #name='Ada'
        print("hello "+name)
    hello()
    
greeting()
print("-------------------")

x=50
def test():
    global x #global değişkene etki eder
    print('x:',x)
    x= 100
    print('changed x to :', x)
    
test()
print(x)