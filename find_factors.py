

def find_factors(num):
    factors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    return sorted(factors)
