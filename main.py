import logging,os,json,tempfile
import streamlit as st
import duck_duckgo_search
from firestore_db import firestoredb

from google.oauth2 import service_account
import datetime




def main_app():
    # print(f"keys:{st.secrets.keys()}")

    st.title("News Expert Agent APP")
    # api_key = st.text_input("Enter your groq API Key:", "")
    
    api_key=st.secrets["groq"]["api_key1"]

    key_dict = json.loads(st.secrets["json_key_file"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestoredb.initialize_firestore(creds)
    # print(firestoredb.read_data(db=db,collection_name="prabhat_khabar",document_id="29_DEC_2024"))

    model_options = ["llama3-70b-8192","llama-3.3-70b-versatile"]#"llama-3.1-8b-instant","mixtral-8x7b-32768"] 
    selected_model = st.selectbox("Select Model", model_options)

    # Display the selected model
    st.write("Selected Model:", selected_model) 
    question = st.text_input("Enter your question (optional):", "")

    options = st.multiselect(
            "Select options:",
            ["Summary", "Key Points","Members"]
        )
    
    states = st.selectbox(
            "Select State:",
            ["India","Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]
        )


    if st.button("Submit"):
            if not api_key:
                st.warning("Please enter your Groq API Key.")
            else:
                with st.spinner('Analyzing...'):
                    if question and options and states:
                        if "Summary" in options:
                            print(states)
                            description=f"""You are a helpful Scam News Analyst expert assistant.
                             Be remember you have to give the answer in brief summary within provided context
                             You reply with proper summary within given context. The news scams should be belongs {states}"""
                            summary = duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
                            # print(f"Agent Response: {summary}")
                            st.subheader("Summary:")
                            st.markdown(summary)

                        if "Key Points" in options:
                            description="""You are a helpful Scam News Analyst expert assistant .
                            Be remember you have to give the answer in points within provided context
                        You reply most keys ponits and factors within given context.  The news scams should be belongs {states}"""
                            key_points = duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
                            # print(f"Agent Response: {key_points}")
                            st.subheader("Key Points:")
                            st.markdown(key_points)
                        if "Members" in options:
                            description="""You are a helpful Scam News Analyst expert assistant .
                             You reply with the names of all members involved in the scam and provide a brief history of their involvement within the given context. The news scams should be belongs {states}
                            """
                            key_Members = duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
                            # print(f"Agent Response: {key_Members}")
                            st.subheader("Key Members:")
                            st.markdown(key_Members)


                        
                        # User_Query_Collection
                        # Generate document_id using current datetime
                        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                        document_id = f"user_query_{current_datetime}"

                        # Create data json to store in db
                        data = {
                            "question":question,
                            "selected_model": selected_model,
                            "selected_options": options,
                            "model_output": {
                                "summary": summary if "Summary" in options else None,
                                "key_points": key_points if "Key Points" in options else None,
                                "members": key_Members if "Members" in options else None,
                                "states" : states
                            }
                        }

                        # Write data to Firestore
                        firestoredb.write_data(db=db, collection_name="User_Query_Collection", document_id=document_id, data=data)


                    else:
                        st.warning("Please enter a Question,select states or india and select at least one option summary/keys points.")





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

if __name__ == "__main__":
    logger = setup_logger()


    try:
        main_app()
    except Exception as e:
        logger.exception(f"An exception occurred:{e.with_traceback}")
        print(e.with_traceback())