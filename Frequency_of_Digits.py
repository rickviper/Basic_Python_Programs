num = input("Enter a number: ")
print("The entered number is: ",num)

unique_digit = set(num)

for i in set(num):
    print(f"{i} occurs {num.count(i)} times")
    
