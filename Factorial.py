#Display the factorial of a number
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num -1)
num = int(input("Enter a number: "))
result = fact(num)
print(f"The factorial of {num} is {result}")
