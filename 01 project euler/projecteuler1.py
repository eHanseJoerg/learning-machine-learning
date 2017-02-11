

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

dreien = []
fuenfen = []

for i in range(1000):
    if i % 3 == 0:
        dreien.append(i)
    elif i % 5 == 0:
        fuenfen.append(i)
    
summe = 0
for elem in dreien:
    summe = summe + elem
    
for elem5 in fuenfen:
    summe = summe + elem5

print(summe)



