userID_1 = ["Deniz","Duman",22,"Bilgisayar Mühendisi"]
userID_2 = ["Derya","Duman",18,"Öğrenci"]

print("Liste Bilgileri..")
print("userID_1: " , userID_1) #liste olduğu için arada + değil , koyulmalı [index] olursa + konulabilir.(string olduğundan)
print("userID_2: " , userID_2)
print("----------------------")

allUsers = userID_1  + userID_2

print("All users: ", allUsers) #birleştirip verir
print("----------------------")

allUsers_separate = [userID_1]+[userID_2]

print(allUsers_separate) #kullanıcıları ayırarak verir.

print("----------------------")

print("first user name: "+allUsers_separate[0][0]) # first users name 
