import time
user_str = input(str("Enter Text: "))
my_str=""
for i in user_str:
    if ord(i)>65 and ord(i)<=90:
        for j in range(65,91):
            if i==chr(j):
                my_str = my_str + i
                print(my_str,end="")
                break
            else:
                print(my_str + chr(j))
                time.sleep(.05)
    elif ord(i)>97 and ord(i)<=123:
        for j in range(97,123):
            if i==chr(j):
                my_str = my_str + i
                print(my_str,end="")
                break
            else:
                print(my_str + chr(j))
                time.sleep(.05)
    else:
        my_str = my_str + i
        print(my_str,end="")
    print()
input()