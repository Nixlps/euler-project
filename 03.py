'''
Given a natural number n, create a algorithm that find the largest prime factor of n

Link: https://projecteuler.net/problem=3
'''
import math
primes = set()
def largestPrimeFactor(num):
    divisor = 2
    result = 1
    while num > 1:
        if num % divisor == 0 and isPrime(divisor):
            num /= divisor
            result = max(result, divisor)
        else:
            divisor += 1
    return num if result == 1 else result
        
def isPrime(k):
    if k in primes: return True
    
    for i in range(2, k):
        if k % i == 0: return False
        
    primes.add(k)
    return True

print(largestPrimeFactor(100)) 
print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))

'''
    Complexity Analysis

    Time: O(num * sqrt(num)) since the worst case goes when num is prime
    Space: O(k) where k is the number of primes that divides num
'''