website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course))
print(website[7:10])

lenWebsite = len(website)
print(website[lenWebsite-3:lenWebsite]) #uzunlukla çıkacak


print(course[0:15]+course[-15:]) #-15:0 çalışmaz

lenCourse = len(course)

print(course[::-1])

name,surname,age,job = 'Bora' , 'Yılmaz' , 32 , 'mühendis'

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

hi = 'hello world'
hi = hi[0:6] + 'W' + hi[-4:]

print(hi)

dizi = 'abc '

print(dizi*3)

