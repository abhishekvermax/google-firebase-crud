import unittest
from src.main.firebase_firestore.firebase_crud_single import (
    create_document_in_collection,
    read_document_per_collection_dict,
)


class TestFirebaseCRUDSingle(unittest.TestCase):
    cred_json = "src\\main\\configs\\firebase_firestore\\authentication\\firebase_firestore_credentials.json"

    def test_read_document_per_collection_dict(self):
        db_dict: dict = read_document_per_collection_dict(
            cred_json_path=self.cred_json, collection_name="category"
        )
        self.assertTrue(len(db_dict), 4)

    def test_create_document_in_collection_dict(self):
        create_document_in_collection(
            cred_json_path=self.cred_json, collection_name="category",document_id="new_doc_id",
            updates_dict={"doc_id": "new_doc_id", "imageUrl": "sample_png", "name": "extra"}
        )
        read_after_creation = read_document_per_collection_dict(
            cred_json_path=self.cred_json, collection_name="category"
        )
        self.assertTrue(len(read_after_creation), 5)


# doc_ref.set({"doc_id": document_id, "imageUrl": "sample_png", "name": "extra"})

if __name__ == "__main__":
    unittest.main()
