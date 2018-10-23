 #Implement a program for above using getopt.



import sys
import getopt

argv = sys.argv[1:]

a=int(sys.argv[1])
choice=sys.argv[2]
c=int(sys.argv[3])
opts, args = getopt.getopt(argv,'a:choice:b' ['--num1','--op','--num2'])
print(opts)
print(args)

for (o,a) in opts:
	if a==num1:
		













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