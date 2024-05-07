import unittest
from ex5 import generate_fake_data, get_youngest_person

class TestPersonDatabase(unittest.TestCase):
    def setUp(self):
        self.db = generate_fake_data(10)

    def test_get_youngest_person(self):
        youngest = get_youngest_person(self.db)
        expected_youngest = min(self.db.values(), key=lambda x: x.age)
        self.assertEqual(youngest, expected_youngest, "Nu a returnat cea mai tanara persoana.")

if __name__ == '__main__':
    unittest.main()
