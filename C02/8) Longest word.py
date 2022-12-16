s=input("Enter the string to find the longest word")
l=s.split()
n=len(l[0])
s=l[0]
for i in l:
    if len(i)>n:
        s=i
        l=len(i)
print("The longest word in the entered list is: ",s)
