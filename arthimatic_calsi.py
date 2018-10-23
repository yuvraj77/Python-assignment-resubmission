#Implment a program with arithmetic functions with  case statements.

import sys
def add(x,y):
	return  x+y;
def sub(x,y):
	return x-y;

def mul(x,y):
	return x*y;

def div(x,y):
	return x/y;

def mod(x,y):
	return x%y;

a=int(sys.argv[1])
choice=sys.argv[2]
b=int(sys.argv[3])

if (choice =='+'):
	print("sum is ",add(a,b))

elif (choice =='-'):
	print("sub is ",sub(a,b))

elif (choice =='*'):
	print("mul is ",mul(a,b))

elif (choice =='/'):
	print("div is ",div(a,b))
else:
	print("modulus is",mod(a,b))