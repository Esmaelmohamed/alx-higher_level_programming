import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_identity_increment(self):
        # Test if the identity is incremented correctly
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.identity, 1)
        self.assertEqual(base2.identity, 2)

    def test_save_load_from_file(self):
        # Test saving instances to a file and loading them back
        base1 = Base()
        base2 = Base()
        base3 = Base()

        Base.save_to_file([base1, base2, base3])
        loaded_instances = Base.load_from_file()
        self.assertEqual(len(loaded_instances), 3)

    # Add more test cases for other functionalities

if __name__ == '__main__':
    unittest.main()
