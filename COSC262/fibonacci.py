seq = {0:0, 1:1}

def fib(num):
    if num not in seq:
        seq[num] = fib(num-1) + fib(num-2)
    return seq[num]

print(fib(6))
