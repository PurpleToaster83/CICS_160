# William Van Uitert

def is_prime(n):
    # only have to check up to root n
    root = n**0.5

    # go over numbers from 2 up to the root
    for i in range(2, int(root + 1)):
        # if divisible then not prime
        if not(n % i):
            return False
    # otherwise it is prime
    return True

def are_relativley_prime(x, y):
    # set paramters to local variables
    a,b,r = max(x,y), min(x,y), 1

    # use the euclidian algorithm to check if coprime
    while r != 0:
        old_r = r
        r = a % b
        a = b
        b = r
    if old_r == 1: # check if the last remainder before 0 is 1
        return True
    return False

def primes_up_to(n):
    primes = []

    # check all numbers lower to see if prime
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def prime_decomposition(n):
    pos_factors = primes_up_to(n)

    # start with lowest prime
    # divide by it till can't anymore
    #check the next one

    while pos_factors:
        active = pos_factors.pop()


def decomp_check(n):
    pass

if __name__ == '__main__':
    n = 0

    while n != 'e':
        n = int(input('Number:'))
        print(f'Primes up to {n}: {primes_up_to(n)}')