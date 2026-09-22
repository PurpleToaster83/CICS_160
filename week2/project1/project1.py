# William Van Uitert

def is_prime(n):
    # only have to check up to root of n
    root = n**0.5

    # go over numbers from 2 up to the root (inclusive)
    for i in range(2, int(root + 1)):
        # if divisible, then not prime
        if not(n % i):
            return False
    # otherwise if not 1, it's prime
    return n != 1

def are_relatively_prime(x, y):
    # set parameters to local variables
    a,b,r = max(x,y), min(x,y), 1

    if not (a % b): return False # check if x and y are mutltiples

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

    # check all numbers less than n for prime
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def prime_decomposition(n):
    # possible prime factors are primes less than n
    pos_factors = primes_up_to(n)

    running = n
    factors = []

    # run until the list of remaining possible factors is empty
    while pos_factors:
        active = pos_factors.pop() # select the element at the back

        # divide running by active until can no longer evenly divide
        while not(running % active):
            running /= active
            factors.append(active)

    # a number is a factor of itself (1 exclusive)
    if not(factors) and n != 1:
        return [n]
    return factors

def decomp_check(n):
    # find the prime decomposition of n
    decomp = prime_decomposition(n)

    # check the length and uniqueness of the decomposition
    if (len(decomp) == 2) and (decomp[0] != decomp[1]):
        return True
    return False

if __name__ == '__main__':
    n = 0

    while n != 'e':
        n = int(input('Number:'))
        print(f'Prime: {is_prime(n)}')
    