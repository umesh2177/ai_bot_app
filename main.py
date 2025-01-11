import streamlit as st
import time
from web_scraper.website_scraper import web_url_scraper

st.title("Scam News APP")
# with st.form("my_form"):

api_key = st.text_input("Enter your groq API Key:", "")

model_options = ["llama3-70b-8192","llama-3.3-70b-versatile", "llama-3.1-8b-instant" ]#"mixtral-8x7b-32768"] 
selected_model = st.selectbox("Select Model", model_options)

# Display the selected model
st.write("Selected Model:", selected_model) 

url = st.text_input("Enter URL:", "")
question = st.text_input("Enter your question (optional):", "")

options = st.multiselect(
    "Select options:",
    ["Summary", "Key Points"]
)


if st.button("Submit"):
    if not api_key:
        st.warning("Please enter your Groq API Key.")
    else:
        with st.spinner('Analyzing...'):
            # time.sleep(2)
            if url:
                Website_Scraper= web_url_scraper(web_url=url,api_key=api_key)
                if "Summary" in options:
                    summary = Website_Scraper.get_summary(question,selected_model)
                    st.subheader("Summary:")
                    st.write(summary)

                if "Key Points" in options:
                    key_points = Website_Scraper.get_key_points(question,selected_model)
                    st.subheader("Key Points:")
                    st.write(key_points)

                # if question:
                #     # Add logic to answer the question based on the extracted text
                #     st.subheader("Answer to your question:")
                #     # ... (your question-answering logic here) ...
                #     st.write("Answer will be displayed here.")