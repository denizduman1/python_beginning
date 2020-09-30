'''  
x = 5
y= 10
z = 20 
'''

x,y,z = 5,10,20
x,y = y,x
x=x+5
x+=5
x-=10
y //= 3
z **= 3
print(x,y,z)

values = (1,2,3,4,5) #tuple
x,y,*z = values #z elemanı dizi olur.
print(x,y,z)