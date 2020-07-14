def convert(x: int, base: int):
    if type(x) != int:
        return -1
    if type(base) != int:
        return -2
    if x < 0:
        return -3
    if base in (0, 1):
        return -4
    new_value = []
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(x, base)
        if base >= 11:
            actual_value = mod
            mod = actual_value
        new_value.append(mod)
        div = x // base
        x = div
        if div == 0:
            return str(new_value[::-1])
        elif div == 1:
            new_value.append(div)
            return str(new_value[::-1])

    return new_value[::-1]

print(convert(1234, 10))
print (convert(1234, 16))
