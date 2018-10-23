 #Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete.

dict={181040012:'arsh',181040013:'ara',
       181040014:'push',
       181040015:'bru'}
print(dict)
dict['181040016']='govin'
print(dict)
dict.pop(181040012)
print(dict)
del dict['181040016']
print(dict)  
for x,y in dict.items():
	print(x,y)
