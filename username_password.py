 #Implement a python code to get username and password. Validate using regular experssions. Conditions: Username should not exceed 10 characters. It can't have symbols. Password should have one upper case, one lower case, one number , one symbol and length minimum of 6.

import re
p= input("Input your password\n")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")