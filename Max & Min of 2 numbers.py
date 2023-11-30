#Max of 2 numbers
def max_of_numbers(num1,num2):
    return max(num1, num2)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = max_of_numbers(num1, num2)
print("The greatest of", num1, "and",num2, "is", result)

#Min of 2 numbers
def min_of_numbers(num1, num2):
    return min(num1, num2)
num1 = float(input("Enter the fist number: "))
num2 = float(input("Enter the second number: "))
result = min_of_numbers(num1, num2)
print(f"The smallest of {num1} and {num2} is {result}")
