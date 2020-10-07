import random

class Soru:
    def __init__(self,soru,secenekler,cevap):
        self.soru = soru
        self.secenekler = secenekler
        self.cevap = cevap
    def yarismaciCevabi(self,cevap):
        return self.cevap == cevap

s1 = Soru("en iyi takım hangisidir?",['FB','GS','TS','BJK','GİRESUN'],'FB') 
s2 = Soru("fenerbahçe kaç yılında kuruldu?",["1907","1905","1903","1961"],"1907")
s3 = Soru("galatasaray kaç yılında kuruldu?",["1907","1905","1903","1961"],"1905")


'''
print(s1.yarismaciCevabi("FB"))
print(s1.yarismaciCevabi("BJK"))
print(s2.yarismaciCevabi("1905"))
print(s2.yarismaciCevabi(1907))
'''

class Yarisma:
    def __init__(self,sorularListesi):
        self.sorular = []
        self.x = 0
        while self.x<=2 :
            sayi = random.randint(0,2)
            if self.sorular.__contains__(sorularListesi[sayi]):
                continue
            else:
                self.sorular.append(sorularListesi[sayi])
                self.x = self.x + 1
        self.puan = 0
        self.sorusirasi = 0
    
    def soruyuCek(self):
        return self.sorular[self.sorusirasi]

    def yarismaBaslasin(self):
        soru = self.soruyuCek()
        print((self.sorusirasi+1),".soru:",(soru.soru))
        for x  in  soru.secenekler:
            print("-",x)
        yarismaciCevap = input('Cevabınız:')
        self.yarismaDevam(yarismaciCevap)
        self.yeniSoruYukleme()
    def yarismaDevam(self,yarismaciCevap):
        sorum = self.soruyuCek()
        if sorum.yarismaciCevabi(yarismaciCevap) :
            self.puan += 1 
        self.sorusirasi += 1
    def yeniSoruYukleme(self):
        if len(self.sorular) == self.sorusirasi:
            self.soruSurec()
            self.skorGoster()
        else:
            self.soruSurec()
            self.yarismaBaslasin()
    def skorGoster(self):
        print("skor:",self.puan)
    def soruSurec(self):
        totalQuestion = len(self.sorular)
        soruNumarasi = self.sorusirasi + 1
        if soruNumarasi>totalQuestion :
            print("Quiz bitti")
        else:
            print(f"Soru {soruNumarasi} of {totalQuestion}".center(100,'*'))

sorularListesi = [s1,s2,s3]
yarismaci_1 = Yarisma(sorularListesi)
yarismaci_1.yeniSoruYukleme()