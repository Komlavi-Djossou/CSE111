import mysql.connector as mysql

# Variables
host = "localhost"
user = "root"
password = ""



# Connecting to mysql
try:
    db = mysql.connect(host=host,user=user, password=password)
    print("Connected Successsfully")
except Exception as e:
    print(e)
    print("Failed to connect")

#  Connecting to an existing database
db1 = mysql.connect(host=host,user=user, password=password,database="students")
try:
    print("Connected to students database")
except Exception as e:
    print("Could not connect to students database")
    print(e)


def main():

    # print out database created
    # db_creater = create_db()
    # print(db_creater)

    # print out all databases
    # dv_viewer = view_db() 
    # print(dv_viewer)

    # print out tables
    db_table = create_table()
    print(db_table)

    # print out tables in database
    tb_add = add_data()
    print(tb_add)

    # print out multiple fields added to the table
    add_fields = add_multiple_field()
    print(add_fields)

    # print out selected table
    # slct_table = display_selected_table()
    # print(slct_table)

    # print columns from french table
    display_cl = display_columns()
    print(display_cl)

# Creating a database
def create_db():
    try:
        command_handler = db.cursor()
        command_handler.execute("CREATE DATABASE students")
        print("Students database has been created")
    except Exception as e:
        print("Could not create database")
        print(e)

# # Viewing all databases
# def view_db():
#     try:
#         command_handler = db.cursor()
#         command_handler.execute("SHOW DATABASES")
#         print("These are the available databases")
#         for database in command_handler:
#             print(database)
#     except Exception as e:
#         print("Could not show all databases")
#         print(e)



# Creating tables in a database
def create_table():
    try:
        command_handler = db1.cursor()
        command_handler.execute("CREATE TABLE french (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), class VARCHAR(255))")
        print("Table created successfully")
    except Exception as e:
        print("Could not create table")
        print(e)

# Showing tables in the database selected
#     command_handler.execute("SHOW TABLES")
#     print("Showing all tables in the database")
#     for table in command_handler:
#         print(table)

# # adding data into the table
def add_data():
    try:
        command_handler = db1.cursor()
        query = "INSERT INTO french(name,class) VALUES (%s,%s)"
        query_vals = ("Andre", "Form Three")
        command_handler.execute(query,query_vals)
        db1.commit()
        print(command_handler.rowcount, "record inserted")
    except Exception as e:
        print("Could not insert columns into table")
        print(e)



# # Adding multiple fields of data
def add_multiple_field():
    try:
        command_handler = db1.cursor()
        query = "INSERT INTO french(name,class) VALUES (%s,%s)"
        query_vals = [("Daniel", "Form One"),
        ("Chioma", "Form Two")
        ]
        command_handler.executemany(query,query_vals)
        db1.commit()
        print(command_handler.rowcount, "record insterted")

    except Exception as e:
        print("Could not execute query")
        print(e)


# # # /Display all records from selected table
# def display_selected_table():
#     command_handler = db1.cursor()
#     command_handler.execute("SELECT * from french")
#     records = command_handler.fetchall()
#     print("Displaying records")
#     for record in records:
#         print(record)

#  Displaying specific columns from the table selected
def display_columns():
    try:
        command_handler = db1.cursor()
        command_handler.execute("SELECT name from french")
        records = command_handler.fetchall()
        print("Displaying names from table : french")
        for record in records:
            print(record)
        # return record
    except Exception as e:
        print("Could not select name from french")
        print(e)



if __name__ == "__main__":
    main()