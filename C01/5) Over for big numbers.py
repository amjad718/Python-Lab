numbers=[]
num=int(input("Enter how many numbers"))
for i in range(num):
    n=int(input("Enter the numbers"))
    numbers.append(n)
for i in range(num):
    if numbers[i]>100:
        numbers[i]="over"
print(numbers)