import unittest
from unittest.mock import patch
from datetime import datetime
from ex1 import is_leap_year

class TestIsLeapYear(unittest.TestCase):
    @patch('ex1.datetime')
    def test_leap_year_true(self, mock_datetime):
        # Configuram mock-ul pentru a returna un an bisect
        mock_datetime.datetime.today.return_value = datetime(2020, 1, 1)
        result = is_leap_year()
        self.assertTrue(result, "Anul 2020 ar trebui sa fie bisect")

    @patch('ex1.datetime')
    def test_leap_year_false(self, mock_datetime):
        # Configuram mock-ul pentru a returna un an care nu este bisect
        mock_datetime.datetime.today.return_value = datetime(2019, 1, 1)
        result = is_leap_year()
        self.assertFalse(result, "Anul 2019 nu ar trebui sa fie bisect")

    def test_with_context_manager(self):
        with patch('ex1.datetime.datetime') as mock_datetime:
            # Testam atat pentru un an bisect cat si pentru unul non-bisect
            mock_datetime.today.return_value = datetime(2024, 1, 1)
            result = is_leap_year()
            self.assertTrue(result, "Anul 2024 ar trebui sa fie bisect")
            
            mock_datetime.today.return_value = datetime(2023, 1, 1)
            result = is_leap_year()
            self.assertFalse(result, "Anul 2023 nu ar trebui sa fie bisect")

if __name__ == '__main__':
    unittest.main()

