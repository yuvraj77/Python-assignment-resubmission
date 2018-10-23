#Implement a program with functions, for finding the area of circle, triangle, square

p=3.147
def area_of_circle():
	x=int(input("enter the radius of circle:\n"))
	return (p*x*x)

def area_of_triangle():
	b=int(input("enter the base:\n"))
	h=int(input("enter the height:\n"))
	return(0.5*b*h)

def area_of_square():
	r=int(input("enter the radius of circle:\n"))
	return(r*r)



def main():

	print("area of circle",area_of_circle())
	print("area of traingle",area_of_triangle())
	print("area of square",area_of_square())
if __name__ == '__main__':
	main()