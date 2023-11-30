#Displaying the gcd of two numbers
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sol = gcd(num1, num2)
print(f"The gcd of {num1} and {num2} is {sol}")
