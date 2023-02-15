def area():
    n=int(input("Enter 1 to calculate area of triangle\nEnter 2 to calculate area of rectangle\nEnter your choice: "))
    if n==1:
        base=int(input("Enter the value of base of triangle: "))
        height=int(input("Enter the value of height of triangle: "))
        print("Area of given triangle is: ", (1/2)*base*height,"cm²")
    elif n==2:
        length=int(input("Enter the value of length of rectangle: "))
        width=int(input("Enter the value of width of rectangle: "))
        print("Area of given rectangle is: ", length*width,"cm²")
    else:
        print("ERROR!\nYou failed to enter a vaild input\nThe program is exiting...")
area()
