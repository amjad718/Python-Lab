# # Generating Positive list of integers

list=[]
pos=[]
n=int(input("Enter the size of the list"))
print("Enter the elements")
for i in range(n):
    num=int(input())
    list.append(num)
for i in list:
    if(i>0):
        pos.append(i)
print("(a) The positive numbers in the entered list is:",pos)

# # Square of N numbers

print("The square of the entered size of the list is:",n*n)

# # Form a list of vowels selected from a given word 

vowel=[]
string=input("Enter the string")
for i in string:
    if i in ('a','e','i','o','u'):
        vowel.append(i)
print("The vowels available in the string is",vowel)
# # word=input("Enter the word you want to find the vowel")
# # for i in string:
# #     while(word==i):
# #         letter=word.split()
# #         i=i+1
# #         for i in letter:
# #             if(i in )

# # List ordinal value of each element of a word (Hint: use ord() to get ordinal values) 

s=[]
ordinal=input("Enter the word")
for i in ordinal:
    s.append(ord(i))
print(s)