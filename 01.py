'''
Given a natural number num, create a algorithm that find the sum of all the multiples of 3 and 5 below num
Link: https://projecteuler.net/problem=1
'''

from time_measure import measure_time

def sumMultiplesOf3And5(num):
    result = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            result += i 
    return result

print(sumMultiplesOf3And5(10))
print(sumMultiplesOf3And5(1000))
print(sumMultiplesOf3And5(1000000))
measure_time(sumMultiplesOf3And5(1000000))

'''
    Complexity Analysis

    Time: O(num) since we basically have a loop o num steps
    Space: O(1) since we only created a int variable 
'''