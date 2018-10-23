tuple1=('apple','mango','banana','orange')
print(tuple1)
tuple2=('carrot','beans','chilli','tomoto')
print(tuple2)
print("list of vegetables and fruits ")
mylist=list(zip(tuple1,tuple2))
a=range(len(mylist))
for i in a:
	print(mylist[i])