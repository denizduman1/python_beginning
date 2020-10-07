class Circle: 
    pi = 3.14
    def __init__(self,yaricap=1):
        self.yaricap = yaricap 
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap 
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle(yaricap=5)
c2 = Circle()

print(f"c1, alan: {c1.alanHesapla()} ve çevre: {c1.cevreHesapla()}")
print(f"c2, alan: {c2.alanHesapla()} ve çevre: {c2.cevreHesapla()}")