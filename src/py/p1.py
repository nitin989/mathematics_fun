"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000

"""

## naive approach 
def sum_of_multiple_3_5(n):
    sum = 0 
    for i in range(n):
        if (i%3 ==0 or i%5==0):
            sum += i
    return sum

print(sum_of_multiple_3_5(1000))

# 234168

## optimal approach 
import math
target = 999
def sumDivisibleByN(num):
    p = int(target/num)
    return num*((p*(p+1))/2)

out = sumDivisibleByN(3) + sumDivisibleByN(5) - sumDivisibleByN(15)
print(out)