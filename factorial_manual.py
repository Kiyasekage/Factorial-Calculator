print("Welcome to factorial calculator")
number = int(input("Input number : "))
counter = number
i = number-1
while i>0:
    number*=i
    i-=1
print("The factorial number of",counter,"is",number)


