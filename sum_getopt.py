import sys
import getopt

opts,args=getopt.getopt(sys.argv[1:],"a:c:b:",["num1=","choice=","num2="])
print(opts)
print(args)

print(opts)
for (o,a) in opts:
	if o in ('-a','--num1'):
		print("num1 entered",a)
		num1 = a
	elif o in ('-c','--choice'):
		print("choice entered",a)
		choice = a
	elif o in ('-b','--num2'):
		print(a)
		num2 = a
num1=int(num1)
num2=int(num2)
if (choice =='+'):
	print("addition",num1 + num2)
elif (choice =='-'):
	print("substract",num1 - num2)
elif (choice =='*'):
	print("mul",num1 * num2)
elif (choice =='/'):
	print("div",num1 / num2)
else :
	print("modulus",num1 % num2)