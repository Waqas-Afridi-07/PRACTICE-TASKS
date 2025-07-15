num = int(input("Enter the number: "))

if(num<=1):
    print("Not prime, Enter greater number")

else:
    for i in range(2, num):
        if (num % i == 0):
            print("Number is not prime")
            break

    else:
        print("Number is prime")