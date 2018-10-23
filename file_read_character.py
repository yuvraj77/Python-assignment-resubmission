fp=open("example.txt","r")
lines=fp.readline()
for ch in lines:
	print(ch)
fp.close()