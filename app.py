import streamlit as st
from src.ImageTextHarvest.pipeline.stage_01_extraction_pipeline import ExtractionPipeline
from src.ImageTextHarvest.pipeline.stage_02_insertion_pipeline import InsertionPipeline
from PIL import Image
import copy

st.set_page_config(page_title="Image text extractor")
st.subheader("Upload an image and extract information")

# Declare variables for storing state
user_uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
submit = st.button("Extract information")
response = ""

if user_uploaded_file is not None and submit:
    image = Image.open(user_uploaded_file)
    # Extract information
    extraction_object = ExtractionPipeline()
    response = extraction_object.main(user_uploaded_file, submit)

# Use a form to handle the insertion input
new_variable = copy.deepcopy(response)
with st.form("insertion_form"):
    query = st.text_input("Edit the text:", response)
    submit2 = st.form_submit_button("Insert information")
    if submit2:
        insertion_object = InsertionPipeline()
        print(query)
        insertion_object.main(submit=submit2, user_input=query)
        st.success("Information inserted successfully!")

# Handle insertion only if the form is submitted


# Print the type of edit_option
st.text(f"Type of edit_option: {type(query)}")
