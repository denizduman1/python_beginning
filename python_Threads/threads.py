import threading
import time

def sayA(name="a"):
    for i in range(10):
        print(i,name,end=" ")
        time.sleep(0.5)

    
def sayB(name="b"):
    for j in range(10):
        print(j,name,end=" ")
        time.sleep(0.5)
        
# sayA()
# sayB()

# t1 = threading.Thread(target=sayA)
# t2 = threading.Thread(target=sayB)
# t1.start()
# t2.start()
start = time.time()
t1 = threading.Thread(target=sayA,args=("Deniz",))  # put  commas(,) inside because type should be tuple
t2 = threading.Thread(target=sayB,args=("Aysima",))

t1.start()
t2.start()
t1.join()
t2.join()

print("")
print("-"*50)
end = time.time()

start_2 = time.time()
sayA("Deniz")
sayB("Aysima")

print("")
print("-"*50)
end2 = time.time()
print((end-start),"seconds for Threads")     
print((end2-start_2),"seconds for Normal")


# start = time.time()
# print("...")
# time.sleep(1)
# end = time.time()
# print((end-start)-1)     
