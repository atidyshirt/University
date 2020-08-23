# Converting between different representations (ENCE260 lecture CA2)
# Python libraries include functions for doing this kind of thing.
# These functions are just to demonstrate how base conversion works.
#
# Allan McInnes / 2018-07-18


# Converting a binary sequence to decimal
def binary_to_unsigned_decimal(bits):
    """Takes a list of bits (0 or 1), MSB first, and returns the
    corresponding unsigned decimal (base 10) value.
    """
    # Note that because we assume MSB first, we reverse the bit list
    # prior to enumeration so that the indices work out correctly
    return sum(bit*(2**i) for i, bit in enumerate(reversed(bits)))
    # Equivalent to:
    # base10 = 0
    # for i, bit in enumerate(reversed(bits)):
    #   base10 += bit*(2**i)
    # return base10

# binary_to_unsigned_decimal([1, 0, 0, 0])
# binary_to_unsigned_decimal([0, 1, 0, 1])
# binary_to_unsigned_decimal([1, 1])

def hex_to_decimal(hexdigits):
    """Takes a list of hexadecimal digits (0-F), MS digit first, and returns the
    corresponding decimal (base 10) value.
    """
    lookup = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8,
              9:9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    return sum(lookup[val]*(16**i) for i, val in enumerate(reversed(hexdigits)))

# hex_to_decimal(['F', 5])
# hex_to_decimal(['F', 'E'])
# hex_to_decimal([0, 'A'])

def decimal_to_hex(decimal):
    """Takes a decimal number (digits 0-9), MS digit first, and returns the
    corresponding hexadecimal (base 16) value as a string.
    """
    lookup = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
              9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hexdigits = []  # We'll build a list of hex digits
    # To do base conversion, we repeatedly divide a number by the base
    # (16 in this case), and save the remainder of each division.
    # The remainder from the first division gives us the the part of
    # the number in the 16**0 position.
    # The remainder from the second division gives us the part of the number
    # at the 16**1 position. And so on.
    # Repeat until there's nothing left.
    while not decimal == 0:
        remainder = decimal % 16       # Find the remainder
        hexdigits += lookup[remainder] # Convert to hex digit and save
        decimal = decimal // 16        # Integer division (//)
    return "0x" + ''.join(reversed(hexdigits))

# decimal_to_hex(245)
# decimal_to_hex(254)
# decimal_to_hex(10)



