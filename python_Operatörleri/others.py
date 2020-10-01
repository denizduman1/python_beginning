# is, in

x = y = [1,2,3]
z = [1,2,3]
# x[2] = 4 y nin de değişir. 
print(x==z)
print(x is y) # x ile y aynı referans mı?
print(x is z)

x=['apple','banana']
print('banana' in x) #banana x listesinde var mı?
