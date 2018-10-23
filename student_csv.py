f=open("student_csv.csv","r")
lines=f.readlines()
count=0
for i in lines:
    count=count+1
    print(i)
print("number of students is",count)