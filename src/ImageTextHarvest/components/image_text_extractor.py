import os
import sys
from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException

import google.generativeai as genai
from dotenv import load_dotenv



class ImageTextExtractor:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_image_data(self, uploaded_file):
        try:
            if uploaded_file is not None:
                logging.info("Received the image to extract data in bytes")
                bytes_data = uploaded_file.getvalue()
                image_parts = [
                    {
                        "mime_type": uploaded_file.type,
                        "data": bytes_data
                    }
                ]
                logging.info("Returning the image data.")
                return image_parts
            else:
                error_message = "No file uploaded"
                logging.exception(error_message)
                raise FileNotFoundError(error_message)
        except Exception as e:
            logging.exception(f"Error in get_image_data: {e}")
            raise CustomException(e, sys)

    def get_response(self, query, image, prompt):
        try:
            model = genai.GenerativeModel("gemini-pro-vision")
            logging.info("Loading the model successful.")
            response = model.generate_content([query, image[0], prompt])
            logging.info("Generated response successfully.")
            return response.text
        except Exception as e:
            logging.exception(f"Error in get_response: {e}")
            raise CustomException(e, sys)
