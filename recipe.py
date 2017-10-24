'''This issa Roman Numeral Converter'''

import unittest

class RomanNumeralConverter(object):
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.digital_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    def convert_to_decimal(self):
        '''Return the roman numeral given at initialization as a decimal value'''
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

    def test_parsing_millenia(self):
        '''Does it return 1000 when parsed "M"?'''
        value = RomanNumeralConverter("M")
        self.assertEqual(value.convert_to_decimal(), 1000)
    
    def test_parsing_half_millenia(self):
        '''Does it return 500 when parsed "D"?'''
        value = RomanNumeralConverter("D")
        self.assertEqual(value.convert_to_decimal(), 500)

    def test_parsing_century(self):
        '''Does it return 100 when parsed "C"?'''
        value = RomanNumeralConverter("C")
        self.assertEqual(value.convert_to_decimal(), 100)

    def test_parsing_half_century(self):
        '''Does it return 50 when parsed "L"?'''
        value = RomanNumeralConverter("L")
        self.assertEqual(value.convert_to_decimal(), 50)

    def test_parsing_decade(self):
        '''Does it return 10 when parsed "X"?'''
        value = RomanNumeralConverter("X")
        self.assertEqual(value.convert_to_decimal(), 10)   

    def test_parsing_half_decade(self):
        '''Does it return 5 when parsed "V"?'''
        value = RomanNumeralConverter("V")
        self.assertEqual(value.convert_to_decimal(), 5) 

    def test_parsing_one(self):
        '''Does it return 1 when parsed "I"?'''
        value = RomanNumeralConverter("I")
        self.assertEqual(value.convert_to_decimal(), 1)    

    def test_empty_roman_numeral(self):
        '''Does it return 0 when parsed an empty string?'''
        value = RomanNumeralConverter(" ")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    
    def test_no_roman_numeral(self):
        '''Does it raise a TypeError when parsed nothing?'''
        value = RomanNumeralConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)
        
if __name__ == '__main__':
    unittest.main()
