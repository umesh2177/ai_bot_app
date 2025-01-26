states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]


import streamlit as st
import json
import duck_duckgo_search
from firestore_db import firestoredb

from google.oauth2 import service_account
import datetime

api_key=st.secrets["groq"]["api_key"]
key_dict = json.loads(st.secrets["json_key_file"])

creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestoredb.initialize_firestore(creds)
# print(firestoredb.read_data(db=db,collection_name="prabhat_khabar",document_id="29_DEC_2024"))

selected_model = "llama3-70b-8192"

question = "Enter your question (optional):", ""

options = ["Summary", "Key Points","Members"]

