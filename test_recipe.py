'''Unittests for the module recipe.py'''

import unittest
from recipe import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    
    def setUp(self):
        # print("Creating a new instance of RomanNumeralConverter class for testing")
        self.value = RomanNumeralConverter()
    
    def test_parsing_millenia(self):
        '''Does it return 1000 when parsed "M"?'''
        self.assertEqual(self.value.convert_to_decimal("M"), 1000)

    def test_combination_1(self):
        '''Does it return 2017 when parsed "MMXVII"?'''
        self.assertEqual(self.value.convert_to_decimal("MMXVII"), 2017)

    def test_convert_to_decimal_1(self):
        '''Does it return "MMXVII" when parsed 2017?'''
        self.assertEqual(self.value.convert_to_roman(2017), "MMXVII")
    
    def test_parsed_value_zero(self):
        '''Does it return an empty string when parsed 0?'''
        self.assertEqual(self.value.convert_to_roman(0), "")


if __name__ == '__main__':
    import sys
    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(RomanNumeralConverterTest(test_name))

    unittest.TextTestRunner(verbosity=2).run(suite)
