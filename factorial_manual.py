import math

print("Welcome to factorial calculator")
number = int(input("Input number : "))
i = number-1
while i>0:
    number*=i
    i-=1
print(number)


