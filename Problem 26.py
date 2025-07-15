Y = int(input("Enter year: "))

if(Y % 4 == 0):
    if(Y % 100 == 0):
        if(Y % 400 == 0):
            print("Leap year")
        else:
            print("Not a leap year")

    else:
        print("Leap year")

else:
    print("Not a leap year")