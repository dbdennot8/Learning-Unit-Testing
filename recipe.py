'''This issa Roman Numeral Converter'''

import unittest

class RomanNumeralConverter(object):
    def __init__(self):
        self.digital_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    def convert_to_decimal(self, roman_numeral):
        '''Return the roman numeral given at initialization as a decimal value'''
        self.roman_numeral = roman_numeral
        val = 0
        if isinstance(self.roman_numeral, str):
            if self.roman_numeral == " ":
                return 0
            else:
                for char in self.roman_numeral:
                    val += self.digital_map[char]
                return val
        else:
            raise TypeError("Input type Unrecognized")

class RomanNumeralConverterTest(unittest.TestCase):
    
    def setUp(self):
        # print("Creating a new instance of RomanNumeralConverter class for testing")
        self.value = RomanNumeralConverter()
    
    def tearDown(self):
        # print("Destroying nolonger needed instance of RomanNumeralConverter class once testing is done\n")
        self.value = None

    def test_parsing_millenia(self):
        '''Does it return 1000 when parsed "M"?'''
        self.assertEqual(self.value.convert_to_decimal("M"), 1000)

    def test_parsing_half_millenia(self):
        '''Does it return 500 when parsed "D"?'''
        self.assertEqual(self.value.convert_to_decimal("D"), 500)

    def test_parsing_century(self):
        '''Does it return 100 when parsed "C"?'''
        self.assertEqual(self.value.convert_to_decimal("C"), 100)

    def test_parsing_half_century(self):
        '''Does it return 50 when parsed "L"?'''
        self.assertEqual(self.value.convert_to_decimal("L"), 50) 

    def test_parsing_decade(self):
        '''Does it return 10 when parsed "X"?'''
        self.assertEqual(self.value.convert_to_decimal("X"), 10)   

    def test_parsing_half_decade(self):
        '''Does it return 5 when parsed "V"?'''
        self.assertEqual(self.value.convert_to_decimal("V"), 5)   

    def test_parsing_one(self):
        '''Does it return 1 when parsed "I"?'''
        self.assertEqual(self.value.convert_to_decimal("I"), 1)  

    def test_empty_roman_numeral(self):
        '''Does it return 0 when parsed an empty string?'''
        self.assertTrue(self.value.convert_to_decimal(" ") == 0)
        self.assertFalse(self.value.convert_to_decimal(" ") > 0)
    
    def test_no_roman_numeral(self):
        '''Does it raise a TypeError when parsed nothing?'''
        self.assertRaises(TypeError, self.value.convert_to_decimal, None)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
