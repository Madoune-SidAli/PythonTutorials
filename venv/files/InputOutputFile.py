import os
#The directory of the current file
print(os.getcwd())

#Modify the directory
os.chdir("the new path")

#list of the files in the current directory
os.listdir('.')

#Open File
myFile = open("file.txt")

#Read File
print(myFile.read())
myFile.close()

#read the lines in the file separating with \n
myFile =  open("file.txt")
print(myFile.readlines())
myFile.close()

#Write in a file
myFile = open("file.txt",'w')
myFile.write("hello world! \n")
myFile.close

#Appende to file
myFile = open("file.txt",'a')
myFile.write("my name is madouen sid ali \n")
myFile.close
