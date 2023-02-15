import random

def gen():
    return random.randint(1,10)
def inp():
    return int(input('Enter your guess:'))
def game():
    a = gen()
    n=inp()
    c = 2
    while n!=a and c>=1:
        if n<a:
            print('number you entered is small,',c,'attempt left')
            c-=1
        if n>a:
            print('number you entered is big,',c,'attempt left')
            c-=1
        n = inp()
    if c==0 and n!=a:
        print("you lose, i thought of",a)    
    if n==a:
        print("that's what i thought")

print("guess that random number between 1 and 10 in my mind within 3 tries")
game()