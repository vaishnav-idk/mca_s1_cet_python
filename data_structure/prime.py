from sympy import isprime

def generate_mersenne_primes(limit):
    """
    Generate Mersenne primes up to a given limit.
    
    Parameters:
    limit (int): The maximum number of Mersenne primes to generate.
    
    Returns:
    list: A list of Mersenne primes.
    """
    mersenne_primes = []
    p = 2  # Start with the first prime number

    while len(mersenne_primes) < limit:
        mersenne_number = (2 ** p) - 1
        if isprime(mersenne_number):
            mersenne_primes.append(mersenne_number)
        p += 1
        # Find the next prime number
        while not isprime(p):
            p += 1

    return mersenne_primes

# Example usage:
limit = 10
print(f"The first {limit} Mersenne primes are:")
print(generate_mersenne_primes(limit))
