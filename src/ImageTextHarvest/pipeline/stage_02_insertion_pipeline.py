from src.ImageTextHarvest.components.insertion import Insertion
from src.ImageTextHarvest.logger import logging
class InsertionPipeline:
    def __str__(self):
        pass


    def main(self,submit,user_input):
        input_prompt = """
            imagine Youself as an expert in sql!
            The SQL database has the name STUDENT and has the following columns - 
            NAME VARCHAR(25),
            REG INT,
            TOTAL_AMOUNT FLOAT,
            YEAR INT,
            SEMESTER VARCHAR(10),
            DEPT VARCHAR(10),
            DATE DATE.
            the user will provide you information as query..
            now you have to generate only sql query by yourself to insert the user provided information into the database.
            you have to generate sql query dynamically based on user query.

            for reference user provided values may have this format.: 
            
            name : MD. Sojib
            reg : 20101030
            total amount : 14000
            year : 4th
            semester : 1st
            dept : CSE
            date : 25-10-2023

            one referenec you can follow is
            Insert into STUDENT values ('MD. Sojib',20101030,14000.00,4,'1st','cse',25-10-2023.your response should change based on user provided query.
            if you are unable to find value for any then insert none. remove '''''' this from your response.you have to generate sql query dynamically based on user query.
            if there are no user provided value then insert none for all the columns
            """
        
        if submit:
            insertion_object = Insertion()
            print(user_input)
            response = insertion_object.get_response(query=user_input,prompt=input_prompt)
            insertion_object.insert_into_database(sql=response,db="student.db")

            
