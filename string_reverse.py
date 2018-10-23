ara=input("enter the string\n")

reverse=''
i=len(ara)
while i>0:
	reverse=reverse+ara[i-1]
	i=i-1
print(reverse)