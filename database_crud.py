
import mysql.connector
import sys
from datetime import datetime 
global conn,cursor;

conn= mysql.connector.connect(host="localhost",user="root")


def connection():
    
    if conn.is_connected():
        print("Connection Established");
    else:
        print("Not Conected, check ..")

def create_database():
    if conn.is_connected():
        cursor=conn.cursor();
        cursor.execute("CREATE DATABASE CRUD_181040013")
        print("Database created");

    #conn.close()
    
def create_table():
    conn= mysql.connector.connect(host="localhost",user="root",database="CRUD_181040013")

    if conn.is_connected():
        cursor = conn.cursor();
        cursor.execute("CREATE TABLE reg_181040013(id INT(20) PRIMARY KEY,fname VARCHAR(50), lname VARCHAR(50),dob DATE)")
        print("Table created successfully")

def insertvalue(id,fname,lname,dob):
    conn= mysql.connector.connect(host="localhost",user="root",database="CRUD_181040013")

    if conn.is_connected():
        query = "INSERT INTO reg_181040013(id,fname,lname,dob) VALUES(%s,%s,%s,%s)"
        details= (id,fname,lname,dob);
        print(details)
        cursor = conn.cursor(); 
        cursor.execute(query,details);
        conn.commit();
        print("Inserted successfully")

def retreiveall():
    conn= mysql.connector.connect(host="localhost",user="root",database="CRUD_181040013")
    query = "SELECT * FROM reg_181040013";
    cursor =  conn.cursor();
    cursor.execute(query)
    rows = cursor.fetchall();
    for row in rows:
        print(row);

def update_table():
    conn= mysql.connector.connect(host="localhost",user="root",database="CRUD_181040013")
    query = "UPDATE reg_181040013 SET fname='yuvi' WHERE fname='yuvaraj'";
    cursor =  conn.cursor();
    cursor.execute(query)
    conn.commit()
    print("table updated")


def truncate_table():
    conn= mysql.connector.connect(host="localhost",user="root",database="CRUD_181040013")
    query="DROP TABLE reg_181040013"
    cursor=conn.cursor();
    cursor.execute(query)
    print("Table Dropped")


def main():
    connection();
    
    while True:
        print("\nEnter your choice:");
        print("createdatabase-->1:")
        print("create table-->2:")
        print("insertion-->3:")
        print("retrieve details-->4")
        print("truncatetable-->5")
        print("update table-->6")
        print("Quit-->q")
        choice = input("Enter the option:")
        if choice == '1':
            create_database()
        if choice == '2':
            create_table()
        if choice == '3':
            id=input("Enter id:");
            fname=input("enter first name:");
            lname=input("enter last name:");
            dob=input("enter Date of birth in (YYYY-MM-DD)format:");
            insertvalue(id,fname,lname,dob)
        if choice=='4':
            retreiveall()
        if choice=='5':
            truncate_table()
        if choice=='6':
            update_table()
        if choice == 'q':
            sys.exit()
        



if __name__ == "__main__":
    main();
    
