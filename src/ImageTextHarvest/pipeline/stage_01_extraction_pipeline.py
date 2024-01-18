from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException
from src.ImageTextHarvest.components.image_text_extractor import ImageTextExtractor
import sys
import streamlit as st

class ExtractionPipeline:
    """
    Class representing the extraction pipeline for extracting information from an image.

    Attributes:
    - None

    Methods:
    - main: Main method to execute the extraction pipeline based on user input.
    """

    def __init__(self):
        """
        Constructor to initialize the ExtractionPipeline class.
        """
        pass

    def main(self, user_uploaded_file, submit):
        """
        Main method to execute the extraction pipeline based on user input.

        Args:
        - user_uploaded_file (FileUploader): The uploaded image file.
        - submit (bool): Flag indicating whether the form has been submitted.

        Returns:
        - str: The extracted information from the image.
        """
        try:
            query = "extract name , reg , total amount, year, semester, dept, date from the image"

            input_prompt = """
            You are an expert in understanding invoices. We will upload an image as an invoice,
            and you will have to collect the following information from the image: 
            name, reg, total amount, year, semester, dept, date.
            
            Your response should be in the following format:
            Example:
            name : MD. Sojib
            reg : 20101030
            total amount : 14000
            year : 4th
            semester : 1st
            dept : CSE
            date : 25-10-2023
            
            Remove extra space before the name.
            """

            if submit:
                image_data_extractor_object = ImageTextExtractor()
                image_data = image_data_extractor_object.get_image_data(uploaded_file=user_uploaded_file)
                response = image_data_extractor_object.get_response(query=query, image=image_data, prompt=input_prompt)
                return response
            else:
                st.warning("Please upload an image before submitting.")

        except Exception as e:
            logging.exception(e)
            raise CustomException(e, sys)
