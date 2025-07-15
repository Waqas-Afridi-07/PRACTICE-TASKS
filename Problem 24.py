num = int(input("Enter number: "))

if(num<=0):
    print("Please enter number greater than zero")

else:
    if(num%5==0):
        print("Number is divisible by 5")

    else:
        print("Number is not divisible by 5")

    if(num%3==0):
        print("Number is divisible by 3")

    else:
        print("Number is not divisible by 3")