#!/usr/bin/python3
"""Module for a UTF-8 Validator.
"""


def _bin(integer):
    binary_string = ''
    while (integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    if len(binary_string) < 8:
        mul_factor = 8 - len(binary_string)
        binary_string = (str(0) * mul_factor) + binary_string
    elif len(binary_string) > 8:
        binary_string = binary_string[:8]
    return binary_string


def validUTF8(data):
    """ A method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    n_bytes = 0
    for num in data:
        bin_string = _bin(num)
        if n_bytes == 0:
            for bit in bin_string:
                if bit == '0':
                    break
                n_bytes += 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
                else:
                    if not (bin_string[0] == '1' and bin_string[1] == '0'):
                        return False

                n_bytes -= 1
    return n_bytes == 0
