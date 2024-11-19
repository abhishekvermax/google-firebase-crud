import unittest
from src.main.firebase_firestore.firebase_connect import get_firebase_fire_store_db_client

class TestFirebaseCRUDSingle(unittest.TestCase):
    cred_json = ""

    def test_get_firebase_fire_store_db_client(self):
        db_c = get_firebase_fire_store_db_client(cred_json_path=self.cred_json)
        class_instance_str = 'google.cloud.firestore_v1.client.Client'
        bool_class_inst = True if class_instance_str in str(type(db_c)) else False
        self.assertTrue(bool_class_inst,True)


if __name__ == "__main__":
    unittest.main()
