import streamlit as st
from  src.ImageTextHarvest.pipeline.stage_01_extraction_pipeline import ExtractionPipeline

st.set_page_config(page_title="Image text extractor")
st.subheader("Upload an image and extract information")
user_uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit = st.button("Extract information")
response = st.text_area("The Response is")


extraction_object = ExtractionPipeline()
extraction_object.main(user_uploaded_file,submit,response_label=response)


