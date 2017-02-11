#-*- coding:utf-8 - *-


def load_dataset():
    '''
    Returns the sample dataset.
    :return: set of itemsets.
    '''
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataset):
    '''
    Creates a list of candidate items of size one.
    :param dataset: set of itemsets.
    :return: map()
    '''
    C1 = set()
    for transaction in dataset:
        for item in transaction:
            #if not [item] in C1:
             C1.add(frozenset([item]))
                #elem = frozenset([item])
                #C1.append(elem)
                # beachte, dass c1 nicht aus Items, sondern aus 1-elementigen Mengen besteht.

    #Der Map-funktion wird eine Funktion und eine Liste übergeben.
    #Sie returned dann die Liste, aber auf alle Items wurde die Funktion angewandt.
    #In diesem Fall wurde aus jedem Element in C1 ein frozenset gemacht.
    #Vorteil vom frozenset: es ist unveränderbar und hashable.
    #return map(frozenset, C1)
    return C1

def scanD(dataset, candidates, min_support):
    '''

    :param dataset: set of itemsets
    :param candidates: itemset
    :param min_support: integer
    :return: returns all candidates that meet a minimum support level.
    '''
    #subset_count zählt, wie oft eine Kandidatenmenge im Dataset auftaucht.
    #subset_count ist ein dict.
    subeset_count = {}
    for tid in dataset:
        for can in candidates:
            if can.issubset(tid):
                subeset_count.setdefault(can, 0)
                subeset_count[can] +=1

    num_items = float(len(dataset))
    retlist = []
    support_data = {}
    for key in subeset_count:
        support = subeset_count[key] / num_items
        if support > min_support:
            retlist.insert(0,key)
        support_data[key] = support
    return retlist, support_data

    ## beachte, das da oben ZWEI Dinge returned werden! Pythonic!

def aprioriGen(freq_sets, k):
    '''
    Generate the joint transactions from candidate sets
    :param freq_sets:
    :param k:
    :return:
    '''
    retlist = []
    lenLk = len(freq_sets)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(freq_sets[i])[:k -2]
            L2 = list(freq_sets[j])[:k -2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retlist.append(freq_sets[i] | freq_sets[j])
    return retlist

def apriori(dataset, minsupport=0.4):
    '''
    Generate a list of candidate item sets
    :param dataset:
    :param minsupport:
    :return:
    '''
    C1 = createC1(dataset)
    D = map(set, dataset)
    L1, support_data = scanD(D,C1,minsupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) >0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D,Ck,minsupport)
        support_data.update(supK)
        L.append(Lk)
        k +=1
    return L, support_data