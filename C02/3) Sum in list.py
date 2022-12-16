l=[]
total=0
n=int(input("Enter the size of the list"))
print("Enter numbers")
for i in range(n):
    num=int(input())
    l.append(num)
for i in l:
    total=sum(l)
print(total)
