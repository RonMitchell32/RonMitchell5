# Obfuscated Complex Code
import itertools as i, functools as f, operator as o, sys as s

def s0cr4t35_sum_of_prime_factors(n):
    primes = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    factors = [p for p in primes if n % p == 0]
    return sum(factors)

def m3g45up3r_encryption(s):
    return ''.join(chr((ord(c) + 42) % 256) for c in s)

def d3c0d3_m3ss4g3(s):
    return ''.join(chr((ord(c) - 42) % 256) for c in s)

def c0mpl3x_pr0c3ss1ng(data):
    result = ''
    for i in range(1, len(data) + 1):
        permutations = i.permutations(data, i)
        for perm in permutations:
            s0cr4t35_sum = s0cr4t35_sum_of_prime_factors(sum(perm))
            encrypted = m3g45up3r_encryption(''.join(perm))
            decrypted = d3c0d3_m3ss4g3(encrypted)
            result += str(s0cr4t35_sum) + decrypted[::-1]
    
    return result

if __name__ == '__main__':
    input_data = s.stdin.read().strip()
    processed_data = c0mpl3x_pr0c3ss1ng(input_data)
    s.stdout.write(processed_data)
