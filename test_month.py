import unittest
from month import get_days_in_month

class TestMonthDays(unittest.TestCase):
    
    def test_valid_months(self):
        self.assertEqual(get_days_in_month("січень"), 31)
        self.assertEqual(get_days_in_month("лютий"), 28)
        self.assertEqual(get_days_in_month("квітень"), 30)
        self.assertEqual(get_days_in_month("грудень"), 31)
    
    def test_case_insensitive(self):
        self.assertEqual(get_days_in_month("СІЧЕНЬ"), 31)
        self.assertEqual(get_days_in_month("Липень"), 31)
    
    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            get_days_in_month("unknown")
        with self.assertRaises(ValueError):
            get_days_in_month("")
    
    def test_whitespace(self):
        self.assertEqual(get_days_in_month("  січень  "), 31)

if __name__ == "__main__":
    unittest.main()