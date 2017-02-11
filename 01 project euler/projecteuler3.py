#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

#Zunächst müssen wir die Primzahlzerlegung machen.
#Die Primzahlen schreiben wir in eine Liste.
#Anschließend ziehen wir daraus das Maximum.


from math import sqrt
import math

primfaktorliste = []
dividend = 600851475143

def primfaktormax(dividend):
    quotient = 2
    while quotient * quotient < dividend:
        while dividend % quotient == 0:
            dividend = dividend / quotient
        quotient = quotient +1
    return dividend
        

#call the procedure
dividend = primfaktormax(dividend)

#print the result
print(dividend)