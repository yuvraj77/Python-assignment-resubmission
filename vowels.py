abc=input("enter the string\n")
count=0
for b in abc:

	if (b=='a' or b=='e' or b=='i'or b=='o'or b=='u'):
		count=count+1
print("number of vowels in string is",count)