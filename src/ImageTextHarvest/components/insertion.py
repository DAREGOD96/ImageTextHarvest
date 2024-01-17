import os
import sys
import sqlite3
from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException

import google.generativeai as genai
from dotenv import load_dotenv

class Insertion:
    def __str__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_response(self,query, prompt):
        logging.info("Loading the model successful.")
        model = genai.GenerativeModel("gemini-pro")  # loading the gemini pro model

        response = model.generate_content([query, prompt])
        logging.info("Generated sql query successfully.")
        print(response.text)
        return response.text

    
    def insert_into_database(self,sql,db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(sql)
        logging.info("Data is inserted into database")
        con.commit()
        con.close()
        print(f"following data inserted {sql}")

