"""
///
///                      Ch.1 What is an Algorithm?
///                 Personal Project By Aaron Ramos 2025
///
/// Recursive implementation of Euclids Algorithm, which finds the great-
/// est common denominator of two inputs.
///
/// @euclids.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

import numpy as np

# Find GCD given two inputs using Euclidʻs algorithm using recursion:
# a = (q_0 * b) + r_0 ---> b = (q_1 * r) + r_1 until r_1 = 0;
# then r is the greatest common denominator

def rec_euclids(a, b):   
    if b == 0:
        return a
    return rec_euclids(b, a%b)

def main():
    # Test cases 1000x
    for i in range(1000):
        rand_int1 = np.random.randint(low=0, high=10000)
        rand_int2 = np.random.randint(low=0, high=10000)
        rec_ans   = rec_euclids(rand_int1, rand_int2)
        np_ans    = np.gcd(rand_int1, rand_int2)
        
        if rec_ans == np_ans:
            print(f"Test Passed: GCD({rand_int1}, {rand_int2}) = {rec_ans}")
        else:
            print("xxx TEST FAILED xxx")

if __name__ == "__main__":
    main()