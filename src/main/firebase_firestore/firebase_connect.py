import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def get_firebase_fire_store_db_client(cred_json_path):
    cred = credentials.Certificate(cred_json_path)
    firebase_admin.initialize_app(cred)
    db_client = firestore.client()
    return db_client
