from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException
from src.ImageTextHarvest.components.image_text_extractor import ImageTextExtractor
import sys
import streamlit as st
from PIL import Image


class ExtractionPipeline:
    def __init__(self):
        pass

    def main(self,user_uploaded_file,submit):
        try:

            query = "extract name , reg , total amount, year,semester,dept,date from the image"

            input_prompt = """
            You are an expert in understanding invoices. We will upload a a image as invoice
            and you will have to collect the following information from the image.name , reg , total amount, year,semester,dept,date.
            your response will be in the following format.
            example:
            name : Md Sojib
            reg : 20101030
            total amount : 40000
            year : 4th
            semester : 2nd
            dept : cse
            date : 3-01-2024 
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


