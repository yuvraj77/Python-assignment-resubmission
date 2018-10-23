list=['123','121','132','198']
print(list)
num=int(input("Enter a number in list to find \n"))
temp=0
n=num
while num!=0:
    rem=num%10
    temp=temp*10+rem
    num=num/10
if temp==n:
    print ("it is palindrome",n)
else:
    print ("is not palindrome",n)