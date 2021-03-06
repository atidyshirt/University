def encodedate(day, month, year):
    """
    This function takes in an encoded date
    decodes it to get the desired format
    """
    # Dates use this format DD/MM/YYYY
    # The Date's binary representation is as follows:
    # (month = first 4-bits)
    # (Day = second  5-bits)  
    # (Year = last  23-bits)
    month_out = get_month(month)
    day_out = get_day(day)
    year_out = get_year(year)
    encoded_date = month_out + day_out + year_out
    return encoded_date

def get_month(x):
    bitmask = 0b11110000000000000000000000000000
    month_pre = x & bitmask
    month = (month_pre << 28) - 1
    return month

def get_day(x):
    bitmask = 0b00001111100000000000000000000000
    day_pre = x & bitmask
    day = (day_pre << 23) - 1
    return day

def get_year(x):
    bitmask = 0b0000000001111111111111111111111
    year_pre = x & bitmask
    year = (year_pre)
    return year

print(encodedate(5,5,2017)) #should return 1107298273
