import unittest
from src.main.firebase_firestore.firebase_crud_single import (
    create_document_in_collection,
    delete_document_in_collection,
    read_document_per_collection_dict,
    update_document_in_collection,
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
            cred_json_path=self.cred_json,
            collection_name="category",
            document_id="new_doc_id",
            create_doc_dict={
                "doc_id": "new_doc_id",
                "imageUrl": "sample_png",
                "name": "extra",
            },
        )
        read_after_creation = read_document_per_collection_dict(
            cred_json_path=self.cred_json, collection_name="category"
        )
        self.assertTrue(len(read_after_creation), 5)

    def test_delete_document_in_collection(self):
        delete_document_in_collection(
            cred_json_path=self.cred_json,
            collection_name="category",
            document_id="new_doc_id"
        )
        read_after_deletion = read_document_per_collection_dict(
            cred_json_path=self.cred_json, collection_name="category"
        )
        self.assertTrue(len(read_after_deletion), 4)


    def test_update_document_in_collection(self):
        create_document_in_collection(
            cred_json_path=self.cred_json,
            collection_name="category",
            document_id="created_to_test_updates_doc_id",
            create_doc_dict={
                "doc_id": "new_doc_id",
                "imageUrl": "sample_png",
                "name": "extra",
            },
        )
        update_document_in_collection(
            cred_json_path=self.cred_json,
            collection_name="category",
            document_id="created_to_test_updates_doc_id",update_field_dict={
                "doc_id": "updated_doc_id"}
        )
        read_after_updation = read_document_per_collection_dict(
            cred_json_path=self.cred_json, collection_name="category"
        )
        self.assertTrue(len(read_after_updation), 5)
        delete_document_in_collection(
            cred_json_path=self.cred_json,
            collection_name="category",
            document_id="created_to_test_updates_doc_id"
        )


# doc_ref.set({"doc_id": document_id, "imageUrl": "sample_png", "name": "extra"})

if __name__ == "__main__":
    unittest.main()
