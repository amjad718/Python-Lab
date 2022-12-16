l1=[]
l2=[]
num1= int(input("Enter the size of the 1st list"))
print("Enter the elements of the list")
for i in range(num1):
    n1=int(input())
    l1.append(n1)
num2= int(input("Enter the size of the 2nd list"))
print("Enter the elements of the list")
for i in range(num2):
    n2=int(input())
    l2.append(n2)
if(num1==num2):
    print("(a) Both the list are of the same length")
else:
    print("(a) Both are of different length")
if(sum(l1)==sum(l2)):
    print("(b) The sum of both lists are equal")
else:
    print("(b) The sum of both lists are different")
comm=set(l1).intersection(l2)
if(comm==None):
    print("(c) There is no common occurences in the list")
else:
    print("(c) The occurences in the list are",comm)

