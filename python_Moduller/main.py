import mod
import math #python klasörümüzdeki kütüphanelerden biri,math gibi bazı fonksiyonlar C ile çekildiği için DLL klasöründe yer alıyor.

#help(mod)
#help(mod.function)

print(mod.number)
print(mod.numbers)
print(mod.person["name"])
print(mod.person["age"])
mod.function(10)
p = mod.Person() #moddaki sınıfı çağırıyoruz 
p.speak()