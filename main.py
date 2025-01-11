import streamlit as st
import time
from web_scraper.website_scraper import web_url_scraper
import pandas as pd
import logging

def main_app():
        st.title("News Expert Agent APP")
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


                        new_data = pd.DataFrame({
                            "URL": [url],
                            "Question": [question],
                            "Bot Summary": [summary],
                            "Key Points": [key_points], #Store key points as a list
                        })

                        # Load existing data (if any)
                        try:
                            df = pd.read_csv("user_inputs.csv")
                        except FileNotFoundError:
                            df = pd.DataFrame(columns=["URL", "Question", "Bot Summary", "Key Points"])

                        # Append new data to the DataFrame
                        df = pd.concat([df, new_data], ignore_index=True)

                        # Save the updated DataFrame to CSV
                        df.to_csv("user_inputs.csv", index=False)


                        # if question:
                        #     # Add logic to answer the question based on the extracted text
                        #     st.subheader("Answer to your question:")
                        #     # ... (your question-answering logic here) ...
                        #     st.write("Answer will be displayed here.")





def setup_logger(log_file='logger.log'):
    """
    Sets up a logger to write logs to the specified file.

    Args:
        log_file (str, optional): The name of the log file. Defaults to 'logger.log'.

    Returns:
        logging.Logger: The configured logger object.
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)  # Set the handler's logging level (can be different from the logger's level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

# Example usage:
if __name__ == "__main__":
    logger = setup_logger()

    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

    try:
        main_app()
    except Exception as e:
        logger.exception("An exception occurred:") 