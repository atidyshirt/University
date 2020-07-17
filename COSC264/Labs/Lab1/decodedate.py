def decodedate(encoded_date):
    """
    This function takes in an encoded date
    decodes it to get the desired format
    """
    # Dates use this format DD/MM/YYYY
    # The Date's binary representation is as follows:
    # (month = first 4-bits)
    # (Day = second  5-bits)  
    # (Year = last  23-bits)
    month = get_month(encoded_date)

def get_month(x):
    bitmask = 0b11110000000000000000000000000000
    month_pre = int('0b' + str(bin(x) & bitmask))
    month = (month_pre >> 28) + 0b1
    return month

# print(get_month(1107298273))

# END GOAL
# print(decodedate(1107298273)) #should return 5.5.2017
