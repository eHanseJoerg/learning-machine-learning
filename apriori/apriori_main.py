import apriori_classes
from apriori_classes import Item, Itemmenge


# Items initialisieren
items = dict()
items['A'] = Item('Seife')
items['B'] = Item('Shampoo')
items['C'] = Item('Shampoo')
items['D'] = Item('Duschgel')
items['E'] = Item('Zahnpasta')
items['F'] = Item('Zahnbürste')
items['G'] = Item('Haarfärbemittel')
items['H'] = Item('Haargel')
items['J'] = Item('Deodorant')
items['K'] = Item('Parfüm')
items['L'] = Item('Kosmetikartikel')

# Transaktionen initialisieren; Itemmenge ist eine Klasse, die von set (Python builtin) erbt
t1 = Itemmenge()
t1.update([items['A'], items['B'], items['D'], items['E']])
t2 = Itemmenge()
t2.update([items['B'], items['C'], items['G'], items['H'], items['L']])
t3 = Itemmenge()
t3.update([items['B'], items['C'], items['E'], items['F'], items['J']])
t4 = Itemmenge()
t4.update([items['B'], items['C'], items['D'], items['G'], items['J'], items['L']])
t5 = Itemmenge()
t5.update([items['A'], items['E'], items['F'], items['J']])
t6 = Itemmenge()
t6.update([items['B'], items['C'], items['D'], items['J'], items['K'], items['L']])
t7 = Itemmenge()
t7.update([items['A'], items['D'], items['E'], items['J']])
t8 = Itemmenge()
t8.update([items['B'], items['C'], items['G'], items['J'], items['K'], items['L']])
t9 = Itemmenge()
t9.update([items['A'], items['B'], items['C'], items['D']])
t10 = Itemmenge()
t10.update([items['B'], items['D'], items['L']])

#Datenbasis mit Transaktionen füllen
D = list()
D.append(t1)
D.append(t2)
D.append(t3)
D.append(t4)
D.append(t5)
D.append(t6)
D.append(t7)
D.append(t8)
D.append(t9)
D.append(t10)



def support(item, datenmenge):
    '''
    Berechne den Support eines Items in einer Menge von Itemmengen (Transaktionen)
    Dazu durchlaufe die Transaktionen der Datenmenge und prüfe, ob item enthalten ist.

    :param item: Item
    :param datenmenge: list()
    :return:
    '''
    count = 0
    for transaktionen in datenmenge:
        for i in transaktionen:
            if i == item:
                count += 1

    return count / len(D)


# Hier soll der AprioriGen - Algorithmus beginnen:
def aprioriGen(Lk_1):
    '''

    :param Lk_1: Itemmenge
    :return: Itemmenge-Menge
    '''


# Hier soll der Apriori - Algorithmus beginnen:
def apriori(datenbasis):
    '''
    Der Algorithmus generiert häufige Itemmengen

    :param datenbasis: Itemmenge[]
    :return: Itemmenge[]
    '''

    # 1. Bestimme häufige L - Datenmengen mit 1 Element:

    # 2. bestimme häufige Lk - Datenmengen mit k Elementen:
    k = 2
    a = set()
    while len(
        # ich brauche hier wieder eine Menge von Itemmengen
    ) > 0:
        Ck =


print(support(items['A'], D))



