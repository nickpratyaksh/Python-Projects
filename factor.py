n=int(input("Enter a number: "))
for i in range(1,n):
    if(n%i==0):
        print(i,"is a factor of",n)
