#Find Fibonacci sequence of a number
num = int(input("Enter a number: "))
term1 = 0
term2 = 1
print("The fibonacci sequence of length",num, "starts with: ")
print(term1, term2)
for i in range (2,num):
    curterm = term1 + term2
    print(curterm)
    term1 = term2
    term2 = curterm
