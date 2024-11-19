from src.main.firebase_firestore.firebase_connect import (
    get_firebase_fire_store_db_client,
)


# Read operation on collection using collection name
def read_document_per_collection_dict(cred_json_path, collection_name) -> dict:
    docs_collection = []
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    col_ref = db_client.collection(collection_name)
    docs = col_ref.stream()
    for doc in docs:
        docs_collection.append(doc.to_dict())
    return docs_collection


# Create operation on collection using document ID
def create_document_in_collection(
    cred_json_path, collection_name, document_id, create_doc_dict
):
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    doc_ref = db_client.collection(collection_name).document(document_id)
    # set object and push to firebase
    doc_ref.set(create_doc_dict)
    print(f"Document created in : {collection_name}, with document id: {document_id}")


# Delete operation on collection using document ID
def delete_document_in_collection(cred_json_path, collection_name, document_id):
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    doc_ref = db_client.collection(collection_name).document(document_id).get()
    if doc_ref.exists:
        print(f"Document data that will be deleted: {doc_ref.to_dict()}")
        # delete document id in collection if it exists
        doc_ref.reference.delete()
        print(f"Deletion done on : {collection_name}, for document id: {document_id}")
    else:
        print(f"No such document present in {collection_name}!")


# Update operation on collection using document ID
def update_document_in_collection(cred_json_path, collection_name, document_id,update_field_dict):
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    doc_ref = db_client.collection(collection_name).document(document_id).get()
    if doc_ref.exists:
        print(f"Document data that will be deleted: {doc_ref.to_dict()}")
        # delete document id in collection if it exists
        doc_ref.reference.update(update_field_dict)
        print(f"Updates done on : {collection_name}, for document id: {document_id}")
    else:
        print(f"No such document present in {collection_name}!")