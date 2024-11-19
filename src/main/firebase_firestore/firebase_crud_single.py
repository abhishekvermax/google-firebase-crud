from src.main.firebase_firestore.firebase_connect import (
    get_firebase_fire_store_db_client,
)


def read_document_per_collection_dict(cred_json_path, collection_name) -> dict:
    docs_collection = []
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    col_ref = db_client.collection(collection_name)
    docs = col_ref.stream()
    for doc in docs:
        docs_collection.append(doc.to_dict())
    return docs_collection


def create_document_category_collection(cred_json_path, collection_name, document_id):
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    doc_ref = db_client.collection(collection_name).document(document_id)
    # set object and push to firebase
    doc_ref.set({"doc_id": document_id, "imageUrl": "sample_png", "name": "extra"})


def get_documentBy_id(cred_json_path, collection_name, document_id):
    db_client = get_firebase_fire_store_db_client(cred_json_path)
    db_client.collection(collection_name).doc(document_id).get()

