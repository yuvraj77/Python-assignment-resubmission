fp=open("example.txt","r")
lines=fp.readline()
result=''
for ch in lines:
	if ord(ch) >= 65:
            result += chr(ord(ch) + 32)
print(result)
fp.close()