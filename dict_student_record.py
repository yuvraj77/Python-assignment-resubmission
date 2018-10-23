import csv
name=input("enter name of student\n")
branch=input("enter the branch\n")
with open("student.csv","a+") as csv_file:
	student_record=csv.writer(csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	student_record.writerow([name,branch])
with open("student.csv","r") as csv_file:
	csv_reader=csv.reader(csv_file)
	dictonary=dict(csv_reader)
print(dictonary)