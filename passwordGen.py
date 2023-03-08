import random

def generator(len):
    password = ""
    for i in range(0,len):
        selector = random.randint(0,3)
        if selector == 0:
            password += chr(random.randint(65,90))
        elif selector == 1:
            password += chr(random.randint(97,122))
        elif selector == 2:
            password += str(random.randint(0,9))
        elif selector == 3:
            password += chr(random.randint(33,64))
    return password

len = int(input("How long do you want the password to be? "))
print("The generated password is: ",generator(len))