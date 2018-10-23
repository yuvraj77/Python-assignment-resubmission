import csv
count=0
with open("student_record.csv","r") as csv_file:
	csv_reader=csv.reader(csv_file)
	for row in csv_reader:
		count+=1
		print(row)
print("number of students",count)

