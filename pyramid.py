rows = input("Enter number of rows ")
rows = int (rows)
m = (2 * rows) - 2
for i in range (0, rows):
    for j in range(0, m):
        print(end=' ')
    m=m-1
    for j in range(0, i + 1):
        print(".", end=' ')
    print("\r")