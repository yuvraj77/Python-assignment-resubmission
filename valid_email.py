import re
 
input = input("Enter an input string:")
m = re.match('[^@]+@[^@]+\.[^@]+',input)
 
if m:
    print("email is valid")
else:
    print("email is not valid")