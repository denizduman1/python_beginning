tuple = (1,2,3,4,3)
print(tuple)
print("0.indeks: ",tuple[0])
tuple_add = (5,6,7,8)
tuple = tuple + tuple_add
print("birleşmiş hali",tuple)
print("kaç tane 3 var? ",tuple.count(3))
print("---------")
list=[1,2]
list_add=[3,4]
list = list + list_add
print(list)
#tuplenin list'ten farkı elemanlar silinemez veya değiştirilemez
#tuple daha az bellek harcar.
