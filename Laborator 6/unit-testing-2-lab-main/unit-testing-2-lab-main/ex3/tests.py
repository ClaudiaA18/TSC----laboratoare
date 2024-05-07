import unittest
from unittest.mock import patch, mock_open
import ex3


class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        mocked_file_content = "3.5\n2.5\n10\n-2\n"
        m = mock_open(read_data=mocked_file_content)
        with patch('ex3.open', m):
            total = ex3.calculate_total("dummy_filename.txt")
            self.assertEqual(total, 14, "Suma numerelor ar trebui să fie 14")

if __name__ == '__main__':
    unittest.main()