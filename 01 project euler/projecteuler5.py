


#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def euler5(mydividend,myquotient):
    while myquotient <21:
            if mydividend % 100 == 0:
                print(mydividend)
            if mydividend % myquotient == 0:
                if myquotient == 20:
                    return mydividend
                myquotient += 1
            else:
                myquotient = 1
                mydividend +=20


print(euler5(2000,1))
