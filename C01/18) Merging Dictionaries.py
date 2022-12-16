dict1={}
dict2={}
n1=int(input("Enter the size of the 1st dictionary"))
for i in range(n1):
    key=input("Enter the key")
    value=input("Enter the value")

    dict1[key]=value
n2=int(input("Enter the size of the 2nd dictionary"))
for i in range(n2):
    key=input("Enter the key")
    value=input("Enter the value")

    dict2[key]=value
print("The merged dictionary is:",dict1|dict2)