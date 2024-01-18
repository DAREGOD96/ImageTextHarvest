import os
import sys
from src.ImageTextHarvest.logger import logging
from src.ImageTextHarvest.exception import CustomException

import google.generativeai as genai
from dotenv import load_dotenv

class ImageTextExtractor:
    """
    Class for extracting text data from an image using a generative model.

    Attributes:
    - None

    Methods:
    - get_image_data: Get image data in bytes from the uploaded file.
    - get_response: Get a generative model's response based on a query, image, and prompt.
    """

    def __init__(self):
        """
        Constructor to initialize the ImageTextExtractor class.

        Loads environment variables and configures the Generative AI API.
        """
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_image_data(self, uploaded_file):
        """
        Get image data in bytes from the uploaded file.

        Args:
        - uploaded_file (FileUploader): The uploaded image file.

        Returns:
        - list: A list containing image data in parts (mime_type and data).
        """
        try:
            if uploaded_file is not None:
                logging.info("Received the image to extract data in bytes.")
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
                error_message = "No file uploaded."
                logging.exception(error_message)
                raise FileNotFoundError(error_message)
        except Exception as e:
            logging.exception(f"Error in get_image_data: {e}")
            raise CustomException(e, sys)

    def get_response(self, query, image, prompt):
        """
        Get a generative model's response based on a query, image, and prompt.

        Args:
        - query (str): The input query.
        - image (list): A list containing image data in parts (mime_type and data).
        - prompt (str): The prompt for the generative model.

        Returns:
        - str: The generated response text.
        """
        try:
            model = genai.GenerativeModel("gemini-pro-vision")
            logging.info("Loading the model successfully.")
            response = model.generate_content([query, image[0], prompt])
            logging.info("Generated response successfully.")
            return response.text
        except Exception as e:
            logging.exception(f"Error in get_response: {e}")
            raise CustomException(e, sys)
