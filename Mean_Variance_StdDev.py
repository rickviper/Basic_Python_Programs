from math import sqrt
mylist = []
num = int(input("Enter the number of elements: "))
for i in range(num):
    val = int(input("Enter the element: "))
    mylist.append(val)
print("The length of the list is: ",len(mylist))
print("The contents of the list are: ",mylist)
total = 0
for i in mylist:
    total += i
mean = total/num
total = 0
for i in mylist:
    total += (i-mean)*(i-mean)
variance = total/num
std_dev = sqrt(variance)
print("The mean value is: ",mean)
print("The variance is: ",variance)
print("The Standard Deviation is: ",std_dev)