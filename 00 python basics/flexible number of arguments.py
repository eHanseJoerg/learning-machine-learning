#Funktion definieren, die eine flexible Anzahl an Argumenten akzeptiert:

def add_numbers(*args):
    # das Asterisk heißt: "akzeptiere so viele Arguemnte wie halt kommen"
    # das *args word sehen wir auch viel in der Python Bibliothek
    total = 0
    for a in args:
        total += a
    print(total)



#Unpacking Arguments:
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + apples_ate * 3.5 - cigs_smoked *2
    print(answer)

# alter Weg des Funktionsaurfrufs:
joergs_data = [33,3,0]
health_calculator(joergs_data[0],joergs_data[1],joergs_data[2])
# neuer Weg: die Liste automatisch entpacken lassen
health_calculator(*joergs_data)

# Super coole Sache!



