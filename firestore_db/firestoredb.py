from google.cloud import firestore

# Initialize Firestore DB
def initialize_firestore(cred):
    # Ensure that the environment variable GOOGLE_APPLICATION_CREDENTIALS is set to the path of your service account key file
    return firestore.Client(credentials=cred)

# Write data to Firestore
def write_data(db, collection_name, document_id, data):
    db.collection(collection_name).document(document_id).set(data)
    print(f'Document {document_id} successfully written.')

# Read data from Firestore
def read_data(db, collection_name, document_id):
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
        return doc.to_dict()
    else:
        print(f'No such document!')
        return None

# if __name__ == "__main__":
#     db = initialize_firestore()
    
#     # Example usage
#     collection_name = 'your_collection'
#     document_id = 'your_document_id'
#     data = {'field1': 'value1', 'field2': 'value2'}
    
#     write_data(db, collection_name, document_id, data)
#     read_data(db, collection_name, document_id)
