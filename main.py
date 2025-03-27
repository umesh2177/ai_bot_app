import logging,os,json,tempfile
import streamlit as st
import duck_duckgo_search
from firestore_db import firestoredb

from google.oauth2 import service_account
import datetime
current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def write_to_firestore(db, question, selected_model, options, summary, key_points, key_Members, key_recent_updates, states):
    # User_Query_Collection
    # Generate document_id using current datetime

    document_id = f"user_query_{current_datetime}"

    # Create data json to store in db
    data = {
        "timestamp": current_datetime,
        "question":question,
        "selected_model": selected_model,
        "selected_options": options,
        "model_output": {
            "summary": summary if "Summary" in options else None,
            "key_points": key_points if "Key Points" in options else None,
            "members": key_Members if "Members" in options else None,
            "recent_updates": key_recent_updates if  "Recent Updates" in options else None,
            "states" : states
        }
    }

    # Write data to Firestore
    return firestoredb.write_data(db=db, collection_name="User_Query_Collection", document_id=document_id, data=data)


def summarize_of_scam(states,question,api_key,selected_model):
    print(states)
    description=f"""You are a helpful Scam News Analyst expert assistant.
        Be remember you have to give the answer in brief summary within provided context
        You reply with proper summary within given context. The news scams should be belongs {states}"""
    return duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
    # print(f"Agent Response: {summary}")
    # return summary

def key_points_of_scam(states,question,api_key,selected_model):
    description="""You are a helpful Scam News Analyst expert assistant .
                Be remember you have to give the answer in points within provided context
                You reply most keys ponits and factors within given context.  The news scams should be belongs {states}"""
    return duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
    # print(f"Agent Response: {key_points}")
    # return key_points

def members_of_scam(states,question,api_key,selected_model):
    description="""You are a helpful Scam News Analyst expert assistant .
                    You reply with the names of all members involved in the scam and provide a brief history of their involvement within the given context. The news scams should be belongs {states}
                """
    return duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
                            # print(f"Agent Response: {key_Members}")
    # return key_Members
    
def recent_updates_of_scam(states,question,api_key,selected_model):
    description="""You are a helpful Scam News Analyst expert assistant .
                   You reply with a brief latest updates within the given context with yearly basis. The news scams should be belongs {states}.
                """
    return duck_duckgo_search.web_search_agent_duckduckgo(api_key_input=api_key,description=description,question=question,model=selected_model,state=states)
                            # print(f"Agent Response: {key_Members}")
    # return key_recent_updates




def option_selector(api_key,db):
    model_options = ["llama3-70b-8192","llama-3.3-70b-specdec","llama-3.3-70b-versatile"]#"llama-3.1-8b-instant","mixtral-8x7b-32768"] 
    selected_model = st.selectbox("Select Model", model_options)

    # Display the selected model
    st.write("Selected Model:", selected_model) 
    question = st.text_input("Enter your question (optional):", "")

    options = st.multiselect(
            "Select options:",
            ["Summary", "Key Points","Members","Recent Updates"]
        )
    
    states = st.selectbox(
            "Select State:",
            ["India","Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]
        )
    summary=""
    key_points=""
    key_Members=""
    key_recent_updates=""

    if st.button("Submit"):
            if not api_key:
                st.warning("Please enter your Groq API Key.")
            else:
                with st.spinner('Analyzing...'):
                    if question and options and states:
                        if "Summary" in options:
                            summary = summarize_of_scam(states,question,api_key,selected_model)
                            st.subheader("Summary:")
                            st.markdown(summary)
                           
                        if "Key Points" in options:
                            key_points = key_points_of_scam(states,question,api_key,selected_model)
                            st.subheader("Key Points:")
                            st.markdown(key_points)
                        if "Members" in options:
                            key_Members = members_of_scam(states,question,api_key,selected_model)
                            st.subheader("Key Members:")
                            st.markdown(members_of_scam(states,question,api_key,selected_model))
                        
                        if "Recent Updates" in options:
                            key_recent_updates = recent_updates_of_scam(states,question,api_key,selected_model)
                            st.subheader("Recent Updates:")
                            st.markdown(key_recent_updates)

                        # Write data to Firestore
                        write_to_firestore(db=db, question=question, selected_model=selected_model, options=options, summary=summary, key_points=key_points, key_Members=key_Members, key_recent_updates=key_recent_updates, states=states)
                      


                    else:
                        st.warning("Please enter a Question,select states or india and select at least one option summary/keys points.")



def contact_us(db):
    if 'toggle_status' not in st.session_state:
        st.session_state['toggle_status'] = False

    # Create the checkbox, using its value as the toggle status
    st.session_state['toggle_status'] = st.checkbox("Contact Us", value=st.session_state['toggle_status'])

    if st.session_state['toggle_status']:# st.button("Contact Us"):
        st.write("Please fill out the form below to get in touch.")

        with st.form("contact_form"):
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Your Email", placeholder="Enter your email address")
            phone_number = st.text_input("Your Phone", placeholder="Enter your phone number")
            subject = st.text_input("Subject", placeholder="Enter the subject of your message")
            message = st.text_area("Message", placeholder="Enter your message here")
            submitted = st.form_submit_button("Submit ")

            if submitted:
                if not name or not email or not subject or not message:
                    st.error("Please fill out all the fields.")
                elif "@" not in email or "." not in email:
                    st.error("Please enter a valid email address.")
                else:
                    try:
                        doc_ref={
                            "name": name,
                            "email": email,
                            "phone": phone_number,
                            "subject": subject,
                            "message": message,
                        }
                        document_id = f"user_contact_{current_datetime}"
                        firestoredb.write_data(db=db, collection_name="User_Contact_Collection", document_id=document_id, data=doc_ref)
                        # Clear the form after successful submission (optional)
                        name = ""
                        email = ""
                        subject = ""
                        message = ""
                        phone_number=""
                        st.success("Thank you for your message! We will get back to you soon.")
                        st.session_state['toggle_status'] = False

                    except Exception as e:
                        st.error(f"Error submitting form: {e}")


def main_app():
    # print(f"keys:{st.secrets.keys()}")
    st.title("Scam News Expert Agent") 
    # api_key = st.text_input("Enter your groq API Key:", "")
    api_key=st.secrets["groq"]["api_key1"]
    key_dict = json.loads(st.secrets["json_key_file"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestoredb.initialize_firestore(creds)
    # st.text(firestoredb.read_data(db=db,collection_name="User_Query_Collection",document_id="user_query_20250126_142937"))
    contact_us(db)
    option_selector(api_key,db)

    

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


def main():
    logger = setup_logger()
    try:
        main_app()
    except Exception as e:
        logger.exception(f"An exception occurred:{e.with_traceback}")
        print(e.with_traceback())

if __name__ == "__main__":
    main()
   