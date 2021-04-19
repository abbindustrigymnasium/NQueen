import numba
import random
import numpy as np
from multiprocessing import Pool


with Pool(8) as p:
    pass
a = p.imap_unordered()

def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return np.zeros_like(base)
    # FIXME Wikipedia says: Assert :: (modulus - 1) * (modulus - 1) does not overflow base
    # Not sure what it means by "base" here: the "base" argument, or the bit representation?
    # Schneier's original doesn't mention this assertion.
    result = np.ones_like(base)
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


@numba.jit
def miller_rabin_numba(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        # a = random.randrange(2, n - 1)
        a = 44
        x = modular_pow(a, s, n)
        
        if x == 1:
            print("ifcase")
            continue
        if x == n - 1:
            print("ifcase")
            continue
            
        flag = True
        for _ in range(r - 1):
            x = pow(x, 2)
            x %= n 
            print("2x:", x, a, s, n)
            if x == n - 1:
                flag = False
        if flag:
            print("Flag")
            return False
    return True

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        # a = random.randrange(2, n - 1)
        a = 44
        x = modular_pow(a, s, n)
        print("a:", a, "s:", s, "n:", n, "x:", x)
        # print("x:", x, a, s, n)
        
        if x == 1 or x == n - 1:
            print("ifcase")
            continue

            
        flag = True
        for _ in range(r - 1):
            x = pow(x, 2)
            x %= n 
            if x == n - 1:
                flag = False
        if flag:
            return False
    return True

print(miller_rabin(79, 10))

print()
print("numba")
print(miller_rabin_numba(79, 10))

