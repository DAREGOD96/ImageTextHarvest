from src.ImageTextHarvest.components.insertion import Insertion
from src.ImageTextHarvest.logger import logging

class InsertionPipeline:
    """
    Class representing the insertion pipeline for generating SQL queries and inserting data into a database.

    Attributes:
    - None

    Methods:
    - main: Main method to execute the insertion pipeline based on user input.
    """

    def __init__(self):
        """
        Constructor to initialize the InsertionPipeline class.
        """
        pass

    def main(self, submit, user_input):
        """
        Main method to execute the insertion pipeline based on user input.

        Args:
        - submit (bool): Flag indicating whether the form has been submitted.
        - user_input (str): User-provided input containing information to be inserted into the database.

        Returns:
        - None
        """
        input_prompt = """
        Imagine yourself as an expert database engineer. There is a database named as student.db with following columns:
        NAME VARCHAR(25),
        REG INT,
        TOTAL_AMOUNT FLOAT,
        YEAR INT,
        SEMESTER VARCHAR(10),
        DEPT VARCHAR(10),
        DATE DATE.

        The user will pass you information as input. Your job is to generate an SQL query for inserting that information
        into the database by converting English questions to SQL query. You are restricted to only generate the appropriate SQL query.
        
        User input example:
        name : MD. Sojib
        reg : 20101030
        total amount : 40000
        year : 4th
        semester : 2nd
        dept : CSE
        date : 03-01-2023

        Your response example:
        Insert into STUDENT values ('MD. Sojib', 20101030, 40000.00, 4, '2nd', 'cse', '03-01-2023')

        Your response should change dynamically based on the user-provided query.
        Also, the SQL code should not have ``` in the beginning or end and "sql" word in the output.
        """
        
        if submit:
            insertion_object = Insertion()
            if user_input:
                response = insertion_object.get_response(query=user_input, prompt=input_prompt)
                insertion_object.insert_into_database(sql=response, db="student.db")
            else:
                print("User input is not found!")
