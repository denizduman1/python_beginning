import gc
import ctypes

class PyObject(ctypes.Structure):
    _fields_ = [("refcnt",ctypes.c_long)]

gc.disable()

lst = []
lst.append(lst)

lst_adress = id(lst) #memory adress
print(lst_adress)

del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1
obj_adress = id(object_1)
obj_adress_2 = id(object_2)
print(obj_adress)
print(obj_adress_2)
a = []
a.append(a)
a_adress = id(a)
del a
del object_1,object_2
gc.collect() #del işlemindeki değişkenlerin hafızadaki değerini siler.iç içe nesnelerde dairesel olanları siler.

print(PyObject.from_address(obj_adress).refcnt)
print(PyObject.from_address(lst_adress).refcnt)
print(PyObject.from_address(a_adress).refcnt)

