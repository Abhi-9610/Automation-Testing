import requests
import unittest

class TestAPI(unittest.TestCase):
    BASE_URL = "http://yourapi.com/api"  # Replace with your actual API URL

    def test_get_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/endpoint")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_post_endpoint(self):
        payload = {"key": "value"}  # Replace with your actual payload
        response = requests.post(f"{self.BASE_URL}/endpoint", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_put_endpoint(self):
        payload = {"key": "new_value"}  # Replace with your actual payload
        response = requests.put(f"{self.BASE_URL}/endpoint/1", json=payload)  # Replace '1' with a valid ID
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["key"], "new_value")

    def test_delete_endpoint(self):
        response = requests.delete(f"{self.BASE_URL}/endpoint/1")  # Replace '1' with a valid ID
        self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()
