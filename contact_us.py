
import logging,os,json,tempfile
import streamlit as st
import duck_duckgo_search
from firestore_db import firestoredb

from google.oauth2 import service_account
import datetime
current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def contact_us(db):
    st.write("Please fill out the form below to get in touch.")

    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        phone_number = st.text_input("Your Phone", placeholder="Enter your phone number")
        subject = st.text_input("Subject", placeholder="Enter the subject of your message")
        message = st.text_area("Message", placeholder="Enter your message here")
        submitted = st.form_submit_button("Submit")

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
                    st.success("Thank you for your message! We will get back to you soon.")
                    document_id = f"user_contact_{current_datetime}"

                    firestoredb.write_data(db=db, collection_name="User_Contact_Collection", document_id=document_id, data=doc_ref)
                    # Clear the form after successful submission (optional)
                    name = ""
                    email = ""
                    subject = ""
                    message = ""
                    phone_number=""
                except Exception as e:
                    st.error(f"Error submitting form: {e}")
if st.button("Back to Main"):
    if "next_page" in st.session_state:
        del st.session_state.next_page
    st.rerun()

