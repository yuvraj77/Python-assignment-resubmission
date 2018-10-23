fp=open("example.txt","r")
lines=fp.readline()
count=0
for ch in lines:
	if(ch=='a' or ch=='e' or ch=='ch' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='ch' or ch=='O' or ch=='U'):
		count=count+1
print("count of vowels ch ",count)
fp.close()