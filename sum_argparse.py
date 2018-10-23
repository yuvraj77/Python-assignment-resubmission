import sys
import argparse
parser = argparse.ArgumentParser(description='CLA based calculator')
parser.add_argument('-a','--num1', type=int,required=True)
parser.add_argument('-c','--choice',required=True)
parser.add_argument('-b','--num1',type=int,required=True)

args=parser.parse_args()
print(args)
if(args.c == '+'):
	print("addition",num1 + num2)
elif(args.c == '-'):
	print("substraction",num1 - num2)
elif(args.c == '*'):
	print("multiplication",num1 * num2)
elif(args.c == '/'):
	print("division",num1 / num2)
else:
	print("modulus",num1 + num2)