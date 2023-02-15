name = input("Please enter your name: ")
no = int(input("Please enter your phone number: "))
mail = input("PLease enter your e-mail address: ")


print ("Press 1 for Monday")
print ("Press 2 for Wednesday")
print ("Press 3 for Friday")
day = int(input("Please select the day you want to book the ticket for: "))

if day == 1:
    dday=("Monday")
    print ("Press 1 for 1:00 pm")
    print ("Press 2 for 11:00 pm")
    time = int(input("Please select timing for the train: "))
    if time == 1:
        ttime = ("1:00 pm")
    elif time ==2:
        ttime = ("11:00 pm")
    else:
        print ("Invalid input")

elif day == 2:
    dday=("Wednesday")
    print ("Press 1 for 11:00 am")
    print ("Press 2 for 8:00 pm")
    time = int(input("Please select timing for the train: "))
    if time == 1:
        ttime = ("11:00 am")
    elif time ==2:
        ttime = ("8:00 pm")
    else:
        print ("Invalid input")

elif day == 3:
    dday=("Friday")
    print ("Press 1 for 3:00 pm")
    print ("Press 2 for 1:00 am")
    time = int(input("Please select timing for the train: "))
    if time == 1:
        ttime = ("3:00 pm")
    elif time ==2:
        ttime = ("1:00 am")
    else:
        print ("Invalid input")

else:
    print ("Invalid input")

print("Press 1 for First Class AC")
print("Press 2 for First Class NON-AC")
print("Press 3 for Second Class AC")
print("Press 4 for Second Class NON-AC")
seat = int(input("Please enter seat you want to book: "))
if seat == 1:
    sseat = "First Class AC"
    fare = "₹500"
    seatno = int(input("Please enter your seat no.: "))

elif seat == 2:
    sseat = "First Class NON-AC"
    fare = "₹400"
    seatno = int(input("Please enter your seat no.: "))

elif seat == 3:
    sseat = "Second Class AC"
    fare = "₹300"
    seatno = int(input("Please enter your seat no.: "))

elif seat == 4:
    sseat = "Second Class nON-AC"
    fare = "₹200"
    seatno = int(input("Please enter your seat no.: "))

else:
    print("Invaild input")


print ("INDIAN RAILWAYS")
print("E-Ticket")
print("Name: ",name)
print("Phone no.: ",no)
print("E-mail address: ",mail)
print("Day: ",dday)
print("Time: ",ttime)
print("Seat booked: ",sseat)
print("Seat no.: ",seatno)
print("Total amount: ",fare)
print("Thank you!")