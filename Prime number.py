#To find whether a number is Prime or not
def isprime(num):
    if num <=1:
        print(num, "is not a prime number")
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number.")
            break
        else:
            print(num, "is a prime number.")
isprime(int(input("Enter a number: ")))
