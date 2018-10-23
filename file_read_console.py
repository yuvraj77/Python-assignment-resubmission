import sys

b=sys.argv[1]
c=sys.argv[2]

fp=open("example.txt","a+")
fp.write(b)
fp.write(c)
line=fp.read()
for i in line:
	print(i)
fp.close()



