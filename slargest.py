list=[]
for i in range(0,5):
    list.append(int(input("Enter a number:")))
    i+=1
print("List=:",list)
a = max(list)
b = 0
for i in list:
    if b<i and a!=i:
        b=i
print("Second largest number is:",b)
