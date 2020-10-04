'''
def myFunc(word,count):
    sayi = 1
    while sayi<=count:
        print(word)
        sayi+=1
    #print(word*count)
'''
'''
myFunc("example",2)
print("-------------------------")
   
def myFunc_2(*args):
    lists = []
    for arg in args:
        lists.append(arg)
    return lists

print(myFunc_2(1,2,3,4,5,6,7,8,9))
'''
'''
sayi1 = int(input("sayi1:"))
sayi2 = int(input("sayi2:"))

def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
            else:
                print(sayi)
                    
        
asalSayilariBul(sayi1,sayi2)
'''

'''
def example(start,end):
    for sayi in range(start,end+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
            else:
                print(sayi)

sayi1=int(input())
sayi2=int(input())
print("***********")
example(sayi1,sayi2)
'''

def tamBolenBul(sayi):
    tamBolenler = []
    for x in range(1,sayi+1):
        if(sayi%x==0):
            tamBolenler.append(x)
    print(tamBolenler)
tamBolenBul(20)