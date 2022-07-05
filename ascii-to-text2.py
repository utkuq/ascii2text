#clear the screen
import os
os.system("cls")
#os.system("clear")

#get ascii code from user
ascii = input("Enter the ascii characters with a space: ")
newascii = ascii.split()

#convert ascii code from string to integer
ascii = [int(x) for x in newascii]

#convert ascii code to string
text = [chr(x) for x in ascii]

#convert the string list to a readable string
newtext = "".join(str(x) for x in text)

print(newtext)   