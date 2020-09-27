website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
hi = " Hello World "
result = hi.strip() #başta ve sondaki boşlukları siler.
print(result)
result = website.lstrip("/:pth")
sadikturan = 'www.sadikturan.com'
sadikturan = sadikturan.strip("w.com") #barındıran harfleri siler
print(sadikturan)
print("---------------")
result = course.lower()
print(result)
count_a = website.count('a')
print(count_a)
isStart = website.startswith('www')
isEnd = website.endswith('com')
print(isStart,isEnd)
websiteHas = website.__contains__('.com') #içeriyor mu
print(websiteHas)
course_isAlpha = course.isalpha()
print(course_isAlpha)
str_contents = "Contents"
result = str_contents.center(50,'*')
print(result)
result = course.replace(" ","-",5)
print(result)
print("------------------------")
result = 'Hello World'.replace(' ','')
result = result.replace("World","There")
print(result)
result=course.split(' ') #parçalara ayırır.
print(result)
result[0] = "JavaScript" #dizi şeklinde olduğu için değiştirme şansımız olur.
print(result)
print(" ".join(result))
