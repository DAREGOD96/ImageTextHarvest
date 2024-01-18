import os
import sqlite3
from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException

import google.generativeai as genai
from dotenv import load_dotenv

class Insertion:
    """
    Class for inserting data into a database using a generative model.

    Attributes:
    - None

    Methods:
    - get_response: Get a generative model's response based on a query and prompt.
    - insert_into_database: Insert generated SQL query into a SQLite database.
    """

    def __init__(self):
        """
        Constructor to initialize the Insertion class.

        Loads environment variables and configures the Generative AI API.
        """
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_response(self, query, prompt):
        """
        Get a generative model's response based on a query and prompt.

        Args:
        - query (str): The input query.
        - prompt (str): The prompt for the generative model.

        Returns:
        - str: The generated SQL query.
        """
        try:
            logging.info("Loading the model successfully.")
            model = genai.GenerativeModel("gemini-pro")  # loading the gemini pro model
            response = model.generate_content([query, prompt])
            logging.info("Generated SQL query successfully.")
            print(response.text)
            return response.text
        except Exception as e:
            logging.error(f"Error in get_response: {str(e)}")
            raise CustomException("Error in generative model response generation.")

    def insert_into_database(self, sql, db):
        """
        Insert generated SQL query into a SQLite database.

        Args:
        - sql (str): The SQL query to be inserted.
        - db (str): The path to the SQLite database.

        Returns:
        - None
        """
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            cur.execute(sql)
            logging.info("Data is inserted into the database.")
            con.commit()
        except Exception as e:
            logging.error(f"Error in insert_into_database: {str(e)}")
            raise CustomException("Error in database insertion.")
        finally:
            con.close()