fp=open("example.txt","r")
lines=fp.readline()
g=''
y=''
for ch in lines:
	if ord (ch) >= 97 and ord(ch) <= 122:
		x = ord(ch) - 32
		y = chr (x)
		g = g + y
	else :
		x = ord(ch) + 32
		y = chr (x)
		g = g + y
print(g)
fp.close()