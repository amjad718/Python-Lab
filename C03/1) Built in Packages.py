import os

#get current path
path = os.getcwd()

#make directory if not exists
if (os.path.exists(path+'NewFolder') == False):
    os.mkdir(path+"/NewFolder")
    print("Folder "+path+"NewFolder created.")
else:
    print(path+"NewFolder exists."
            )
#make file if not exists
if (os.path.exists(path+'/NewFolder/newfile.txt')):
    print("NewFile.txt already exists") 
    f = open(path+"/NewFolder/newfile.txt", "w")
else:
    f = open(path+"/NewFolder/newfile.txt", "x")

f.write("hello world")
f.close()

#read from file
if(os.path.exists(path+'/NewFolder/newfile.txt')):
    f = open(path+'/NewFolder/newfile.txt','r')
    print(f.read())
    f.close()
else :
    print("No such file or directory!")