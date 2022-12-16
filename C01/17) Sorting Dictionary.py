n=int(input("Enter the size of the dictionary"))
dict={}
for i in range(n):
    key=input("Enter the key")
    value=input("Enter the value")

    dict[key]=value
print("Ascending Order:",sorted(dict.items()))
print("Descending order:",sorted((dict.items()) ,reverse=True))