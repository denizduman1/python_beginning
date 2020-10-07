class Car():
    def __init__(self,model,fiyat):
        self.model = model
        self.fiyat = fiyat
        print(f"{self.model} model ve {self.fiyat} fiyatlı aracınız oluşturuldu.")
    def aracYasHesapla(self):
        yas = 2020 - self.model 
        return yas
    
class Opel(Car):
    def __init__(self,marka,model,fiyat,dizelMi,otomatikMi):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat
        self.dizelMi = dizelMi
        self.otomatikMi = otomatikMi
        super().__init__(model,fiyat)
        print(f"{self.marka} markalı aracınız oluşturuldu.")
    def markaOzellikleri(self):
        if self.dizelMi == True : 
            if self.otomatikMi == True: 
                print("Aracınız dizel ve otomatik viteslidir.") 
            else :
                print("Aracınız dizel ve manuel viteslidir.")      ,
        else: 
            if self.otomatikMi == True:
                print("Aracınız benzinli ve otomatik viteslidir.") 
            else :
                print("Aracınız benzinli ve manuel viteslidir.")  
              
       
        
        
o1 = Opel("Opel",2019,45000,True,False)
o1.markaOzellikleri()
print("Aracınız",o1.aracYasHesapla(),"yaşındadır.")