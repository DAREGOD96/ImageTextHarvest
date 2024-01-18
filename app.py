import streamlit as st
from src.ImageTextHarvest.pipeline.stage_01_extraction_pipeline import ExtractionPipeline
from src.ImageTextHarvest.pipeline.stage_02_insertion_pipeline import InsertionPipeline
from PIL import Image

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.response = ""

st.set_page_config(page_title="Image text Harvest")
st.subheader("Upload an image and extract information")

# Declare variables for storing state
user_uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit = st.button("Extract information")

if user_uploaded_file is not None and submit:
    extraction_object = ExtractionPipeline()
    st.session_state.response = extraction_object.main(user_uploaded_file, submit)
elif user_uploaded_file is None and submit:
    st.warning("Please upload a image to procced")


# Use a form to handle the insertion input
with st.form("insertion_form"):
    query = st.text_area("Edit the text:", st.session_state.response)
    submit2 = st.form_submit_button("Insert information")
    if submit2:
        if query:
            insertion_object = InsertionPipeline()
            insertion_object.main(submit=submit2, user_input=query)
            st.success("Information inserted successfully!")
        else:
            st.warning("No query is found")

