s1=input("Enter the 1st string")
s2=input("Enter the 2nd string")
newstring=s2[0] + s1[1:] +" "+ s1[0] + s2[1:]
print(newstring)