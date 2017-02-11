# A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#


palindrom= 9001

mini = 91
maxi = 999
i = mini
palindro = 0

while i < maxi:
    j = mini
    while j < maxi:
        kandidat = i *j
        if str(kandidat) == str(kandidat)[::-1]:
            if kandidat > palindro:
                palindro = kandidat
                print(str(palindro)[::-1])
        j = j+1
    i = i +1
    
