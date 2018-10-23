import sys

def add(a,b):
	return(a + b);

def subb(a,b):
	return(a - b);

def mul(a,b):
	return(a * b);

def div(a,b):
	return(a / b);

def mod(a,b):
	return(a % b);

try:
	num1=int(input("enter the first number\n"))
	num2=int(input("enter the second number\n"))
	choice=int(input("enter your choice 1=add: 2=subb: 3=mul:  4=div: 5=mod: q=exit \n"))
except:
	print("error occured")

if choice ==1:
	print(add(num1,num2))


elif choice ==2:
	print(subb(num1,num2))

elif choice ==3:
	print(mul(num1,num2))

elif choice ==4:
	print(div(num1,num2))

elif choice ==5:
	print(mod(num1,num2))

else:
	sys.exit()
