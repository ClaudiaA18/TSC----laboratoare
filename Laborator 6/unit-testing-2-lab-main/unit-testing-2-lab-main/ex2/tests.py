import unittest
from ex2 import get_marks
from requests.exceptions import Timeout
from unittest.mock import patch
import ex2

class TestMarks(unittest.TestCase):
    @patch('ex2.requests.get')
    def test_get_marks_timeout(self, mock_get):
        mock_get.side_effect = Timeout
        result = ex2.get_marks()
        self.assertIsNone(result, "None la timeout.")

if __name__ == '__main__':
    unittest.main()
