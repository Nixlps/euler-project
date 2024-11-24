'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Given a natural number num, find the largest palindrome made from the product of two numbers with num digits.


Link: https://projecteuler.net/problem=4
'''

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def largestPalindrome(num):
    result = 0
    for i in range(10**num-1, 10**(num-1)-1, -1):
        for j in range(i, 10**(num-1)-1, -1):
            product = i*j
            
            if product <= result:
                break

            if isPalindrome(i*j):
                result = product
    return result

print(largestPalindrome(1))
print(largestPalindrome(2))
print(largestPalindrome(3))
print(largestPalindrome(4))
print(largestPalindrome(5))
# print(largestPalindrome(6))
# print(largestPalindrome(7))

'''
    Complexity Analysis
    Time: O(10^2num * log(num)) since the worst case goes when num is prime
    Space: O(log(num)) since the number of digits grows in log proportion
'''