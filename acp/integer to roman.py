class RomanConverter:
    """
    A class to convert integers to Roman numerals.
    """
    def _init_(self):
        self.roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        """
        Converts an integer to its Roman numeral representation.

        Args:
            num (int): The integer to convert. Must be between 1 and 3999.

        Returns:
            str: The Roman numeral representation of the integer.

        Raises:
            ValueError: If the input integer is out of the valid range.
        """
        if not isinstance(num, int) or not (1 <= num <= 3999):
            raise ValueError("Input must be an integer between 1 and 3999.")

        roman_numeral = ""
        for value, symbol in self.roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


if __name__ == "_main_":
    converter = RomanConverter()

    try:
        print(f"1994 in Roman numerals: {converter.int_to_roman(1994)}")
        print(f"58 in Roman numerals: {converter.int_to_roman(58)}")
        print(f"3 in Roman numerals: {converter.int_to_roman(3)}")
        print(f"3999 in Roman numerals: {converter.int_to_roman(3999)}")
        # Test invalid input
        # print(converter.int_to_roman(0))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Test another invalid input
        # print(converter.int_to_roman(4000))
        pass
    except ValueError as e:
        print(f"Error: {e}")