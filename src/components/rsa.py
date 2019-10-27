import random
from gmpy2 import mpq, mpz
from math import gcd

def powMod(x, y, mod):
    """
    (Efficiently) Calculate and return `x' to the power of `y' mod `mod'.

    If possible, the three numbers are converted to GMPY's bignum
    representation which speeds up exponentiation.  If GMPY is not installed,
    built-in exponentiation is used.
    """

    x = mpz(x)
    y = mpz(y)
    mod = mpz(mod)
    return pow(x, y, mod)


def find_prime(bits):
    """
    Find prime using Fermat's little theorem.
    """
    prime_found = False

    lower_limit = 2**bits
    upper_limit = 2**(bits+1) - 1

    range_prime = upper_limit - lower_limit

    while not prime_found:
        random_ = random.randint(0, range_prime)
        n = random_ + lower_limit
        is_powMod_1 = powMod(2, n-1, n)
        if is_powMod_1 == 1:
            prime_found = True
    return n

def get_n(a,b):
    return a*b

def get_totient(a,b):
    return (a-1) * (b-1)

def find_coprime(totient):
    coprime_found = False
    i = 1
    while not coprime_found:
        i += 1
        coprime_found = gcd(i, totient) == 1
    return i

def find_d(totient, coprime):
    k = 1
    k = mpq(k)
    d = 2.9
    d = mpq(d)
    while d % 1 != 0:
        d = ((k * totient) + 1) / coprime
        k += 1
    return d

def encrypt(m, i, n):
    return powMod(m,i,n)

def decrypt(c, d, n):
    return powMod(c, d, n)

def str_to_ascii(m):
    int_m_decr = ""
    for c in m:
        ascii_c = ord(c)
        int_m_decr += str(ascii_c)
    return int_m_decr

def ascii_to_str(c):
    str_ascii = ""
    k = len(str(c))
    j = 0
    work = str(c)
    while j < k:
        if work[j] == '1':
            ascii_char = int(work[j:j+3])
            str_ascii += chr(ascii_char)
            j += 3
        else:
            ascii_char = int(work[j:j+2])
            str_ascii += chr(ascii_char)
            j += 2
    return str_ascii