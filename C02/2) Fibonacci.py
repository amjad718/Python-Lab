n=int(input("Enter the limit for fibonacci series"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    s=a+b
    print(s)
    a=b
    b=s
