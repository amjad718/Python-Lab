numbers=[]
num=int(input("Enter the size of the list"))
for i in range(num):
    n=int(input("Enter the number"))
    numbers.append(n)
print("Entered list is:",numbers)
for i in numbers:
    if(i%2==0):
        numbers.remove(i)
print("The entered numbers with even numbers removed is",numbers)
