from retrieve_data import create_db, create_table, add_multiple_field, display_columns
import pytest
import mysql.connector as mysql

# Variables
host = "localhost"
user = "root"
password = ""

# check if students database has been created
def test_create_db():
    db1 = mysql.connect(host=host,user=user, password=password,database="students")
    command_handler = db1.cursor()
    command_handler.execute("SHOW DATABASES LIKE 'students' ") 
    records = command_handler.fetchall()
    assert ('students',) in records

# check if french table exist in the students database
def test_create_table():
    db1 = mysql.connect(host=host,user=user, password=password,database="students")
    command_handler = db1.cursor()
    command_handler.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'students' AND table_name = 'french' ") 
    record = command_handler.fetchall()
    assert record == [(1,)]


# check if french table has been updated with additional data
def test_add_multiple_field():
    db1 = mysql.connect(host=host,user=user, password=password,database="students")
    command_handler = db1.cursor()
    command_handler.execute("SELECT name, class from french")
    records = command_handler.fetchall()    
    assert ("Daniel", "Form One") in records and ("Chioma", "Form Two") in records

# test if selected table displays specific columns 
def test_display_columns():
    db1 = mysql.connect(host=host,user=user, password=password,database="students")
    command_handler = db1.cursor()
    command_handler.execute("SELECT name from french")
    records = command_handler.fetchall()
    assert ('Andre',) in records and ('Daniel',) in records and ('Chioma',) in records

pytest.main(["-v", "--tb=line", "-rN", "test_retrieve_data.py"])