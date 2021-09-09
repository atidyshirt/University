a = [2,3,11,17]
primes = 979, 983

def fermats_prime(a, primes):
    for prime in primes:
        for ab in a:
            print("Number:", prime, "Value: ", ab**(prime-1) % prime)

def miller(n,a,u,v):
    b = a**u % n
    if b == 1:
        return True
    else:
        for _ in range(0, v-1):
            if b == -1:
                return True
            b = b**2 % n
        return False

print(miller(17, 11, 4, 2))
