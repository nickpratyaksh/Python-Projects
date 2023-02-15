#program to delete all duplicate elements from a list
list = []
for i in range(5):
    list.append(int(input("Enter a number:")))
print(list)
a=4
for i in range(a):
    for j in range(i+1,a):
        if list[i] == list[j]:
            print('yo')
            del list[j]
            a-=1
#doesnt work

