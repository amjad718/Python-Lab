n=input("Enter the string in which you want the change \n")
def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1
print("The modified string is \t",change_char(n))

