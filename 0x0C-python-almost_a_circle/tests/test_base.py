import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_empty_list(self):
        # Test to ensure that to_json returns '[]' for an empty list
        result = Base.to_json([])
        self.assertEqual(result, "[]")

    def test_to_json_non_empty_list(self):
        # Test to ensure that to_json returns valid JSON for a non-empty list
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        result = Base.to_json(data)
        expected_result = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(result, expected_result)

    # Add more test cases for other methods as needed

if __name__ == '__main__':
    unittest.main()
