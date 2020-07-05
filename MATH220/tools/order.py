def order(item, mod, x=1):
    test = item ** x
    if test >= mod:
        while test >= mod:
            test = test - mod
        if test == 1:
            return item, x
        else:
            return order(item, mod, x+1)

    else:
        if test == 1:
            return item, x
        else:
            return order(item, mod, x+1)

def order_on_list(Z, mod):
    for item in Z:
        val, o = order(item, mod)
        print("-------------------------------")
        print("Element " + str(val) + " order: " + str(o))
        print("-------------------------------")
    return ""


z = [int(x) for x in input("Enter list (seporate with spaces): ").split()]
mod = int(input("Enter modulo: "))

print(order_on_list(z, mod))
