# -*- coding: UTF-8 -*-

#The sum of the squares of the first ten natural numbers is,
#1² + 2² + ... + 10² = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)² = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



sumsquare = 0
sum = 0

for i in range(1, 101):
    sumsquare = sumsquare + i*i

for j in range(1, 101):
    sum = sum + j

print(sum)
print(sum*sum)
print(sum*sum - sumsquare)