'''This issa Roman Numeral Converter that also does the reverse'''


class RomanNumeralConverter(object):
    def __init__(self):
        self.digital_map = {"M": 1000, "D": 500,
                            "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

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

    def convert_to_roman(self, decimal_number):
        '''Returns a roman numeral given a decimal number'''
        self.decimal_number = decimal_number

        val = ""
        while decimal_number > 1000:
            val += "M"
            decimal_number -= 1000
        while decimal_number > 500:
            val += "D"
            decimal_number -= 500
        while decimal_number > 100:
            val += "C"
            decimal_number -= 100
        while decimal_number > 50:
            val += "L"
            decimal_number -= 50
        while decimal_number > 10:
            val += "X"
            decimal_number -= 10
        while decimal_number > 5:
            val += "V"
            decimal_number -= 5
        while decimal_number >= 1:
            val += "I"
            decimal_number -= 1
        return val
