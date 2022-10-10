
from tkinter import *
import mysql.connector as mysql
import re


# A function to create a connection with mysql

def build_connection(hostname, username, password, db):
    try:
        connection = mysql.connect(host=hostname, user=username, passwd=password, database=db)
        return connection
    except:
        raise Exception("Couldn't make the connection")


# Email validity checking function : checks the format of the email address given
def valid_email(email):
    pattern = r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9]+[.][a-z]{2,3}"
    invalid_pattern = r"[._@]{2}"
    if re.fullmatch(pattern, email) and not re.findall(invalid_pattern, email):
        return True
    else:
        return False

# for _  in range(100):
#     p = input("P: ")
#     if valid_email(p):
#         print(True)
#     else:
#         print(False)

def valid_password(password):
    pattern = r"[0-9]"
    if len(password) >= 8  and password.isalnum() and re.findall(pattern , password):
        return True
    else:
        return False


# def login():
#     try:
#         password = None
#         while 1:
#             conn = build_connection("localhost", "root", "23080518", "data")
#             cursor = conn.cursor()
#             email = input("enter a valid email id: ")
#             if not valid_email(email):
#                 print("Please enter a valid email id")
#                 continue
#             cursor.execute(f" SELECT * from accounts Where email = '{email}'")
#             result = cursor.fetchone()
#             if not result:
#                 print("No such account linked with this email id was found")
#                 continue
#             password = result[1]
#             conn.close()
#             cursor.close()
#             break
#
#         for _ in range(5):
#             entered_password = input("Enter the password to your account: ")
#             if password == entered_password:
#                 show_details(email)
#                 return 1
#             print("The password is incorrect")
#
#         print("Please try again later")
#         return 0
#
#     except :
#         print("Couldn't login right now please try again later")


def register():
    global conn , cursor
    try:

        conn = build_connection("localhost", "root", "23080518", "data")
        cursor = conn.cursor()
        while(1):
            email = input("enter a valid email id: ")
            if not valid_email(email):
                print("Please enter a valid email id")
                continue
            cursor.execute(f"Select email from accounts where email = '{email}'")
            result = cursor.fetchone()
            if result:
                print("We already have an account with this email id , login or chose another email.")
            else:
                break
        print("Password must be at least 8 char long and must contain a number")
        while(1):
            password = input("Please enter your desired password for this account: ")
            c_password = input("Enter your password again to verify")
            if not valid_password(password) or password != c_password:
                continue

    except:
        print("Couldn't register you right now please try again later")

    finally:
        conn.close()
        cursor.close()


# The Connection and the Cursor has been initialized here

# conn = build_connection("localhost", "root", "23080518", "data")
# cursor = conn.cursor()

# # We will create the database named DATA if it is not there

# cursor.execute("SHOW Databases like 'data' ")
# found = False
# for database in cursor:
#     if database[0] == "data":
#         # print("Database 'data' is already present")
#         found = True
# if not found:
#     cursor.execute("CREATE DATABASE IF NOT EXIST data;")
#     print("A new database 'data' was created")
# cursor.close()

# # We will create a table named 'accounts' in the database of data


# conn = build_connection("localhost", "root", "23080518", "data")
# cursor = conn.cursor()
# cursor.execute("""
#                     CREATE TABLE IF NOT EXISTS accounts (email VARCHAR(255) PRIMARY KEY UNIQUE,
#                     password VARCHAR(255) NOT NULL,
#                     name VARCHAR(50) NOT NULL,
#                     age INTEGER NOT NULL,
#                     phone_number INTEGER UNIQUE NOT NULL ,
#                     gender VARCHAR(20 ));""")



def login(window , email , password):
    try:
        if not valid_email(email):
            raise "Please enter a valid Email Address"
        conn =  build_connection("localhost", "root", "23080518", "data")
        cursor.execute(f" SELECT * from accounts Where email = '{email}'")
        result = cursor.fetchone()
        if not result:
            raise "No account found linked with this Email Address"
        password1 = result[1]
        cursor.close()
        conn.close()
        if password1 != password:
           raise "Invalid Email or Password"
        label = Label(window , text="Connection was successful").place(x= 450 , y= 150)
    except:
        err = Label(window , text="Invalid Username or Password" ,fg= "red" , bg ="White")
        err.place(x= 410 , y= 150)
