# Create a file with patients personal records. Check for the names are properly entered. Means, no number or symbols allowed.

import sys
import csv

def main():
	patient_name=input("enter name of patient\n")
	patient_age=int(input("enter the age\n"))
	patient_phone_no=int(input("enter the phone number\n"))

	with open("patient_record.csv","a+") as csv_file:
		patient_record=csv.writer(csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_file.seek(0)
		first_char=csv_file.read(1)
		if not first_char:
			patient_record.writerow(['patient_name','patient_age','patient_phone_no'])
		patient_record.writerow([patient_name,patient_age,patient_phone_no])
	print("records are written into patient_record.csv\n")

if __name__=="__main__":
	main()