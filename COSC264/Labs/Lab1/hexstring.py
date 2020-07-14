def hexstring(x):
    if type(x) != int:
        return -1
    if x < 0:
        return -3

    ALPHABET_VALUES = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
                       '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
                       '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
                       '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
                       '34': 'Y', '35': 'Z'}

    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(x, 16)
        if 16 >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = x // 16
        x = div
        if div == 0:
            new_value += "x0"
            return str(new_value[::-1])
        elif div == 1:
            new_value += str(div)
            new_value += "x0"
            return str(new_value[::-1])
    new_value += "x0"
    return new_value[::-1]

print(hexstring(1234))
