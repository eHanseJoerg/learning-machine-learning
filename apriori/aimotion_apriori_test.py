import aimotion_apriori

dataset = aimotion_apriori.load_dataset()
print('Das Ergebnis von load_dataset():')
print(dataset)

C1 = aimotion_apriori.createC1(dataset)
print('Das Ergebnis von createC1():')
print(C1)


D = dataset
#set(dataset)
print('Das steht in D:')
print(D)

L1, support_data = aimotion_apriori.scanD(D,C1,0.1)

print('Das steht in L1:')
print(L1)
