if 3>2:
    print("Hoşgeldiniz..") #if şart(iki nokta) altına bir tab boşluk.

username = 'deniz'
password = '1234'

isLoggedin = (username=='deniz') and (password=='1234')

if isLoggedin:
    print(f"hoşgeldin {username}")
else:
    print('username ya da password yanlış.')

if (username=='deniz'):
    if(password=='1234'):
        print("hoşgeldin")
    else:
        print('parola yanlış')
else: 
    print("username yanlış")
    

    