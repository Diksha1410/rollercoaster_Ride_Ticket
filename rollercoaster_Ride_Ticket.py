# Write a python Program where a ticket collector asks a question and generate ticket for the Rollercoaster Ride
# a. Somebody who is over 120 cm allows them to purchase a ticket otherwise not.
# b. Check the age of the rider and allow him to ride
# c. Also if rider wants to click the photo or not.

# Code Starts Here:- 

# printing the WELCOME message
print("******* Welcome to the ROLLERCOASTER RIDE *******")
# declaring a variable
bill = 0

# 
while True:
    # asking for input from the users
    height = input("Please enter height in cm: ")
    # using isdigit method of string
    if height.isdigit():
        height = int(height)
        break
    else:
        print("[INVALID INPUT]")
        continue

# using range function
if height in range(1,120):
    print("You Can't ride")
elif height>120:
    print("You Can ride")

    while True:
        # asking for input from the users
        age = input("Please Enter age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("[INVALID INPUT]")
            continue
    # using the if-elif-else conditions
    if age not in range(1,56):
        print("Age not valid")
    else:
        if age in range(12,18):
            bill +=7 
        elif age in range(18,44):
            bill +=12
        elif age in range(44,56):
            bill += 0
        else:
            bill +=5
        # asking user if they want photos 
        want_photos = input("Do you want photos?\n Press 1 for Yes 2 for No: ")

        while want_photos not in ("1", "2"):
            want_photos = input("Please choose 1 or 2\n")
        else:
            match want_photos:
                    case "1":
                        print(f"The total bill is - ${bill+3}")
                    case "2":
                        print(f"The total bill is - ${bill}")
    

            