#Program to delete all odd and negative numbers from a list
list=[]
for i in range(0,5):
    list.append(int(input("Enter a number:")))
print(list)
i,j=0,5
while i<j:
    if list[i]<0:
        del list[i]
        j-=1
    elif list[i]%2!=0:
        del list[i]
        j-=1
    else:
        i+=1
print(list)
