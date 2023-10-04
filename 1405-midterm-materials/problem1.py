""" Largest prime factor program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def largest_prime_factor(N):
    highest_prime_factor = 1
    for factor in range(1,N + 1):
        # Check if it is a factor
        if N % factor == 0:

            # Check if the factor is a prime number
            for counter in range(2,factor + 1):
                if factor == counter:
                    highest_prime_factor = factor
                if factor % counter == 0:
                    break
                

    return highest_prime_factor