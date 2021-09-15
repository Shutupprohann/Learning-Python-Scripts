import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*/"

while True :
    password_lenghth = int(input("Enter The length of Password :"))
    password_count = int(input("Enter the number of passwords you want : "))
    for i in range(0,password_count):
        password = " "
        for x in range(0,password_lenghth):
            password_char = random.choice(chars)
            password = password + password_char

        print("Here is your passwowrd :" + str(password)) 
    exit()    
       







