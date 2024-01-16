import sqlite3

## Connectt to SQlite
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

## create the table
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    REG INT,
    TOTAL_AMOUNT FLOAT,
    YEAR INT,
    SEMESTER VARCHAR(10),
    DEPT VARCHAR(10),
    DATE DATE
);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('saimon',20101030,40000.00,4,'1st','cse','1/16/2024')''')

## Disspaly ALl the records

print("The isnerted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()