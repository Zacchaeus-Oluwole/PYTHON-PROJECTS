dataset = ['TREASON', 'ABLE TREASON', 'PORTABLE', 'THE MAN OF TREE'] # List of available words. You can add to it
data = set()
qs = 'Tre'  #Pass in the word or character to search
cc = 0
qsN = len(qs)
c = qsN
for i in dataset:
    dN = len(i)
    vN = (dN-qsN) + 1
    for m in range(vN):
        result = i[m:c]
        c+=1
        if result.lower() == qs.lower():
            # print(i)
            data.add(i)
        if (m+1) == vN:
            m = 0
            c = qsN
            break
print(list(data))